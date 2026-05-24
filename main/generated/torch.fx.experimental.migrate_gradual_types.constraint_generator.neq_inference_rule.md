# torch.fx.experimental.migrate_gradual_types.constraint_generator.neq_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.neq_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/15e96b281415c58d3acf5d63d86df9d68744ee16/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L925)

Translates to inconsistent in gradual types.
To prove inequality, we should prove that
tensors are either different sizes or
disagree on at least one dimension

This is a WIP (works when the condition
is false. We are working on making this operation work
when the condition is true as well)

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]