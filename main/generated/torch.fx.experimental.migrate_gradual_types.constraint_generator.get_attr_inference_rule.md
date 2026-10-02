# torch.fx.experimental.migrate_gradual_types.constraint_generator.get_attr_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.get_attr_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/dcd7ed975a6b090ec2bcf2360c28c9a263be8fe5/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L142)

If the attribute is "device" then the tensor shape is preserved

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/builtins/functions.html#int)]