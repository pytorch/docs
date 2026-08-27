# torch.compile

torch.compile(*model: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[_InputT], _RetT]*, ***, *fullgraph: [bool](https://docs.python.org/3/library/functions.html#bool) = False*, *dynamic: [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *backend: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [Any](https://docs.python.org/3/library/typing.html#typing.Any)] = 'inductor'*, *mode: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *options: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [int](https://docs.python.org/3/library/functions.html#int) | [bool](https://docs.python.org/3/library/functions.html#bool) | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [Any](https://docs.python.org/3/library/typing.html#typing.Any)]] | [None](https://docs.python.org/3/library/constants.html#None) = None*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *disable: [bool](https://docs.python.org/3/library/functions.html#bool) = False*, *dynamic_shapes: [Any](https://docs.python.org/3/library/typing.html#typing.Any) = None*) → [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[_InputT], _RetT][[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/__init__.py#L3052)

torch.compile(*model: [None](https://docs.python.org/3/library/constants.html#None) = None*, ***, *fullgraph: [bool](https://docs.python.org/3/library/functions.html#bool) = False*, *dynamic: [bool](https://docs.python.org/3/library/functions.html#bool) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *backend: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [Any](https://docs.python.org/3/library/typing.html#typing.Any)] = 'inductor'*, *mode: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *options: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [int](https://docs.python.org/3/library/functions.html#int) | [bool](https://docs.python.org/3/library/functions.html#bool) | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [Any](https://docs.python.org/3/library/typing.html#typing.Any)]] | [None](https://docs.python.org/3/library/constants.html#None) = None*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *disable: [bool](https://docs.python.org/3/library/functions.html#bool) = False*, *dynamic_shapes: [Any](https://docs.python.org/3/library/typing.html#typing.Any) = None*) → [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[_InputT], _RetT]], [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[_InputT], _RetT]]

Optimizes given model/function using TorchDynamo and specified backend.
If you are compiling an [`torch.nn.Module`](torch.nn.Module.html#torch.nn.Module), you can also use [`torch.nn.Module.compile()`](torch.nn.Module.html#torch.nn.Module.compile)
to compile the module inplace without changing its structure.

Concretely, for every frame executed within the compiled region, we will attempt
to compile it and cache the compiled result on the code object for future
use. A single frame may be compiled multiple times if previous compiled
results are not applicable for subsequent calls (this is called a "guard
failure"), you can use TORCH_LOGS=guards to debug these situations.
Multiple compiled results can be associated with a frame up to
`torch._dynamo.config.recompile_limit`, which defaults to 8; at which
point we will fall back to eager. Note that compile caches are per
*code object*, not frame; if you dynamically create multiple copies of a
function, they will all share the same code cache.

Parameters:

- **model** (*Callable**or**None*) - Module/function to optimize
- **fullgraph** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If False (default), torch.compile attempts to discover compilable regions
in the function that it will optimize. If True, then we require that the entire function be
capturable into a single graph. If this is not possible (that is, if there are graph breaks),
then this will raise an error. This also opts into unbacked semantics, notably it will turn on
capture_scalar_outputs and capture_dynamic_output_shape_ops on by default.
- **dynamic** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*or**None*) - Use dynamic shape tracing. When this is True, we will up-front attempt
to generate a kernel that is as dynamic as possible to avoid recompilations when
sizes change. This may not always work as some operations/optimizations will
force specialization; use TORCH_LOGS=dynamic to debug overspecialization.
When this is False, we will NEVER generate dynamic kernels, we will always specialize.
By default (None), we automatically detect if dynamism has occurred and compile a more
dynamic kernel upon recompile.
- **backend** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*or**Callable*) -

backend to be used

- "inductor" is the default backend, which is a good balance between performance and overhead
- Non experimental in-tree backends can be seen with torch._dynamo.list_backends()
- Experimental or debug in-tree backends can be seen with torch._dynamo.list_backends(None)
- To register an out-of-tree custom backend:
[https://docs.pytorch.org/docs/main/user_guide/torch_compiler/torch.compiler_custom_backends.html#registering-custom-backends](https://docs.pytorch.org/docs/main/user_guide/torch_compiler/torch.compiler_custom_backends.html#registering-custom-backends)
- **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) -

Can be either "default", "reduce-overhead", "max-autotune" or "max-autotune-no-cudagraphs"

- "default" is the default mode, which is a good balance between performance and overhead
- "reduce-overhead" is a mode that reduces the overhead of python with CUDA graphs,
useful for small batches. Reduction of overhead can come at the cost of more memory
usage, as we will cache the workspace memory required for the invocation so that we
do not have to reallocate it on subsequent runs. Reduction of overhead is not guaranteed
to work; today, we only reduce overhead for CUDA only graphs which do not mutate inputs.
There are other circumstances where CUDA graphs are not applicable; use TORCH_LOGS=perf_hints
to debug.
- "max-autotune" is a mode that leverages Triton or template based matrix multiplications
on supported devices and Triton based convolutions on GPU.
It enables CUDA graphs by default on GPU.
- "max-autotune-no-cudagraphs" is a mode similar to "max-autotune" but without CUDA graphs
- To see the exact configs that each mode sets you can call torch._inductor.list_mode_options()
- **options** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) -

A dictionary of options to pass to the backend. Some notable ones to try out are

- epilogue_fusion which fuses pointwise ops into templates. Requires max_autotune to also be set
- max_autotune which will profile to pick the best matmul configuration
- fallback_random which is useful when debugging accuracy issues
- shape_padding which pads matrix shapes to better align loads on GPUs especially for tensor cores
- triton.cudagraphs which will reduce the overhead of python with CUDA graphs
- trace.enabled which is the most useful debugging flag to turn on
- trace.graph_diagram which will show you a picture of your graph after fusion
- guard_filter_fn that controls which dynamo guards are saved with compilations.
This is an unsafe feature and there is no backward compatibility guarantee provided
for dynamo guards as data types.
For stable helper functions to use, see the documentation in torch.compiler, for example:
- torch.compiler.skip_guard_on_inbuilt_nn_modules_unsafe
- torch.compiler.skip_guard_on_all_nn_modules_unsafe
- torch.compiler.keep_tensor_guards_unsafe
- For inductor you can see the full list of configs that it supports by calling torch._inductor.list_options()
- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*or**None*) - Optional identifier for the compiled region. When supported by downstream
tooling, this is surfaced on wrapped compiled-region higher-order operators and other debug metadata.
- **disable** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Turn torch.compile() into a no-op for testing
- **recompile_limit** ([*int*](https://docs.python.org/3/library/functions.html#int)*or**None*) - Maximum number of recompilations allowed for this
`torch.compile()` call before falling back to eager. If None (default), uses
the global `torch._dynamo.config.recompile_limit` (default 8). With
`fullgraph=True`, exceeding the limit raises `FailOnRecompileLimitHit`.
- **isolate_recompiles** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If True, this `torch.compile()` call tracks
recompilations independently. By default, all `torch.compile()` calls on the
same function share a single set of compiled entries, so one call's
recompilations count against every other call's limit. With
`isolate_recompiles=True`, each call gets its own isolated set of entries.
Lookups for an isolated compile call will still fall back to entries from
non-isolated compile calls (BC-friendly reuse), but new compilations are
stored separately. `recompile_limit` is checked per-region;
`accumulated_recompile_limit` is a global cap across all regions.
Default-strategy behavior is asymmetric: SKIP decisions (from
`skip_code`, `@torch._dynamo.skip`, FX-generated code, etc.) are
inherited by isolated regions -- those remain skipped. RUN_ONLY persisted
by a non-isolated region hitting its recompile limit does NOT bleed
into isolated regions -- each region manages its own RUN_ONLY state.
Default False.

Example:

```
@torch.compile(options={"triton.cudagraphs": True}, fullgraph=True)
def foo(x):
 return torch.sin(x) + torch.cos(x)
```