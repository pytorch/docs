# torch.fx.experimental.migrate_gradual_types.constraint_generator.size_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.size_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/c8532b3e7f0e3aec4bb518524c3ca041e17665aa/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L636)

The constraint is just lhs = rhs.
Ex: size = input_ids.size()

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/builtins/functions.html#int)]