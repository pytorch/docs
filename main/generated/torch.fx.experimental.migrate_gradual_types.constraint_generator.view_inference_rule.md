# torch.fx.experimental.migrate_gradual_types.constraint_generator.view_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.view_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L591)

Similar to reshape but with an extra condition on the strides

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/builtins/functions.html#int)]