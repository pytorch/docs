# torch.fx.experimental.migrate_gradual_types.constraint_generator.get_attr_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.get_attr_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/fd6d216e3e8bf07c470716dfbf022d82fadd521d/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L142)

If the attribute is "device" then the tensor shape is preserved

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]