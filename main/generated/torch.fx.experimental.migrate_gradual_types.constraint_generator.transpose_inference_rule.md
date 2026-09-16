# torch.fx.experimental.migrate_gradual_types.constraint_generator.transpose_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.transpose_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/a483bad75086c479c263d54ad3dbf19e1fde74d8/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L415)

Can be considered as a sequence of two index selects, so we generate constraints accordingly

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/builtins/functions.html#int)]