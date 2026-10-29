# torch.fx.experimental.migrate_gradual_types.constraint_generator.size_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.size_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L636)

The constraint is just lhs = rhs.
Ex: size = input_ids.size()

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/builtins/functions.html#int)]