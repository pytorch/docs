# torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_greatest_upper_bound

torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_greatest_upper_bound(*constraint*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1317)

Parameters:

- **constraint** (*TGreatestUpperBound*) - Greatest upper bound on tensors
- **counter** ([*int*](https://docs.python.org/3/library/functions.html#int)) - variable tracking

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]

Returns: A set of equality constraints and DGreatestUpperBound constraints