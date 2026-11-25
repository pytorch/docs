# torch.fx.experimental.migrate_gradual_types.constraint_generator.linear_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.linear_inference_rule(*n*, *module_instance*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/7e752fbd7bf384857985d3e556423eaca714bbfe/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L1401)

Input and output sizes should be the same except for the last dimension
If the input is Dyn, then so should the output

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/builtins/functions.html#int)]