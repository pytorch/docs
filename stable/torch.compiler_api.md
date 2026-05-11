# torch.compiler API reference

For a quick overview of `torch.compiler`, see [torch.compiler](user_guide/torch_compiler/torch.compiler.html#torch-compiler-overview).

| [`compile`](generated/torch.compiler.compile.html#torch.compiler.compile) | See [`torch.compile()`](generated/torch.compile.html#torch.compile) for details on the arguments for this function. |
| --- | --- |
| [`reset`](generated/torch.compiler.reset.html#torch.compiler.reset) | This function clears all compilation caches and restores the system to its initial state. |
| [`allow_in_graph`](generated/torch.compiler.allow_in_graph.html#torch.compiler.allow_in_graph) | Tells the compiler frontend (Dynamo) to skip symbolic introspection of the function and instead directly write it to the graph when encountered. |
| [`substitute_in_graph`](generated/torch.compiler.substitute_in_graph.html#torch.compiler.substitute_in_graph) | Register a polyfill handler for a function, usually a C function from the C extension, to be used in place of the original function when inlining the original function in the graph. |
| [`assume_constant_result`](generated/torch.compiler.assume_constant_result.html#torch.compiler.assume_constant_result) | This function is used to mark a function fn as having a constant result. |
| [`list_backends`](generated/torch.compiler.list_backends.html#torch.compiler.list_backends) | Return valid strings that can be passed to torch.compile(..., backend="name"). |
| [`disable`](generated/torch.compiler.disable.html#torch.compiler.disable) | This function provides a decorator to disable compilation on a function. |
| [`set_stance`](generated/torch.compiler.set_stance.html#torch.compiler.set_stance) | Set the current stance of the compiler. |
| [`set_enable_guard_collectives`](generated/torch.compiler.set_enable_guard_collectives.html#torch.compiler.set_enable_guard_collectives) | Enables use of collectives *during* guard evaluation to synchronize behavior across ranks. |
| [`cudagraph_mark_step_begin`](generated/torch.compiler.cudagraph_mark_step_begin.html#torch.compiler.cudagraph_mark_step_begin) | Indicates that a new iteration of inference or training is about to begin. |
| [`is_compiling`](generated/torch.compiler.is_compiling.html#torch.compiler.is_compiling) | Indicates whether a graph is executed/traced as part of torch.compile() or torch.export(). |
| [`is_dynamo_compiling`](generated/torch.compiler.is_dynamo_compiling.html#torch.compiler.is_dynamo_compiling) | Indicates whether a graph is traced via TorchDynamo. |
| [`is_exporting`](generated/torch.compiler.is_exporting.html#torch.compiler.is_exporting) | Indicated whether we're under exporting. |
| [`keep_portable_guards_unsafe`](generated/torch.compiler.keep_portable_guards_unsafe.html#torch.compiler.keep_portable_guards_unsafe) | A common function to only keep guards that can be used in both Python and non-Python environments. |
| [`skip_guard_on_inbuilt_nn_modules_unsafe`](generated/torch.compiler.skip_guard_on_inbuilt_nn_modules_unsafe.html#torch.compiler.skip_guard_on_inbuilt_nn_modules_unsafe) | A common function to skip guards on the inbuilt nn modules like torch.nn.Linear. |
| [`skip_guard_on_all_nn_modules_unsafe`](generated/torch.compiler.skip_guard_on_all_nn_modules_unsafe.html#torch.compiler.skip_guard_on_all_nn_modules_unsafe) | A common function to skip guards on all nn modules, both user defined as well inbuilt nn modules (like torch.nn.Linear). |
| [`keep_tensor_guards_unsafe`](generated/torch.compiler.keep_tensor_guards_unsafe.html#torch.compiler.keep_tensor_guards_unsafe) | A common function to keep tensor guards on all tensors. |
| [`skip_guard_on_globals_unsafe`](generated/torch.compiler.skip_guard_on_globals_unsafe.html#torch.compiler.skip_guard_on_globals_unsafe) | A common function to skip guards on all globals. |
| [`skip_all_guards_unsafe`](generated/torch.compiler.skip_all_guards_unsafe.html#torch.compiler.skip_all_guards_unsafe) | A function for skipping all guards on a compiled function. |
| [`nested_compile_region`](generated/torch.compiler.nested_compile_region.html#torch.compiler.nested_compile_region) | Tells **``torch.compile``** that the marked set of operations forms a nested compile region (which is often repeated in the full model) whose code can be compiled once and safely reused. |