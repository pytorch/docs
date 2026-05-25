# torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_greatest_upper_bound

torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_greatest_upper_bound(*constraint*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/69bbaeafe0b3f1e423be17b25ca11b149845b521/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1317)

Parameters:

- **constraint** (*TGreatestUpperBound*) - Greatest upper bound on tensors
- **counter** ([*int*](https://docs.python.org/3/library/functions.html#int)) - variable tracking

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]

Returns: A set of equality constraints and DGreatestUpperBound constraints