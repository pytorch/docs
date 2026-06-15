# torch.fx.experimental.migrate_gradual_types.constraint_generator.bmm_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.bmm_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/6a231d0d3e1ccd63dd51479bcadc969d0a8de2b9/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L165)

Constraints that match the input to a size 3 tensor
and switch the dimensions according to the rules
of batch multiplication

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]