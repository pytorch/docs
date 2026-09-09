# torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_all_constraints_trace_time

torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_all_constraints_trace_time(*tracer_root*, *graph*, *node*, *counter=0*)[[source]](https://github.com/pytorch/pytorch/blob/c712ec6ebb4ecd2838e2cafb0bbc7a3c5acfe668/torch/fx/experimental/migrate_gradual_types/transform_to_z3.py#L440)

Takes a node and a graph and generates two sets of constraints.
One set constraints the node's constraints and another set
constraints the negation of the node's constraints
:param tracer_root: the root for getting the module instances
:param graph: the graph so far in the tracing process
:param node: node that represents a conditional
:param counter: variable tracking

Returns: Two sets of constraints. One with a conjunction with the
conditional constraint and the other with a conjunction with
its negation.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]