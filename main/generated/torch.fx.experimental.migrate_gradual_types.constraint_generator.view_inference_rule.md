# torch.fx.experimental.migrate_gradual_types.constraint_generator.view_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.view_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/7e9fd4e82a01d43fc8afdf03258cf85ee22db2ea/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L591)

Similar to reshape but with an extra condition on the strides

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]