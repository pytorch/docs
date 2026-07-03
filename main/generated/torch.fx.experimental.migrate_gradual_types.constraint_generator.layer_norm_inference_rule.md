# torch.fx.experimental.migrate_gradual_types.constraint_generator.layer_norm_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.layer_norm_inference_rule(*n*, *module_instance*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L1331)

Input and output shapes should be equal.
Input should be consistent with the normalized_shape

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]