# torch.utils.checkpoint

Note

Checkpointing is implemented by rerunning a forward-pass segment for
each checkpointed segment during backward propagation. This can cause persistent
states like the RNG state to be more advanced than they would without
checkpointing. By default, checkpointing includes logic to juggle
the RNG state such that checkpointed passes making use of RNG
(through dropout for example) have deterministic output as
compared to non-checkpointed passes. The logic to stash and restore
RNG states can incur a moderate performance hit depending on the runtime
of checkpointed operations. If deterministic output compared to
non-checkpointed passes is not required, supply `preserve_rng_state=False`
to `checkpoint` or `checkpoint_sequential` to omit stashing and
restoring the RNG state during each checkpoint.

The stashing logic saves and restores the RNG state for CPU and another
device type (infer the device type from Tensor arguments excluding CPU
tensors by `_infer_device_type`) to the `run_fn`. If there are multiple
devices, device state will only be saved for devices of a single device type,
and the remaining devices will be ignored. Consequently, if any checkpointed
functions involve randomness, this may result in incorrect gradients. (Note
that if CUDA devices are among the devices detected, it will be prioritized;
otherwise, the first device encountered will be selected.) If there are no
CPU-tensors, the default device type state (default value is `cuda`, and it
could be set to other device by `DefaultDeviceType`) will be saved and restored.
However, the logic has no way to anticipate if the user will move
Tensors to a new device within the `run_fn` itself. Therefore, if you move
Tensors to a new device ("new" meaning not belonging to the set of
[current device + devices of Tensor arguments]) within `run_fn`, deterministic
output compared to non-checkpointed passes is never guaranteed.

