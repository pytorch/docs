# torch.fx.experimental.migrate_gradual_types.constraint_generator.neq_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.neq_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/2dc676a67d91491beadb4615ae9fe15e144086ea/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L925)

Translates to inconsistent in gradual types.
To prove inequality, we should prove that
tensors are either different sizes or
disagree on at least one dimension

This is a WIP (works when the condition
is false. We are working on making this operation work
when the condition is true as well)

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/builtins/functions.html#int)]