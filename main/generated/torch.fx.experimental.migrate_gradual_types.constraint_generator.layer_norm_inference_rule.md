# torch.fx.experimental.migrate_gradual_types.constraint_generator.layer_norm_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.layer_norm_inference_rule(*n*, *module_instance*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/474b9649dd111ae9b0c31728da812cc3dda2c4ae/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L1331)

Input and output shapes should be equal.
Input should be consistent with the normalized_shape

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]