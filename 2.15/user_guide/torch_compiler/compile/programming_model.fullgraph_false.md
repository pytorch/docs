# Working with `fullgraph=False`

While `fullgraph=False` is the default `torch.compile` setting, the semantics of resuming compilation upon encountering a graph break are more complicated.
You can find details on the `fullgraph=False` semantics in the subsections.

The strategy for using `torch.compile(fullgraph=False)` is as follows:

1. [Determine the ideal location to place `torch.compile`](programming_model.where_to_apply_compile.html). Normally, it is the highest-level function that doesn't result in excessive graph breaks.
Functions that do a lot of preprocessing or I/O operations are examples of functions that result in many graph breaks and do not significantly benefit from `torch.compile`.
a. You can isolate issues by first compiling individual functions/modules before compiling entire models.
2. [Apply `torch.compiler.disable` to functions in the compiled region that result in a lot of graph breaks
and do not benefit from compilation](programming_model.compiler_disable.html). In this case, one graph break is better than potentially tens or hundreds.
3. [Use `TORCH_LOGS="graph_breaks"` or tlparse to investigate remaining graph breaks.](programming_model.observability.html)
Work around these graph breaks using the same approaches as working around graph breaks under
the `fullgraph=True` programming model. Not all graph breaks need to be removed - some may
impact performance more than others. The general rule is to focus on graph breaks that are happening during model computation.
a. We recommend using `torch.compile(backend='eager')` when debugging graph breaks, for faster debugging iteration times

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