torch.utils.checkpoint.checkpoint(*function*, **args*, *use_reentrant=None*, *context_fn=<function noop_context_fn>*, *determinism_check='default'*, *debug=False*, *early_stop=True*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/utils/checkpoint.py#L354)

Checkpoint a model or part of the model.

Activation checkpointing is a technique that trades compute for memory.
By default, tensors computed during the forward pass are kept alive until
they are used in gradient computations in the backward pass. To reduce this
memory usage, tensors produced in the passed `function` are not kept
alive until the backward pass. Instead, any passed tensors in `args`
are kept alive, and the unsaved tensors are recomputed by re-invoking
`function` in the backward pass as needed for gradient computation.
Activation checkpointing can be applied to any part of a model - this is
sometimes described as "checkpointing" that part of the model.

There are currently two checkpointing implementations available, determined
by the `use_reentrant` parameter. It is recommended that you use
`use_reentrant=False`. Please refer the note below for a discussion of
their differences.

Warning

If the `function` invocation during the backward pass differs
from the forward pass, e.g., due to a global variable, the checkpointed
version may not be equivalent, potentially causing an
error being raised or leading to silently incorrect gradients.

Warning

The `use_reentrant` parameter should be passed explicitly. In version
2.9 we will raise an exception if `use_reentrant` is not passed.
If you are using the `use_reentrant=True` variant, please refer to the
note below for important considerations and potential limitations.

Note

The reentrant variant of checkpoint (`use_reentrant=True`) and
the non-reentrant variant of checkpoint (`use_reentrant=False`)
differ in the following ways:

- Non-reentrant checkpoint stops recomputation as soon as all needed
intermediate activations have been recomputed. This feature is enabled
by default, but can be disabled with `set_checkpoint_early_stop()`.
Reentrant checkpoint always recomputes `function` in its
entirety during the backward pass.
- The reentrant variant does not record the autograd graph during the
forward pass, as it runs with the forward pass under
[`torch.no_grad()`](generated/torch.no_grad.html#torch.no_grad). The non-reentrant version does record the
autograd graph, allowing one to perform backward on the graph within
checkpointed regions.
- The reentrant checkpoint only supports the
[`torch.autograd.backward()`](generated/torch.autograd.backward.html#torch.autograd.backward) API for the backward pass without its
inputs argument, while the non-reentrant version supports all ways
of performing the backward pass.
- At least one input and output must have `requires_grad=True` for the
reentrant variant. If this condition is unmet, the checkpointed part
of the model will not have gradients. The non-reentrant version does
not have this requirement.
- The reentrant version does not consider tensors in nested structures
(e.g., custom objects, lists, dicts, etc) as participating in
autograd, while the non-reentrant version does.
- The reentrant checkpoint does not support checkpointed regions with
detached tensors from the computational graph, whereas the
non-reentrant version does. For the reentrant variant, if the
checkpointed segment contains tensors detached using `detach()` or
with [`torch.no_grad()`](generated/torch.no_grad.html#torch.no_grad), the backward pass will raise an error.
This is because `checkpoint` makes all the outputs require gradients
and this causes issues when a tensor is defined to have no gradient in
the model. To avoid this, detach the tensors outside of the
`checkpoint` function.

Parameters:

- **function** - describes what to run in the forward pass of the model or
part of the model. It should also know how to handle the inputs
passed as the tuple. For example, in LSTM, if user passes
`(activation, hidden)`, `function` should correctly use the
first input as `activation` and the second input as `hidden`
- **args** - tuple containing inputs to the `function`

Keyword Arguments:

- **preserve_rng_state** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Omit stashing and restoring
the RNG state during each checkpoint. Note that under torch.compile,
this flag doesn't take effect and we always preserve RNG state.
Default: `True`
- **use_reentrant** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - specify whether to use the activation checkpoint variant that
requires reentrant autograd. This parameter should be passed
explicitly. In version 2.9 we will raise an exception if
`use_reentrant` is not passed. If `use_reentrant=False`,
`checkpoint` will use an implementation that does not require
reentrant autograd. This allows `checkpoint` to support additional
functionality, such as working as expected with
`torch.autograd.grad` and support for keyword arguments input into
the checkpointed function.
- **context_fn** (*Callable**,**optional*) - A callable returning a tuple of two
context managers. The function and its recomputation will be run
under the first and second context managers respectively.
This argument is only supported if `use_reentrant=False`.
- **determinism_check** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - A string specifying the determinism
check to perform. By default it is set to `"default"` which
compares the shapes, dtypes, and devices of the recomputed tensors
against those the saved tensors. To turn off this check, specify
`"none"`. Currently these are the only two supported values.
Please open an issue if you would like to see more determinism
checks. This argument is only supported if `use_reentrant=False`,
if `use_reentrant=True`, the determinism check is always disabled.
- **debug** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `True`, error messages will also include
a trace of the operators ran during the original forward computation
as well as the recomputation. This argument is only supported if
`use_reentrant=False`.
- **early_stop** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `True`, non-reentrant checkpoint stops
recomputation as soon as it has computed all needed Tensors. This
argument is ignored if `use_reentrant=True`. Can be overridden
globally using `set_checkpoint_early_stop()` context manager.
Default: `True`.

Returns:

Output of running `function` on `*args`

torch.utils.checkpoint.checkpoint_sequential(*functions*, *segments*, *input*, *use_reentrant=None*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/utils/checkpoint.py#L542)

Checkpoint a sequential model to save memory.

Sequential models execute a list of modules/functions in order
(sequentially). Therefore, we can divide such a model in various segments
and checkpoint each segment. All segments except the last will not store
the intermediate activations. The inputs of each checkpointed segment will
be saved for re-running the segment in the backward pass.

Warning

The `use_reentrant` parameter should be passed explicitly. In version
2.9 we will raise an exception if `use_reentrant` is not passed.
If you are using the use_reentrant=True` variant, please see
:func:`~torch.utils.checkpoint.checkpoint` for
the important considerations and limitations of this variant. It is
recommended that you use ``use_reentrant=False.

Parameters:

- **functions** - A [`torch.nn.Sequential`](generated/torch.nn.Sequential.html#torch.nn.Sequential) or the list of modules or
functions (comprising the model) to run sequentially.
- **segments** - Number of chunks to create in the model
- **input** - A Tensor that is input to `functions`
- **preserve_rng_state** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Omit stashing and restoring
the RNG state during each checkpoint.
Default: `True`
- **use_reentrant** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - specify whether to use the activation checkpoint variant that
requires reentrant autograd. This parameter should be passed
explicitly. In version 2.5 we will raise an exception if
`use_reentrant` is not passed. If `use_reentrant=False`,
`checkpoint` will use an implementation that does not require
reentrant autograd. This allows `checkpoint` to support additional
functionality, such as working as expected with
`torch.autograd.grad` and support for keyword arguments input into
the checkpointed function.

Returns:

Output of running `functions` sequentially on `*inputs`

Example

```
>>> model = nn.Sequential(...)
>>> input_var = checkpoint_sequential(model, chunks, input_var)
```

torch.utils.checkpoint.set_checkpoint_debug_enabled(*enabled*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/utils/checkpoint.py#L49)

Context manager that sets whether checkpoint should print additional debug
information when running. See the `debug` flag for
`checkpoint()` for more information. Note that
when set, this context manager overrides the value of `debug` passed to
checkpoint. To defer to the local setting, pass `None` to this context.

Parameters:

**enabled** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether checkpoint should print debug information.
Default is 'None'.

*class*torch.utils.checkpoint.CheckpointPolicy(*value*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/utils/checkpoint.py#L1290)

Enum for specifying the policy for checkpointing during backpropagation.

The following policies are supported:

- `{MUST,PREFER}_SAVE`: The operation's output will be saved during the forward
pass and will not be recomputed during the backward pass
- `{MUST,PREFER}_RECOMPUTE`: The operation's output will not be saved during the
forward pass and will be recomputed during the backward pass
- `{MUST,PREFER}_CPU_OFFLOAD`: The operation's output will be saved during the
forward pass, offloaded to CPU, and reloaded to GPU during the backward pass

Use `MUST_*` over `PREFER_*` to indicate that the policy should not be overridden
by other subsystems like torch.compile.

Note

A policy function that always returns `PREFER_RECOMPUTE` is
equivalent to vanilla checkpointing.

A policy function that returns `PREFER_SAVE` every op is
NOT equivalent to not using checkpointing. Using such a policy would
save additional tensors not limited to ones that are actually needed for
gradient computation.

*class*torch.utils.checkpoint.SelectiveCheckpointContext(***, *is_recompute*, *op_output=None*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/utils/checkpoint.py#L1260)

Context passed to policy function during selective checkpointing.

This class is used to pass relevant metadata to the policy function during
selective checkpointing.

The policy function is only called during the forward pass. During
recomputation, cached values are retrieved by index, so `is_recompute`
is deprecated and always `False`.

Example

```
>>>
>>> def policy_fn(ctx, op, *args, **kwargs):
>>> print(ctx.op_output)
>>>
>>> context_fn = functools.partial(create_selective_checkpoint_contexts, policy_fn)
>>>
>>> out = torch.utils.checkpoint.checkpoint(
>>> fn, x, y,
>>> use_reentrant=False,
>>> context_fn=context_fn,
>>> )
```

torch.utils.checkpoint.create_selective_checkpoint_contexts(*policy_fn_or_list*, *allow_cache_entry_mutation=False*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/utils/checkpoint.py#L1470)

Helper to avoid recomputing certain ops during activation checkpointing.

Use this with torch.utils.checkpoint.checkpoint to control which
operations are recomputed during the backward pass.

Parameters:

- **policy_fn_or_list** (*Callable**or**List*) -

- If a policy function is provided, it should accept a
`SelectiveCheckpointContext`, the `OpOverload`, args and
kwargs to the op, and return a `CheckpointPolicy` enum value
indicating whether the execution of the op should be recomputed or not.
- If a list of operations is provided, it is equivalent to a policy
returning CheckpointPolicy.MUST_SAVE for the specified
operations and CheckpointPolicy.PREFER_RECOMPUTE for all other
operations.
- **allow_cache_entry_mutation** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - By default, an error is
raised if any tensors cached by selective activation checkpoint are
mutated in order to ensure correctness. If set to True, this check
is disabled.

Returns:

A tuple of two context managers.

Example

```
>>> import functools
>>>
>>> x = torch.rand(10, 10, requires_grad=True)
>>> y = torch.rand(10, 10, requires_grad=True)
>>>
>>> ops_to_save = [
>>> torch.ops.aten.mm.default,
>>> ]
>>>
>>> def policy_fn(ctx, op, *args, **kwargs):
>>> if op in ops_to_save:
>>> return CheckpointPolicy.MUST_SAVE
>>> else:
>>> return CheckpointPolicy.PREFER_RECOMPUTE
>>>
>>> context_fn = functools.partial(create_selective_checkpoint_contexts, policy_fn)
>>>
>>> # or equivalently
>>> context_fn = functools.partial(create_selective_checkpoint_contexts, ops_to_save)
>>>
>>> def fn(x, y):
>>> return torch.sigmoid(torch.matmul(torch.matmul(x, y), y)) * y
>>>
>>> out = torch.utils.checkpoint.checkpoint(
>>> fn, x, y,
>>> use_reentrant=False,
>>> context_fn=context_fn,
>>> )
```

*class*torch.utils.checkpoint.GraphExecGroup[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/utils/checkpoint.py#L1732)

Any checkpointed regions encountered by backward under the same instance
of this context manager will trigger recompute at most once, even if
there are multiple calls to backward.

Backward calls under the same instance of this context manager must execute
over non-overlapping regions of the backward graph even if retain_graph=True.
In particular, any two backward call cannot use the same saved activation for
gradient computation.

Note

This context manager only affects checkpoint with use_reentrant=False, and
is a no-op otherwise.

torch.utils.checkpoint.set_checkpoint_early_stop(*enable*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/utils/checkpoint.py#L776)

Controls whether checkpoint should stop recomputation early.

By default, non-reentrant checkpoint stops recomputation as soon as it
has computed all needed Tensors. This context manager can be used to disable
that feature if it is problematic for your specific application.

This context manager only needs to be active when forward is run. It does
not need to be active during backward.

Example:

```
>>> message = "saved tensors default hooks are disabled"
>>> with set_checkpoint_early_stop(False):
... # Any checkpoint under this context manager will respect this
... # context manager, even if its backward is performed outside.
... out = checkpoint(fn, inputs)
...
>>> out.backward()
```

torch.utils.checkpoint.set_device_states(*devices*, *states*, ***, *device_type=None*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/utils/checkpoint.py#L195)

Sets random number generator states for the specified devices.

Parameters:

- **devices** - Device ids to set states for.
- **states** - States to set.
- **device_type** - `device_type` of the devices to set states for. Default
is the device returned by a call to `DefaultDeviceType.get_device_type()`,
which is `cuda` if not changed by calling `DefaultDeviceType::set_device_type()`.