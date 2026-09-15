# torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_greatest_upper_bound

torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_greatest_upper_bound(*constraint*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1317)

Parameters:

- **constraint** (*TGreatestUpperBound*) - Greatest upper bound on tensors
- **counter** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - variable tracking

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/builtins/functions.html#int)]

Returns: A set of equality constraints and DGreatestUpperBound constraints