# torch.fx.experimental.migrate_gradual_types.constraint_generator.cumsum_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.cumsum_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L699)

Input and output shapes should be equal
We should verify that the index is valid

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]