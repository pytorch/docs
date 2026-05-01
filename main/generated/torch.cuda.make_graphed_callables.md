# torch.cuda.make_graphed_callables

torch.cuda.make_graphed_callables(*callables: [Module](torch.nn.Module.html#torch.nn.Module) | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [object](https://docs.python.org/3/library/functions.html#object)]*, *sample_args: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...]*, *num_warmup_iters: [int](https://docs.python.org/3/library/functions.html#int) = 3*, *allow_unused_input: [bool](https://docs.python.org/3/library/functions.html#bool) = False*, *pool: _POOL_HANDLE | [None](https://docs.python.org/3/library/constants.html#None) = None*) → [Module](torch.nn.Module.html#torch.nn.Module) | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [object](https://docs.python.org/3/library/functions.html#object)][[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/cuda/graphs.py#L316)

torch.cuda.make_graphed_callables(*callables: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Module](torch.nn.Module.html#torch.nn.Module) | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [object](https://docs.python.org/3/library/functions.html#object)], ...]*, *sample_args: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...], ...]*, *num_warmup_iters: [int](https://docs.python.org/3/library/functions.html#int) = 3*, *allow_unused_input: [bool](https://docs.python.org/3/library/functions.html#bool) = False*, *pool: _POOL_HANDLE | [None](https://docs.python.org/3/library/constants.html#None) = None*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Module](torch.nn.Module.html#torch.nn.Module) | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [object](https://docs.python.org/3/library/functions.html#object)], ...]

Accept callables (functions or [`nn.Module`](torch.nn.Module.html#torch.nn.Module)s) and returns graphed versions.

Each graphed callable's forward pass runs its source callable's
forward CUDA work as a CUDA graph inside a single autograd node.

The graphed callable's forward pass also appends
a backward node to the autograd graph. During backward, this node runs the
callable's backward work as a CUDA graph.

Therefore, each graphed callable should be a drop-in replacement for its source callable
in an autograd-enabled training loop.

See [Partial-network capture](../notes/cuda.html#partial-network-capture) for detailed use and constraints.

If you pass a tuple of several callables, their captures will use the same memory pool.
See [Graph memory management](../notes/cuda.html#graph-memory-management) for when this is appropriate.

Parameters:

- **callables** ([*torch.nn.Module*](torch.nn.Module.html#torch.nn.Module)*or**Python function**, or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**these*) - Callable or callables to graph.
See [Graph memory management](../notes/cuda.html#graph-memory-management) for when passing a tuple of callables
is appropriate. If you pass a tuple of callables, their order in the tuple must be the same order
they'll run in the live workload.
- **sample_args** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**Tensors**, or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**tuples**of**Tensors*) - Samples args for each callable.
If a single callable was passed, `sample_args` must be a single tuple of argument Tensors.
If a tuple of callables was passed, `sample_args` must be tuple of tuples of argument Tensors.
- **num_warmup_iters** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The number of warmup iterations. Currently, `DataDistributedParallel` needs
11 iterations for warm up. Default: `3`.
- **allow_unused_input** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If False, specifying inputs that were not used when computing outputs
(and therefore their grad is always zero) is an error. Defaults to False.
- **pool** (*optional*) - Token (returned by [`graph_pool_handle()`](torch.cuda.graph_pool_handle.html#torch.cuda.graph_pool_handle) or
[`other_Graph_instance.pool()`](torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph.pool)) that hints this graph may share memory
with the indicated pool. See [Graph memory management](../notes/cuda.html#graph-memory-management).

Note

The `requires_grad` state of each Tensor in `sample_args` must match the state
that's expected for the corresponding real input in the training loop.

Warning

This API is in beta and may change in future releases.

Warning

`sample_args` for each callable must contain only Tensors. Other types are not allowed.

Warning

Returned callables do not support higher order differentiation (e.g., double backward).

Warning

In any [`Module`](torch.nn.Module.html#torch.nn.Module) passed to `make_graphed_callables()`, only parameters
may be trainable. Buffers must have `requires_grad=False`.

Warning

After you pass a [`torch.nn.Module`](torch.nn.Module.html#torch.nn.Module) through `make_graphed_callables()`,
you may not add or remove any of that Module's parameters or buffers.

Warning

[`torch.nn.Module`](torch.nn.Module.html#torch.nn.Module)s passed to `make_graphed_callables()` must not have module hooks
registered on them at the time they are passed. However, registering hooks on modules *after* passing them
through `make_graphed_callables()` is allowed.

Warning

When running a graphed callable, you must pass its arguments in the same order and format
they appeared in that callable's `sample_args`.

Warning

The automatic mixed precision is supported in `make_graphed_callables()` only with disabled
caching. The context manager torch.cuda.amp.autocast() must have cache_enabled=False.