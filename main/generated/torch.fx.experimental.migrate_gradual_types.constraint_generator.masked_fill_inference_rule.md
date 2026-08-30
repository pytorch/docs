# torch.fx.experimental.migrate_gradual_types.constraint_generator.masked_fill_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.masked_fill_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L481)

Similar to addition. For now we implement the constraints when
the argument is a boolean tensor. There is also a case for when
it is a condition. We will leave this out for now.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]