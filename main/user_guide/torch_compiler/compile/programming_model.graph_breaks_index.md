# Working with Graph Breaks

As you might remember from [Dynamo Core Concepts](programming_model.dynamo_core_concepts.html) that Dynamo performs a graph break when
it encounters code that can't be traced. In the default `torch.compile` settings, Dynamo compiles the FX graph
that has been determined up to that point, executes the unsupported code in regular Python, and then resumes tracing.

Graph breaks enable Dynamo to trace through arbitrary Python code and carve out functional
subgraphs that can each be individually optimized.

However, graph breaks may cause unexpected slowness in `torch.compile`.
If you're not seeing the expected speedups, we recommend checking for graph breaks and removing them.

The following sections outline strategies for addressing graph breaks.

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