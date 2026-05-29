# torch.fx.experimental.migrate_gradual_types.constraint_generator.linear_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.linear_inference_rule(*n*, *module_instance*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/516f64b797cf7645a973e20d856d3e0ddec79948/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L1401)

Input and output sizes should be the same except for the last dimension
If the input is Dyn, then so should the output

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]