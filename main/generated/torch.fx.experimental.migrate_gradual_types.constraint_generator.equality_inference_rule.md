# torch.fx.experimental.migrate_gradual_types.constraint_generator.equality_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.equality_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L371)

We generate the constraint: input = output

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/builtins/functions.html#int)]