# torch.fx.experimental.migrate_gradual_types.constraint_generator.layer_norm_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.layer_norm_inference_rule(*n*, *module_instance*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L1331)

Input and output shapes should be equal.
Input should be consistent with the normalized_shape

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]