# torch.fx.experimental.migrate_gradual_types.constraint_generator.get_attr_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.get_attr_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/502e93eb52e0fcf07a908796ccd61af06c4b58b9/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L142)

If the attribute is "device" then the tensor shape is preserved

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]