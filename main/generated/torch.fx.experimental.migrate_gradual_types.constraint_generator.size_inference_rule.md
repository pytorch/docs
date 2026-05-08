# torch.fx.experimental.migrate_gradual_types.constraint_generator.size_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.size_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/3565a492def04bf126af9d46958533d16fb88274/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L636)

The constraint is just lhs = rhs.
Ex: size = input_ids.size()

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]