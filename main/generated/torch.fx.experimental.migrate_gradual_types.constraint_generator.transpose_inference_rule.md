# torch.fx.experimental.migrate_gradual_types.constraint_generator.transpose_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.transpose_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/df83f06a8c49a667b9408934fa9eaae1aaf32d04/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L415)

Can be considered as a sequence of two index selects, so we generate constraints accordingly

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]