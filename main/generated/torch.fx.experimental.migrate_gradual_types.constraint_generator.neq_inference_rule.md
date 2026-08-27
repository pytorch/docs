# torch.fx.experimental.migrate_gradual_types.constraint_generator.neq_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.neq_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L925)

Translates to inconsistent in gradual types.
To prove inequality, we should prove that
tensors are either different sizes or
disagree on at least one dimension

This is a WIP (works when the condition
is false. We are working on making this operation work
when the condition is true as well)

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]