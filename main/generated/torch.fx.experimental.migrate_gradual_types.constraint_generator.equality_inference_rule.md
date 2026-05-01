# torch.fx.experimental.migrate_gradual_types.constraint_generator.equality_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.equality_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L371)

We generate the constraint: input = output

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]