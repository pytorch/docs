# torch.distributed.fsdp.fully_shard

## PyTorch FSDP2 (`fully_shard`)

PyTorch FSDP2 ([RFC](https://github.com/pytorch/pytorch/issues/114299)) provides
a fully sharded data parallelism (FSDP) implementation targeting performant
eager-mode while using per-parameter sharding for improved usability

- See the [Getting Started with FSDP2](https://pytorch.org/tutorials/intermediate/FSDP_tutorial.html)
tutorial for more information.
- If you are currently using FSDP1, consider migrating to FSDP2 using our
[migration guide](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html#fsdp1-to-fsdp2-migration-guide).

The user contract for `fully_shard(model)` is as follows

- For model initialization, fully_shard converts model.parameters() from
plain torch.Tensor to DTensor in-place. The parameters are moved to the
appropriate device according to the device mesh.
- Before forward and backward passes, pre-forward/backward hooks are
responsible for all-gathering the parameters and converting model.parameters()
from DTensor to plain torch.Tensor.
- After forward and backward passes, post-forward/backward hooks free
the unsharded parameters (no communication needed) and convert
model.parameters() from plain torch.Tensor back to DTensor.
- For the optimizer, it must be initialized with the DTensor model.parameters(),
and the optimizer step should be performed on DTensor parameters.
- Call `model(input)` instead of `model.forward(input)` to trigger pre-forward
hooks to all-gather parameters. To make model.forward(input) work, users must
either call `model.unshard()` explicitly or use `register_fsdp_forward_method(model, "forward")`
to register the forward method for hooking.
- fully_shard groups parameters together for a single all-gather. User should apply
fully_shard in a bottom-up manner. For example, in a Transformer model, fully_shard
should be applied to each layer before applying it to the root model. When applied
to the root model, fully_shard excludes model.parameters() from each layer and groups
the remaining parameters (e.g., embeddings, output projection) into a single
all-gather group.
- `type(model)` is "unioned" with `FSDPModule` in-place. For example, if model
is originally of type nn.Linear, then fully_shard changes `type(model)` from
nn.Linear to `FSDPLinear` in-place. `FSDPLinear` is an instance of both
nn.Linear and `FSDPModule`. It retains all methods of nn.Linear while also
exposing FSDP2-specific APIs under FSDPModule, such as `reshard()` and
`unshard()`.
- Fully Qualified Names (FQNs) for parameters remain unchanged. If we call
`model.state_dict()`, the FQNs are the same before and after applying
fully_shard. This is because fully_shard does not wrap the module but only
registers hooks to the original module.

### Communication Grouping and Scheduling

Each call to `fully_shard` creates one **communication group** containing all
parameters in the module that are not already assigned to a group from an
earlier call on a submodule. Each group's parameters are all-gathered together
in one collective before forward, and their gradients are reduce-scattered
together in one collective after backward. Unlike DDP, FSDP2 has no
`bucket_cap_mb` parameter -- the communication boundaries are determined
entirely by which modules you apply `fully_shard` to.

Consider a model with four submodules where `a`, `b`, `c`, and `d`
denote the number of parameters in each:

```
model[ m1[a] -> m2[b] -> m3[c] -> m4[d] ]
```

**If you only call** `fully_shard(model)` **(root only)**, all parameters are
in a single group. This means the entire forward and backward look like:

```
all-gather(a+b+c+d) -> forward(m1,m2,m3,m4) -> backward(m4,m3,m2,m1) -> reduce-scatter(a+b+c+d)
```

All communication happens as two large blocking operations with no overlap
with compute. This is almost never what you want.

**If you apply** `fully_shard` **per submodule** -- for example, calling
`fully_shard(m2)`, `fully_shard(m3)`, and then `fully_shard(model)` --
the remaining parameters (`a` and `d`) form the root group, while `m2`
and `m3` each get their own group.

In **forward**, all-gathers run on a separate CUDA stream, so the next
module's all-gather can overlap with the current module's forward compute.
Each module's pre-forward hook issues its own all-gather and waits for it to
complete before running the module. Because the CPU typically runs ahead of
the GPU, the next module's all-gather is issued on the AG stream while the
current module's forward is still executing on the compute stream:

```
time ──────────────────────────────────────────────►

compute: [wait] [ fwd(m1) | fwd(m2) | fwd(m3,m4) ]
AG stream: [AG(a,d)] [AG(b) | AG(c) ]
```

While `fwd(m1)` runs on the compute stream, the CPU fires `m2`'s
pre-forward hook, which issues `AG(b)` on the AG stream. To make this
overlap more robust (e.g. when CPU-side overhead reduces the lead), use
`set_modules_to_forward_prefetch` to issue the next all-gather earlier --
inside the current module's pre-forward hook rather than waiting for the next
module's hook to fire.

In **backward**, FSDP2 additionally prefetches the next module's all-gather
explicitly and runs reduce-scatters on a separate CUDA stream, all without
any additional configuration:

```
time ──────────────────────────────────────────────►

compute: [ bwd(m4,m3) | bwd(m2) | bwd(m1) ]
AG stream: [AG(c)] [ AG(b) | AG(a,d) ]
RS stream: |[RS(c)] [ RS(b)| RS(a,d) ]
```

While `bwd(m4,m3)` runs on the compute stream, the all-gather for `b`
(needed by `m2`) is prefetched on the AG stream. While `bwd(m2)` runs,
both `AG(a,d)` and `RS(c)` overlap with compute. This pipelining is why
the recommended pattern is to apply `fully_shard` bottom-up to each layer
before applying it to the root.

To control the size of each communication group, choose which modules to wrap:
wrapping more fine-grained modules produces smaller, more overlappable groups
(similar to smaller DDP buckets), while wrapping fewer modules produces larger
groups. There is no automatic bucketing -- the grouping is explicit and
determined by the module structure.

Compared to PyTorch FSDP1 (`FullyShardedDataParallel`):

- FSDP2 uses `DTensor`-based dim-0 per-parameter sharding for a simpler
sharding representation compared to FSDP1's flat-parameter sharding, while
preserving similar throughput performance. More specifically, FSDP2 chunks
each parameter on dim-0 across the data parallel workers (using
`torch.chunk(dim=0)`), whereas FSDP1 flattens, concatenates, and chunks a
group of tensors together, making reasoning about what data is present on
each worker and resharding to different parallelisms complex. Per-parameter
sharding provides a more intuitive user experience, relaxes constraints
around frozen parameters, and allows for communication-free (sharded) state
dicts, which otherwise require all-gathers in FSDP1.
- FSDP2 implements a different memory management approach to handle the
multi-stream usages that avoids `torch.Tensor.record_stream`. This ensures
deterministic and expected memory usage and does not require blocking the CPU
like in FSDP1's `limit_all_gathers=True`.
- FSDP2 exposes APIs for manual control over prefetching and collective
scheduling, allowing power users more customization. See the methods on
`FSDPModule` below for details.
- FSDP2 simplifies some of the API surface: e.g. FSDP2 does not directly
support full state dicts. Instead, users can reshard the sharded state dicts
containing `DTensor` s to full state dicts themselves using `DTensor`
APIs like `DTensor.full_tensor()` or by using higher-level APIs like
[PyTorch Distributed Checkpoint](https://pytorch.org/docs/stable/distributed.checkpoint.html) 's
distributed state dict APIs. Also, some other args have been removed; see
[here](https://github.com/pytorch/torchtitan/blob/main/docs/fsdp.md) for
details.

The frontend API is `fully_shard` that can be called on a `module`:

torch.distributed.fsdp.fully_shard(*module*, ***, *mesh=None*, *reshard_after_forward=None*, *shard_placement_fn=None*, *mp_policy=MixedPrecisionPolicy(param_dtype=None, reduce_dtype=None, output_dtype=None, cast_forward_inputs=True)*, *offload_policy=OffloadPolicy()*, *ignored_params=None*, *dp_mesh_dims=None*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L97)

Apply fully sharded data parallelism (FSDP) to `module`, where FSDP
shards module parameters, gradients, and optimizer states across data
parallel workers to save memory at the cost of communication.

At initialization, FSDP shards the module's parameters across the data
parallel workers given by `mesh`. Before forward, FSDP all-gathers the
sharded parameters across the data-parallel workers to get the unsharded
parameters for forward computation. If `reshard_after_forward` is
`True`, then FSDP frees the unsharded parameters after forward and
re-all-gathers them in backward before gradient computation. After gradient
computation, FSDP frees the unsharded parameters and reduce-scatters the
unsharded gradients across data-parallel workers.

This implementation represents the sharded parameters as `DTensor` s
sharded on dim-0, while the unsharded parameters will be like the original
parameters on `module` (e.g. [`torch.Tensor`](tensors.html#torch.Tensor) if originally
[`torch.Tensor`](tensors.html#torch.Tensor)). A module
[forward pre-hook](https://pytorch.org/docs/main/generated/torch.nn.Module.html#torch.nn.Module.register_forward_pre_hook)
on `module` all-gathers the parameters, and a module
[forward hook](https://pytorch.org/docs/main/generated/torch.nn.Module.html#torch.nn.Module.register_forward_hook)
on `module` frees them (if needed). Similar backward hooks all-gather
parameters and later free parameters and reduce-scatter gradients.

Since grouping multiple tensors together for one collective is critical for
communication efficiency, this implementation makes this grouping first
class. Calling `fully_shard()` on `module` constructs one group that
includes the parameters in `module.parameters()` except those already
assigned to a group from an earlier call on a submodule. This means that
`fully_shard()` should be called bottom-up on your model. Each group's
parameters are all-gathered in one collective, and its gradients are
reduce-scattered in one collective. Partitioning the model into multiple
groups ("layer by layer") allows for peak memory savings and communication/computation
overlap. Users generally should *not* call `fully_shard()` only on the
topmost root module.

When called with a list (`fully_shard([a, b, ...])`), the model's
forward may run only a subset of the grouped modules, with the rest
called later in the same iteration. Chunked-loss training with
`fully_shard([norm, head])` is the motivating case: the main forward
runs norm only, then head is invoked per chunk. Caveats:

- Each standalone per-chunk invocation registers its own post_backward
autograd node, so N chunk calls produce N reduce-scatters for that
group.
- `mp_policy.cast_forward_inputs` and `mp_policy.output_dtype`
both apply per module in the group -- every invocation (including
each standalone per-chunk call) casts its inputs to `param_dtype`
and its output to `output_dtype`.

Note

If `forward()` or `backward()` raises, FSDP's per-iteration
state (iteration forward-root marker, grouped-module run
trackers, in-flight collective state, per-group training states)
is left in an undefined condition. To recover and run another
iteration, call `FSDPModule.reset_iter_state()` on the root
FSDP module. The failed iteration's gradients are discarded,
including any `no_sync` / HSDP partial-reduce accumulation
state.

Parameters:

- **module** (*Union**[*[*nn.Module*](generated/torch.nn.Module.html#torch.nn.Module)*,**List**[*[*nn.Module*](generated/torch.nn.Module.html#torch.nn.Module)*]**]*) - The module or modules to
shard with FSDP and group together for communication.
- **mesh** (*Optional**[*[*DeviceMesh*](distributed.html#torch.distributed.device_mesh.DeviceMesh)*]*) - This data parallel mesh defines the
sharding and device. If 1D, then parameters are fully sharded
across the 1D mesh (FSDP) with `(Shard(0),)` placement. If 2D,
then parameters are sharded across the 1st dim and replicated
across the 0th dim (HSDP) with `(Replicate(), Shard(0))`
placement. The mesh's device type gives the device type used for
communication; if a CUDA or CUDA-like device type, then we use the
current device.
- **reshard_after_forward** (*Optional**[**Union**[*[*bool*](https://docs.python.org/3/library/functions.html#bool)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]**]*) -

This controls the parameter
behavior after forward and can trade off memory and communication:

- If `True`, then this reshards parameters after forward and
re-all-gathers in backward.
- If `False`, then this keeps the unsharded parameters in memory
after forward and avoids the all-gather in backward. For best performance,
we usually set `False` for the root module, because the root module
is typically required immediately when the backward pass begins.
- If `None`, it is set to `True` for non-root modules and `False`
for root modules.
- If an `int`, then this represents the world size to reshard to
after forward. It should be a non-trivial divisor of the `mesh`
shard dim size (i.e. excluding 1 and the dim size itself). A
choice may be the intra-node size (e.g. `torch.cuda.device_count()`).
This allows the all-gather in backward to be over a smaller world
size at the cost of higher memory usage than setting to `True`.
- After forward, the parameters registered to the module depend on
to this: The registered parameters are the sharded parameters if
`True`; unsharded parameters if `False`; and the parameters
resharded to the smaller mesh otherwise. To modify the parameters
between forward and backward, the registered parameters must be
the sharded parameters. For `False` or an `int`, this can be
done by manually resharding via `reshard()`.
- **shard_placement_fn** (*Optional**[**Callable**[**[**nn.Parameter**]**,**Optional**[*[*Shard*](distributed.tensor.html#torch.distributed.tensor.placement_types.Shard)*|**ShardPlacementResult**]**]**]*) -

This callable can be used to override the sharding placement and/or
mesh for a parameter. It can return:

- `None`: Use default sharding (Shard(0)) on the mesh passed to
`fully_shard`.
- `Shard`: Shard the parameter on the specified dimension
using the mesh passed to `fully_shard`.
- `ShardPlacementResult`: Specify both the shard placement
and a custom `FSDPMeshInfo`. This allows different
parameters to be sharded across different process groups, enabling
use cases like Mixture of Experts where expert params use a
different mesh than regular params.

If sharding on a nonzero dim, we currently require even sharding,
i.e. the tensor dim size on that dim must be divisible by the FSDP
shard mesh size.
- **mp_policy** (*MixedPrecisionPolicy*) - This controls the mixed precision
policy, which offers parameter/reduction mixed precision for this
module. See `MixedPrecisionPolicy` for details.
- **offload_policy** (*OffloadPolicy*) - This controls the offloading policy,
which offers parameter/gradient/optimizer state offloading. See
`OffloadPolicy` and its subclasses for details.
- **ignored_params** ([*set*](https://docs.python.org/3/library/stdtypes.html#set)*[**nn.Parameter**]**|**None*) - Optional(Set[nn.Parameter]): The set of parameters to be
ignored by FSDP. They will not be sharded, nor moved to the device
during init, nor have their gradients reduced in backward.
- **dp_mesh_dims** (*Optional**[**DataParallelMeshDims**]*) - When provided,
`mesh` is treated as the full SPMD mesh, and parameters should be
DTensors on this mesh with `Replicate()` on all DP dimensions.
The `shard` field names which dim(s) FSDP shards on (multiple
dims are flattened). The `replicate` field names the HSDP
replication dim(s) (multiple dims are flattened).

Returns:

The module with FSDP applied (in-place).

Return type:

FSDPModule

*class*torch.distributed.fsdp.FSDPModule(**args*, ***kwargs*)

reset_iter_state()[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L375)

Resets FSDP's per-iteration state after an exception aborted a
forward or backward mid-flight. The supported recovery workflow is:

1. Catch the exception from `forward()` or `backward()`.
2. Call `reset_iter_state()` on the *root* FSDP module.
3. Run the next iteration normally.

The reset waits on any in-flight all-gather/reduce-scatter events,
reshards every parameter group, and clears iteration trackers
(`iter_forward_root`, `_modules_to_run_forward`, post-forward
order, per-group training states). Any in-flight gradient
reductions are discarded: the failed iteration's gradients are
lost, including HSDP partial-reduce-accumulation state and
`no_sync` grad-accumulation state. Callers doing gradient
accumulation should treat the microbatch sequence as invalidated
and restart it.

Must be called on the root FSDP module -- i.e. the module the
top-level `fully_shard` was applied to, equivalently the
module first forwarded. Calling on a non-root module raises
`RuntimeError`.

reshard()[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L335)

Reshards the module's parameters, freeing the unsharded parameters if
they are allocated and registering the sharded parameters to the
module. This method is *not* recursive.

set_all_reduce_hook(*hook*, ***, *stream=None*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L591)

Parameters:

- **hook** (*Callable**[**[*[*torch.Tensor*](tensors.html#torch.Tensor)*]**,**None**]*) - User-defined all-reduce hook
with expected signature `hook(reduce_output: torch.Tensor) -> None`
where `reduce_output` is the reduce-scatter output if only
using FSDP or the all-reduce output if using native HSDP.
- **stream** (*Optional**[*[*torch.cuda.Stream*](generated/torch.cuda.Stream_class.html#torch.cuda.Stream)*]*) - Stream to run the all-reduce
hook in. This should only be set if not using native HSDP. If
using native HSDP, the hook will run in the internally defined
all-reduce stream used by the native HSDP all-reduce.

set_allocate_memory_from_process_group_for_comm(*enable*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L807)

Sets whether the temporary staging buffers used to send and receive data
over collective communications should be allocated using the custom
optimized allocator provided by the ProcessGroup itself (if any). This
might allow the ProcessGroup to be more efficient. For example, when
using NCCL, this enables it to leverage zero-copy transfers over SHARP
(for NVLink and/or InfiniBand).

This cannot be used together with `set_custom_all_gather()` or
`set_custom_reduce_scatter()` as those APIs allow for
finer-grained control over each communication, and this method cannot
determine their staging buffer allocation strategy.

Parameters:

**enable** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to turn on ProcessGroup allocation.

set_custom_all_gather(*comm*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L553)

Overrides the default `all_gather` communication behavior,
to have better control over the communication and memory usage.
See Comm and ReduceScatter for details.

Parameters:

**comm** (*AllGather*) - Custom all-gather communication.

set_custom_reduce_scatter(*comm*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L572)

Overrides the default `reduce_scatter` communication behavior,
to have better control over the communication and memory usage.
See Comm and ReduceScatter for details.

Parameters:

**comm** (*ReduceScatter*) - Custom reduce_scatter communication.

set_force_sum_reduction_for_comms(*enable*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L659)

Sets whether to require the low-level collective communication
primitives to exclusively use "sum"-type reductions, even if it comes
at the cost of separate additional pre- or post-scaling operations.
This is needed for example because NCCL currently supports zero-copy
transfers only for this kind of collectives.

NB: for MTIA devices, this is always implicitly enabled.

NB: if set_all_reduce_hook is used under FSDP setup, the caller needs
to ensure the custom all-reduce across FSDP units follow this strategy
as well, as FSDP can no longer automatically handle that.

Parameters:

**enable** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to only ever use ReduceOp.SUM for comms.

set_gradient_divide_factor(*factor*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L646)

Sets a custom divide factor for the gradient reduction. This might use
a custom reduce op using NCCL's PreMulSum, which allows multiplying by
the factor before reduction.

Parameters:

**factor** ([*float*](https://docs.python.org/3/library/functions.html#float)) - Custom divide factor.

set_is_last_backward(*is_last_backward*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L403)

Sets whether the next backward is the last one. On the last backward,
FSDP waits on pending gradient reduction and clears internal data
data structures for backward prefetching. This can be useful for
microbatching.

set_modules_to_backward_prefetch(*modules*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L533)

Sets the FSDP modules for which this FSDP module should explicitly
prefetch all-gathers in backward. This overrides the default backward
pretching implementation that prefetches the next FSDP module based on
the reverse post-forward order.

Passing a singleton list containing the previous FSDP module gives the
same all-gather overlap behavior as the default overlap behavior.
Passing a list with at least length two is required for more aggressive
overlap and will use more reserved memory.

Parameters:

**modules** (*List**[**FSDPModule**]*) - FSDP modules to prefetch.

set_modules_to_forward_prefetch(*modules*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L513)

Sets the FSDP modules for which this FSDP module should explicitly
prefetch all-gathers in forward. The prefetching runs after this
module's all-gather copy-out.

Passing a singleton list containing the next FSDP module gives the same
all-gather overlap behavior as the default overlap behavior, except the
prefetched all-gather is issued earlier from the CPU. Passing a list
with at least length two is required for more aggressive overlap and
will use more reserved memory.

Parameters:

**modules** (*List**[**FSDPModule**]*) - FSDP modules to prefetch.

set_post_optim_event(*event*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L622)

Sets a post-optimizer-step event for the root FSDP module to wait the
all-gather streams on.

By default, the root FSDP module waits the all-gather streams on the
current stream to ensure that the optimizer step has finished before
all-gathering. However, this may introduce false dependencies if
there is unrelated computation after the optimizer step. This API
allows the user to provide their own event to wait on. After the root
waits on the event, the event is discarded, so this API should be
called with a new event each iteration.

Parameters:

**event** ([*torch.Event*](generated/torch.Event.html#torch.Event)) - Event recorded after the optimizer step
to wait all-gather streams on.

set_reduce_scatter_divide_factor(*factor*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L641)

Use `set_gradient_divide_factor()` instead

set_reduce_scatter_max_input_buffers(*max_input_buffers*, ***, *recurse=True*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L707)

Sets how many gradient reduce-scatter input buffers may be in flight at
once - the copy-in (`chunk_cat`) buffer cap-K (experimental).

FSDP keeps **1** such buffer in flight by default, so the compute stream
must wait on the previous reduce-scatter before the next copy-in can
reuse that buffer. When the reduce-scatter is exposed (communication
slower than the backward compute meant to hide it), that recycle wait
stalls the compute stream. Raising the cap lets the next copy-in write a
**fresh** buffer instead of waiting - removing the stall - at the cost
of extra peak memory for the retained buffers. The copy-in stays on the
compute stream; there is no extra stream and no `record_stream`. This
helps only when the reduce-scatter is exposed.

Parameters:

- **max_input_buffers** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Max reduce-scatter input buffers retained in
flight (the memory<->overlap dial); must be `>= 1`. `1` is
FSDP's default behavior (single buffer; the exposed-RS stall). A
small value (e.g. `2`) bounds peak memory and adds no stall as
long as it is `>=` the reduce-scatter pipeline depth (otherwise
an exposed reduce-scatter trades back a tail stall); a larger
value retains more buffers for deeper overlap at higher peak
memory.
- **recurse** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to set for all FSDP submodules or just the
passed-in module.

set_reduce_scatter_unused_params(*reduce_scatter_unused_params*, ***, *recurse=True*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L680)

Sets whether to include zero gradients for parameters that did not
receive a gradient in backward. This is needed when different ranks
use different parameters due to conditional control flow (e.g.
multi-modal models, mixture of experts), causing mismatched
reduce-scatter collectives. Similar to DDP's
`find_unused_parameters`.

Parameters:

- **reduce_scatter_unused_params** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to include zero
gradients for unused parameters in gradient reduction.
- **recurse** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to set for all FSDP submodules or just
the passed-in module.

set_requires_all_reduce(*requires_all_reduce*, ***, *recurse=True*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L437)

Sets if the module should all-reduce gradients. This can be used to
implement gradient accumulation with only reduce-scatter but not
all-reduce for HSDP.

set_requires_gradient_sync(*requires_gradient_sync*, ***, *recurse=True*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L413)

Sets if the module should sync gradients. This can be used to implement
gradient accumulation *without communication*. For HSDP, this controls
both reduce-scatter and all-reduce together. This is the equivalence of
no_sync in FSDP1.

Parameters:

- **requires_gradient_sync** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to reduce gradients for the
module's parameters.
- **recurse** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to set for all FSDP submodules or just the
passed-in module.

set_reshard_after_backward(*reshard_after_backward*, ***, *recurse=True*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L490)

Sets if the module should reshard parameters after backward. This can
be used during gradient accumulation to trade off higher memory for
reduced communication since the unsharded parameters do not need to be
re-all-gathered before the next forward.

Parameters:

- **reshard_after_backward** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to reshard parameters after
backward.
- **recurse** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to set for all FSDP submodules or just the
passed-in module.

set_reshard_after_forward(*reshard_after_forward*, *recurse=True*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L453)

Sets if the module should reshard parameters after forward. This can be
used to change the `reshard_after_forward` FSDP arg at runtime. For
example, this can be used to set the FSDP root module's value to
`True` (since it is otherwise specially set to `False`), or it can
set an FSDP module's value to `False` for running evals and set back
to `True` for training.

Parameters:

- **reshard_after_forward** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to reshard parameters after
forward.
- **recurse** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to set for all FSDP submodules or just the
passed-in module.

set_separate_reduce_scatter_group(*enable=True*, ***, *recurse=True*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L758)

Enables (or disables) running gradient reduce-scatter on its own process
group so it can overlap with all-gather in the backward pass
(experimental).

By default FSDP runs all-gather and reduce-scatter on separate CUDA
streams but through the **same** process group - one NCCL communicator,
which processes one collective at a time and so serializes them on the
wire. When enabled, FSDP creates a dedicated process group over the shard
ranks (`dist.new_group(..., use_local_synchronization=True)`) - one
per distinct set of shard ranks, typically a single communicator - so
the two collectives can progress concurrently when the network can
sustain it. This is collective for each shard rank set: like other FSDP
comm setup, call it consistently across ranks using this FSDP mesh.

Parameters:

- **enable** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - `True` (default) gives reduce-scatter its own
process group; `False` resets it to the shared shard/all-gather
group.
- **recurse** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to set for all FSDP submodules or just the
passed-in module.

set_symm_mem_for_comm(*backend='NCCL'*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L828)

Sets the symmetric memory (`symm_mem`) backend for allocating the
staging buffers used in all-gather collectives. This allows NCCL to use
optimized all-gather implementations via symmetric memory. Such
optimization may depend on the topology of the system. For single node,
Copy Engine All-Gather may be used. For multi-node, Symmetric Kernel
All-Gather may be used.

To enable Copy Engine All-Gather, you need to set the NCCL process group
with the zero-CTA policy.
`python
opts = dist.ProcessGroupNCCL.Options()
opts.config.cta_policy = dist.ProcessGroupNCCL.NCCL_CTA_POLICY_ZERO
dist.init_process_group(backend="nccl", pg_options=opts, device_id=device)
`
Alternatively, you can set the environment variable NCCL_CTA_POLICY to 2.
`bash
export NCCL_CTA_POLICY=2
`
For more details, see [Copy Engine
Collectives]([https://docs.pytorch.org/docs/2.11/symmetric_memory.html#copy-engine-collectives](https://docs.pytorch.org/docs/2.11/symmetric_memory.html#copy-engine-collectives)).

This cannot be used together with `set_custom_all_gather()` or
`set_custom_reduce_scatter()`.

Parameters:

**backend** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The symmetric memory backend to use. Defaults to
`"NCCL"`. Currently, only `"NCCL"` is supported.

set_unshard_in_backward(*unshard_in_backward*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L796)

Sets whether the FSDP module's parameters need to be unsharded in
backward. This can be used in expert cases when the user knows that all
parameters in this FSDP module's parameter group are not needed for
backward computation (e.g. embedding).

unshard(*async_op=False*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L345)

Unshards the module's parameters by allocating memory and all-gathering
the parameters. This method is *not* recursive. The unshard follows the
`MixedPrecisionPolicy`, so it will all-gather following
`param_dtype` if set.

Parameters:

**async_op** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True`, then returns a `UnshardHandle`
that has a `wait()` method to wait on the unshard op. If
`False`, then returns `None` and waits on the handle inside
this function.

Return type:

*UnshardHandle* | None

Note

If `async_op=True`, then FSDP will wait on the pending
unshard in the module's pre-forward for the user. The user only
needs to call `wait()` explicitly if the wait should happen
before pre-forward.

*class*torch.distributed.fsdp.UnshardHandle

A handle to wait on a `FSDPModule.unshard()` op.

wait()[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L907)

Waits on the unshard op. This ensures that the current stream can use
the unsharded parameters, which are now registered to the module.

torch.distributed.fsdp.register_fsdp_forward_method(*module*, *method_name*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L927)

Registers a method on `module` to be considered a forward method for
FSDP.

FSDP all-gathers parameters pre-forward and optionally frees parameters
post-forward (depending on `reshard_after_forward`). FSDP only knows to
do this for `nn.Module.forward()` by default. This function patches a
user-specified method to run the pre/post-forward hooks before/after the
method, respectively. If `module` is not an `FSDPModule`, then
this is a no-op.

Parameters:

- **module** ([*nn.Module*](generated/torch.nn.Module.html#torch.nn.Module)) - Module to register the forward method on.
- **method_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Name of the forward method.

*class*torch.distributed.fsdp.MixedPrecisionPolicy(*param_dtype=None*, *reduce_dtype=None*, *output_dtype=None*, *cast_forward_inputs=True*)

This configures FSDP's mixed precision. Unlike autocast, this applies mixed
precision at the module level, not op level, which means low-precision
activations are saved for backward and high-to-low-precision casts are
incurred only at module boundaries.

FSDP works well with module-level mixed precision since it keeps the
high-precision sharded parameters in memory anyway. In other words, FSDP
does not require any extra memory to keep a high-precision copy of the
parameters for the optimizer step.

Variables:

- **param_dtype** (*Optional**[*[*torch.dtype*](tensor_attributes.html#torch.dtype)*]*) - This specifies the dtype for
the unsharded parameter and hence the dtype for forward/backward
computation and the parameter all-gather. If this is `None`, then
the unsharded parameter uses the original dtype. The optimizer step
uses the sharded parameter in the original dtype. (Default:
`None`)
- **reduce_dtype** (*Optional**[*[*torch.dtype*](tensor_attributes.html#torch.dtype)*]*) - This specifies the dtype for
gradient reduction (i.e. reduce-scatter or all-reduce). If this is
`None` but `param_dtype` is not `None`, then the reduction
uses the compute dtype. This can be used to run gradient reduction
in full precision while using low precision for compute. If also
gradient reduction is disabled via `set_requires_gradient_sync()`,
then FSDP will accumulate gradients using `reduce_dtype`.
(Default: `None`)
- **output_dtype** (*Optional**[*[*torch.dtype*](tensor_attributes.html#torch.dtype)*]*) - This specifies the dtype for
casting floating-point forward outputs. This can be used to
help implement cases where different modules have different mixed
precision policies. (Default: `None`)
- **cast_forward_inputs** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - This specifies whether FSDP should cast the
forward's floating-point input tensors to `param_dtype` or not.
For grouped `fully_shard([a, b, ...])`, the cast is applied per
module, before each module's forward.

*class*torch.distributed.fsdp.OffloadPolicy

This base class represents the policy of no offloading and is only used as
the default value for the `offload_policy` arg.

*class*torch.distributed.fsdp.CPUOffloadPolicy(*pin_memory=True*)

This offload policy offloads parameters, gradients, and optimizer states to
CPU. Sharded parameters are copied host-to-device before all-gather. The
all-gathered parameters are freed according to `reshard_after_forward`.
Sharded gradients are copied device-to-host in backward, and the optimizer
step runs on CPU with CPU optimizer states.

Variables:

**pin_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to pin sharded parameter and gradient
memory. Pinning memory allows both more efficient H2D/D2H copies
and for the copies to overlap with compute. However, the pinned
memory cannot be used by other processes. Set this to `False` if
you have insufficient CPU memory. (Default: `True`)

torch.distributed.fsdp.share_comm_ctx(*modules*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/distributed/fsdp/_fully_shard/_fully_shard.py#L965)

Share cuda streams for multiple FSDPModules

Example usage:

from torch.distributed.fsdp import share_comm_ctx
share_comm_ctx([fsdp_model_1, fsdp_model_2, ...])

For Pipeline Parallelism (PP), each model chunk is a FSDP root. We want
to share cuda streams for all-gather, reduce-scatter, and all-reduce.
This avoids allocating inter-stream memory framgmentation

Parameters:

**modules** (*List**[**FSDPModule**]*) - modules to share cuda streams

*class*torch.distributed.fsdp.DataParallelMeshDims(*shard=None*, *replicate=None*)

Specifies which dimensions of a full SPMD `DeviceMesh` correspond to
data parallelism when using `fully_shard()` whose parameters are already
DTensors on that mesh.

Variables:

- **shard** (*Optional**[**Union**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**...**]**]**]*) - Mesh dimension name(s)
that FSDP shards parameters on. If a tuple of names, those dims
are flattened into a single shard dimension. At least one of
`shard` and `replicate` must be set.
- **replicate** (*Optional**[**Union**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**...**]**]**]*) - Mesh dimension
name(s) for HSDP or DDP replication. If a tuple of names, those
dims are flattened into a single replicate dimension.