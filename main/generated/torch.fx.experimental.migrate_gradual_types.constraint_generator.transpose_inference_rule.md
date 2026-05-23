# torch.fx.experimental.migrate_gradual_types.constraint_generator.transpose_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.transpose_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/2f696474dc8fe614670ddb889f4ae1c75d1a11e6/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L415)

Can be considered as a sequence of two index selects, so we generate constraints accordingly

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]