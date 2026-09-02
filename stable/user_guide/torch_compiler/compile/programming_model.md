# torch.compile Programming Model

The `torch.compile` programming model:

1. Clarifies some internal behaviors of `torch.compile` so that one can better predict compiler behavior on user code and
2. Provides ways for one to take more fine-grained control over `torch.compile`.

By understanding the `torch.compile` programming model, one can systematically unblock themselves when encountering issues with `torch.compile`.

- [Dynamo Core Concepts](programming_model.dynamo_core_concepts.html)

- [Dynamo Tracing](programming_model.dynamo_core_concepts.html#dynamo-tracing)
- [Graph Breaks](programming_model.dynamo_core_concepts.html#graph-breaks)
- [Guards](programming_model.dynamo_core_concepts.html#guards)
- [Recompilations](programming_model.dynamo_core_concepts.html#recompilations)
- [Dynamic Shapes](programming_model.dynamo_core_concepts.html#dynamic-shapes)
- [Working with Graph Breaks](programming_model.graph_breaks_index.html)

- [Use `fullgraph=True` to Identify and Eliminate Graph Breaks](programming_model.fullgraph_true.html)

- [Strategy 1: Rewrite the unsupported code to use features supported by Dynamo](programming_model.fullgraph_true.html#strategy-1-rewrite-the-unsupported-code-to-use-features-supported-by-dynamo)
- [Strategy 2: Pure functions can always be compiled via an escape hatch.](programming_model.fullgraph_true.html#strategy-2-pure-functions-can-always-be-compiled-via-an-escape-hatch)
- [Strategy 3: Don't compile the code](programming_model.fullgraph_true.html#strategy-3-don-t-compile-the-code)
- [Common Graph Breaks](programming_model.common_graph_breaks.html)

- [Incorrect Code](programming_model.common_graph_breaks.html#incorrect-code)
- [Data-dependent operations](programming_model.common_graph_breaks.html#data-dependent-operations)
- [Printing and logging](programming_model.common_graph_breaks.html#printing-and-logging)
- [Use `torch._dynamo.nonstrict_trace`](programming_model.dynamo_nonstrict_trace.html)
- [Custom Operators](programming_model.custom_ops.html)
- [Working with `fullgraph=False`](programming_model.fullgraph_false.html)

- [Where to apply torch.compile?](programming_model.where_to_apply_compile.html)

- [`compile(model)` vs `model.compile()`](programming_model.where_to_apply_compile.html#compile-model-vs-model-compile)
- [Disabling and Suppressing Errors](programming_model.compiler_disable.html)
- [Toggling `error_on_graph_break`](programming_model.error_on_graph_break.html)

- [`error_on_graph_break(False)` example](programming_model.error_on_graph_break.html#error-on-graph-break-false-example)
- [`error_on_graph_break(True)` example](programming_model.error_on_graph_break.html#error-on-graph-break-true-example)
- [`error_on_graph_break` nesting behavior](programming_model.error_on_graph_break.html#error-on-graph-break-nesting-behavior)
- [Interaction with `fullgraph`](programming_model.error_on_graph_break.html#interaction-with-fullgraph)
- [Summary of `fullgraph=True/False` vs `error_on_graph_break`](programming_model.error_on_graph_break.html#summary-of-fullgraph-true-false-vs-error-on-graph-break)
- [Nested Graph Breaks](programming_model.nested_graph_breaks.html)
- [Skipped Functions](programming_model.skipped_functions.html)

- [Graph Break in a Loop](programming_model.skipped_functions.html#graph-break-in-a-loop)
- [Graph Break in a Context Manager](programming_model.skipped_functions.html#graph-break-in-a-context-manager)
- [Graph Break in a Try Block](programming_model.skipped_functions.html#graph-break-in-a-try-block)
- [Hitting a Recompilation Limit](programming_model.skipped_functions.html#hitting-a-recompilation-limit)
- [Compiler Errors](programming_model.skipped_functions.html#compiler-errors)
- [Dealing with Skipped Functions](programming_model.skipped_functions.html#dealing-with-skipped-functions)
- [Non-strict Tracing Programming Model](programming_model.non_strict_tracing_model.html)

- [Pure Functions](programming_model.non_strict_tracing_model.html#pure-functions)

- [Example 1: No explicit input (e.g. accesses global tensor)](programming_model.non_strict_tracing_model.html#example-1-no-explicit-input-e-g-accesses-global-tensor)
- [Example 2: Side effect (printing)](programming_model.non_strict_tracing_model.html#example-2-side-effect-printing)
- [Example 3: Side effect (input list mutation)](programming_model.non_strict_tracing_model.html#example-3-side-effect-input-list-mutation)
- [No direct data_ptr manipulation](programming_model.non_strict_tracing_model.html#no-direct-data-ptr-manipulation)
- [Specialization and Constants](programming_model.non_strict_tracing_model.html#specialization-and-constants)
- [Dealing with Recompilations](programming_model.recompilation.html)

- [Is Dynamic Shapes Enabled?](programming_model.recompilation.html#is-dynamic-shapes-enabled)
- [Wrapping Constants with Tensors](programming_model.recompilation.html#wrapping-constants-with-tensors)
- [Unspecializing Integer Attributes on `nn.Module`s](programming_model.recompilation.html#unspecializing-integer-attributes-on-nn-modules)
- [Changing the Cache Size Limit](programming_model.recompilation.html#changing-the-cache-size-limit)
- [Graph Breaking to Reduce Recompilation Costs](programming_model.recompilation.html#graph-breaking-to-reduce-recompilation-costs)
- [Reducing Compile Time](programming_model.reducing_compile_time.html)

- [Avoid unnecessary recompilations](programming_model.reducing_compile_time.html#avoid-unnecessary-recompilations)
- [Use dynamic shapes to avoid shape-driven recompiles](programming_model.reducing_compile_time.html#use-dynamic-shapes-to-avoid-shape-driven-recompiles)
- [Regional compilation](programming_model.reducing_compile_time.html#regional-compilation)
- [Hierarchical compilation with `nested_compile_region`](programming_model.reducing_compile_time.html#hierarchical-compilation-with-nested-compile-region)
- [Measuring compile time](programming_model.reducing_compile_time.html#measuring-compile-time)
- [Reducing Guard Overhead](programming_model.reducing_guard_overhead.html)

- [1. Reduce pre-graph bytecode time with `install_free_tensors`](programming_model.reducing_guard_overhead.html#reduce-pre-graph-bytecode-time-with-install-free-tensors)
- [2. Skip guards on `nn.Module`s with `guard_filter_fn`](programming_model.reducing_guard_overhead.html#skip-guards-on-nn-modules-with-guard-filter-fn)
- [3. Try `use_recursive_dict_tags_for_guards` first](programming_model.reducing_guard_overhead.html#try-use-recursive-dict-tags-for-guards-first)
- [4. Skip guard evaluation after warmup with `skip_guard_eval_unsafe`](programming_model.reducing_guard_overhead.html#skip-guard-evaluation-after-warmup-with-skip-guard-eval-unsafe)
- [Putting it together](programming_model.reducing_guard_overhead.html#putting-it-together)
- [Further reading](programming_model.reducing_guard_overhead.html#further-reading)
- [tlparse / TORCH_TRACE](programming_model.observability.html)

- [TORCH_LOGS](programming_model.observability.html#torch-logs)
- [tlparse vs. TORCH_LOGS](programming_model.observability.html#tlparse-vs-torch-logs)
- [Reporting Issues](programming_model.reporting_issues.html)

- [Ablation](programming_model.reporting_issues.html#ablation)
- [Bisecting](programming_model.reporting_issues.html#bisecting)
- [Creating a reproducer](programming_model.reporting_issues.html#creating-a-reproducer)