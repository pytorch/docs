# torch.fx.experimental.migrate_gradual_types.constraint_generator.bmm_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.bmm_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/a37249c7e9824d557710fe7682d943593ef355d8/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L165)

Constraints that match the input to a size 3 tensor
and switch the dimensions according to the rules
of batch multiplication

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]