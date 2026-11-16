# torch.fx.experimental.migrate_gradual_types.constraint_generator.index_select_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.index_select_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L239)

We constrain the second argument to a vector or Dyn.
The output replaces the input with the shape of the vector
at the position given by the index (first argument)

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/builtins/functions.html#int)]