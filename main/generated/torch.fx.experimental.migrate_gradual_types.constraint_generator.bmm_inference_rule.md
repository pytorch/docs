# torch.fx.experimental.migrate_gradual_types.constraint_generator.bmm_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.bmm_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L165)

Constraints that match the input to a size 3 tensor
and switch the dimensions according to the rules
of batch multiplication

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]