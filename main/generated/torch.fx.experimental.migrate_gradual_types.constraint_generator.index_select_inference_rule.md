# torch.fx.experimental.migrate_gradual_types.constraint_generator.index_select_inference_rule

torch.fx.experimental.migrate_gradual_types.constraint_generator.index_select_inference_rule(*n*, *symbols*, *constraints*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/a471a58d241b08025dcb4ec69c2d30e5a49a757a/torch/fx/experimental/migrate_gradual_types/constraint_generator.py#L239)

We constrain the second argument to a vector or Dyn.
The output replaces the input with the shape of the vector
at the position given by the index (first argument)

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]