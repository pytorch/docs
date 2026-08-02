# torch.compiler API reference

For a quick overview of `torch.compiler`, see [torch.compiler](user_guide/torch_compiler/torch.compiler.html#torch-compiler-overview).

| [`compile`](generated/torch.compiler.compile.html#torch.compiler.compile) | See [`torch.compile()`](generated/torch.compile.html#torch.compile) for details on the arguments for this function. |
| --- | --- |
| [`reset`](generated/torch.compiler.reset.html#torch.compiler.reset) | Reset the in-process compiler state. |
| [`nonstrict_trace`](generated/torch.compiler.nonstrict_trace.html#torch.compiler.nonstrict_trace) | Decorator to mark a function as nonstrict-traceable for dynamo. |
| [`allow_in_graph`](generated/torch.compiler.allow_in_graph.html#torch.compiler.allow_in_graph) | Tells the compiler frontend (Dynamo) to skip symbolic introspection of the function and instead directly write it to the graph when encountered. |
| [`substitute_in_graph`](generated/torch.compiler.substitute_in_graph.html#torch.compiler.substitute_in_graph) | Register a polyfill handler for a function, usually a C function from the C extension, to be used in place of the original function when inlining the original function in the graph. |
| [`assume_constant_result`](generated/torch.compiler.assume_constant_result.html#torch.compiler.assume_constant_result) | This function is used to mark a function fn as having a constant result. |
| [`list_backends`](generated/torch.compiler.list_backends.html#torch.compiler.list_backends) | Return valid strings that can be passed to torch.compile(..., backend="name"). |
| [`disable`](generated/torch.compiler.disable.html#torch.compiler.disable) | This function provides a decorator to disable compilation on a function. |
| [`set_default_backend`](generated/torch.compiler.set_default_backend.html#torch.compiler.set_default_backend) | Set the default backend for `torch.compile` when no `backend` argument is specified. |
| [`get_default_backend`](generated/torch.compiler.get_default_backend.html#torch.compiler.get_default_backend) | Return the current default backend for `torch.compile`. |
| [`set_stance`](generated/torch.compiler.set_stance.html#torch.compiler.set_stance) | Set the current stance of the compiler. |
| [`set_enable_guard_collectives`](generated/torch.compiler.set_enable_guard_collectives.html#torch.compiler.set_enable_guard_collectives) | Enables use of collectives *during* guard evaluation to synchronize behavior across ranks. |
| [`cudagraph_mark_step_begin`](generated/torch.compiler.cudagraph_mark_step_begin.html#torch.compiler.cudagraph_mark_step_begin) | Indicates that a new iteration of inference or training is about to begin. |
| [`cudagraph_mark_warmup_incomplete`](generated/torch.compiler.cudagraph_mark_warmup_incomplete.html#torch.compiler.cudagraph_mark_warmup_incomplete) | Request another warmup for the active CUDA Graph Trees function. |
| [`is_compiling`](generated/torch.compiler.is_compiling.html#torch.compiler.is_compiling) | Indicates whether a graph is executed/traced as part of torch.compile() or torch.export(). |
| [`is_dynamo_compiling`](generated/torch.compiler.is_dynamo_compiling.html#torch.compiler.is_dynamo_compiling) | Indicates whether a graph is traced via TorchDynamo. |
| [`is_exporting`](generated/torch.compiler.is_exporting.html#torch.compiler.is_exporting) | Indicates whether we're under exporting. |
| [`keep_portable_guards_unsafe`](generated/torch.compiler.keep_portable_guards_unsafe.html#torch.compiler.keep_portable_guards_unsafe) | A common function to only keep guards that can be used in both Python and non-Python environments. |
| [`skip_guard_on_inbuilt_nn_modules_unsafe`](generated/torch.compiler.skip_guard_on_inbuilt_nn_modules_unsafe.html#torch.compiler.skip_guard_on_inbuilt_nn_modules_unsafe) | A common function to skip guards on the inbuilt nn modules like torch.nn.Linear. |
| [`skip_guard_on_all_nn_modules_unsafe`](generated/torch.compiler.skip_guard_on_all_nn_modules_unsafe.html#torch.compiler.skip_guard_on_all_nn_modules_unsafe) | A common function to skip guards on all nn modules, both user defined as well inbuilt nn modules (like torch.nn.Linear). |
| [`keep_tensor_guards_unsafe`](generated/torch.compiler.keep_tensor_guards_unsafe.html#torch.compiler.keep_tensor_guards_unsafe) | A common function to keep tensor guards on all tensors. |
| [`skip_guard_on_globals_unsafe`](generated/torch.compiler.skip_guard_on_globals_unsafe.html#torch.compiler.skip_guard_on_globals_unsafe) | A common function to skip guards on all globals. |
| [`skip_all_guards_unsafe`](generated/torch.compiler.skip_all_guards_unsafe.html#torch.compiler.skip_all_guards_unsafe) | A function for skipping all guards on a compiled function. |
| [`nested_compile_region`](generated/torch.compiler.nested_compile_region.html#torch.compiler.nested_compile_region) | Tells **``torch.compile``** that the marked set of operations forms a nested compile region (which is often repeated in the full model) whose code can be compiled once and safely reused. |
| [`load_cache_artifacts`](generated/torch.compiler.load_cache_artifacts.html#torch.compiler.load_cache_artifacts) | Hot loads cache artifacts that were previously serialized via save_cache_artifacts |
| [`load_compiled_function`](generated/torch.compiler.load_compiled_function.html#torch.compiler.load_compiled_function) | Load an aot-compiled function from a file. |
| [`save_cache_artifacts`](generated/torch.compiler.save_cache_artifacts.html#torch.compiler.save_cache_artifacts) | Serializes all the cache artifacts that were created during the compilation |
| [`wrap_numpy`](generated/torch.compiler.wrap_numpy.html#torch.compiler.wrap_numpy) | Decorator that turns a function from `np.ndarray`s to `np.ndarray`s into a function from `torch.Tensor`s to `torch.Tensor`s. |

## torch.compiler.precompile

torch.compiler.precompile(*fn*, **example_inputs*, *backend='inductor'*, *tracer='make_fx'*, *decompositions=None*)

Ahead-of-time precompile `fn` against example inputs, returning a self-contained,
runnable Python source string plus an acceleration cache as `(python_code, cache)`.
`fn` is the whole computation, taking the model(s) as
explicit arguments, e.g. `lambda model, x: model(x)` or a training step. The
`nn.Module` arguments have their parameters/buffers lifted to graph inputs, so no
weights are baked into the artifact - you pass the model again at runtime to the
reloaded callable. Reload with `torch.compiler.precompile.load` (below).

Note

With the default `make_fx` tracer, capture is non-strict. Control flow is
specialized to the example inputs, and shapes are static - each size is baked in.
The exception is a tensor dim explicitly marked unbacked (inductor backend only)
with `torch._dynamo.decorators.mark_unbacked` on the inputs before the call; such
a dim is captured as an unbacked symint, so one artifact serves any runtime size of
it, and a graph that needs to guard on it fails at capture. Each input's dtype and
device are specialized too (a runtime mismatch is rejected), and the inductor backend
additionally specializes on input memory format. See Note [precompile programming
model] in `torch/_precompile.py`. `torch.compiler.precompile` is distinct from
`torch._dynamo.config.caching_precompile` (a `torch.compile` caching mode).

If `fn` runs a backward, the artifact re-runs the whole forward and backward and
scatters the resulting parameter gradients onto the runtime model's `parameters()`
`.grad` fields, accumulating (`p.grad += g`) exactly like eager `.backward()` -
so keep your usual `zero_grad()` / `optimizer.step()` loop. Which params receive a
grad is fixed at capture time (frozen or non-contributing params stay `.grad = None`).
The artifact returns `fn`'s own result (`None` for a bare `.backward()` step), not
the gradients.

Parameters:

- **fn** - The whole computation to capture, taking the model(s) and runtime inputs
as positional arguments.
- **example_inputs** - Example positional arguments to `fn`; the `nn.Module`
arguments are lifted and the rest are the runtime inputs.
- **backend** - `"inductor"` (default) lowers through AOTAutograd + Inductor;
`"eager"` keeps the captured ATen graph (layout-flexible, no kernels; shapes
are still specialized to the example).
- **tracer** - capture front-end. `"make_fx"` (default) is a non-strict make_fx
trace and the only tracer implemented today; `"dynamo"` is planned and raises
`NotImplementedError` for now.
- **decompositions** - Optional decomposition table (`dict` of `OpOverload` to a
decomposition function) forwarded to `make_fx`; defaults to `None`.

Returns:

`(python_code, cache)` - a self-contained Python source string (the
single source of truth for the calling convention) and a binary acceleration
cache (no weights, no calling-convention metadata; it carries a small
format/version/backend/code_hash integrity tag that `load` verifies).

Raises:

**PrecompileError** - if capture, lowering, or a runtime call violates the
contract (see the exception below).

Example:

```
python_code, cache = torch.compiler.precompile(lambda m, x: m(x), model, x)
f = torch.compiler.precompile.load(python_code, cache)
out = f(model, x) # pass the model again at runtime
```

precompile.load(*python_code*, *cache*)[[source]](https://github.com/pytorch/pytorch/blob/30731ee8f01763cf1d32dc2e3962f51fc034c482/torch/_precompile.py#L1742)

Reconstruct a runnable from the `(python_code, cache)` pair returned by
`precompile`. The calling convention is read from `python_code` (the single
source of truth); `cache` only accelerates loading - it carries only the compiled
backend artifact (the Inductor bundle for `backend="inductor"`; empty for
`backend="eager"`) and no weights. You pass the model(s) again at runtime.

Warning

`load` runs the artifact as code: it executes `python_code` (via `exec`) and,
for the inductor backend, primes the kernel caches from the `cache`. Treat
`(python_code, cache)` as trusted, executable input - only load a pair you
produced yourself or otherwise trust, exactly as you would any code you are about to
run (see Note [precompile programming model], invariant 7). `load` also emits a
per-call warning before it runs.

Parameters:

- **python_code** - The self-contained Python source string returned by `precompile`.
- **cache** - The binary acceleration cache returned by `precompile`.

Returns:

A runnable callable with the same calling convention as the captured `fn`.
Arguments are matched positionally at both capture and load time; keyword-argument
calling conventions are not supported.

Raises:

**PrecompileError** - if `python_code` is not a valid precompile artifact (it
fails to parse or is missing its calling-convention metadata), if `cache` is
paired with a different `python_code` (mismatched `backend` tag or
`code_hash`), or if a runtime call violates the precompile contract.

*exception*torch.compiler.PrecompileError

The error type raised by `torch.compiler.precompile` and its artifacts.

Raised when capture, lowering, `load`, or a runtime call violates the precompile
contract - e.g. a tensor baked as a constant (invariant 1), an unsupported /
effectful op, a non-tensor output the inductor backend cannot lower, or a runtime
input whose shape or memory format differs from the example (invariants 3 and 6).
See Note [precompile programming model] in this module for the full contract.