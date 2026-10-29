# torch.fx.experimental.migrate_gradual_types.constraint_generator.linear_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.linear_inference_rule(*n*, *module_instance*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L1401)

Input and output sizes should be the same except for the last dimension
If the input is Dyn, then so should the output

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/builtins/functions.html#int)]