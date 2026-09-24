# torch.fx.experimental.migrate_gradual_types.constraint_generator.masked_fill_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.masked_fill_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L481)

Similar to addition. For now we implement the constraints when
the argument is a boolean tensor. There is also a case for when
it is a condition. We will leave this out for now.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/builtins/functions.html#int)]