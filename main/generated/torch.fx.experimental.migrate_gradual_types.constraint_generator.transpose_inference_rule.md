# torch.fx.experimental.migrate_gradual_types.constraint_generator.transpose_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.transpose_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L415)

Can be considered as a sequence of two index selects, so we generate constraints accordingly

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]