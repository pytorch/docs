# torch.fx.experimental.migrate_gradual_types.constraint_generator.bmm_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.bmm_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/9a3243ec510ddea6c63c86d01aef273f400f375f/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L165)

Constraints that match the input to a size 3 tensor
and switch the dimensions according to the rules
of batch multiplication

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]