# torch.fx.experimental.migrate_gradual_types.constraint_generator.cumsum_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.cumsum_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/7798c7075502848ec00766455ada537e02f55ee1/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L699)

Input and output shapes should be equal
We should verify that the index is valid

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/builtins/functions.html#int)]