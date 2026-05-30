# torch.fx.experimental.migrate_gradual_types.constraint_generator.bmm_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.bmm_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/e5aa1320b162fc3b9d0d53207fe340a6d3aa03d1/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L165)

Constraints that match the input to a size 3 tensor
and switch the dimensions according to the rules
of batch multiplication

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]