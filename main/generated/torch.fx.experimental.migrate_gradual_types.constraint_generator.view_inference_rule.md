# torch.fx.experimental.migrate_gradual_types.constraint_generator.view_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.view_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/e3b3670d208b9e770a7ca36a3fed1ea0f052f799/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L591)

Similar to reshape but with an extra condition on the strides

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]