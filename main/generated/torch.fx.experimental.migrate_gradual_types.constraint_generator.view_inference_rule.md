# torch.fx.experimental.migrate_gradual_types.constraint_generator.view_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.view_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/8bea8e2d91031a1dee02417397d5a065e31c43c8/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L591)

Similar to reshape but with an extra condition on the strides

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/builtins/functions.html#int)]