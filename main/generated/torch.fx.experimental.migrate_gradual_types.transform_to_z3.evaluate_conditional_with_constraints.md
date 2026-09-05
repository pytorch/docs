# torch.fx.experimental.migrate_gradual_types.transform_to_z3.evaluate_conditional_with_constraints

torch.fx.experimental.migrate_gradual_types.transform_to_z3.evaluate_conditional_with_constraints(*tracer_root*, *graph*, *node*, *counter=0*, *user_constraints=None*)[[source]](https://github.com/pytorch/pytorch/blob/13818df097cc56c9a2a860678049f2a42a008853/torch/fx/experimental/migrate_gradual_types/transform_to_z3.py#L508)

Given an IR and a node representing a conditional, evaluate the conditional
and its negation
:param tracer_root: Tracer root for module instances
:param node: The node to be evaluated

Returns: the results of evaluating the condition and the negation with
the rest of the constraints

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]