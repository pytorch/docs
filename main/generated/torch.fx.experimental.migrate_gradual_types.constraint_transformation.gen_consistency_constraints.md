# torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_consistency_constraints

torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_consistency_constraints(*constraint*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/847b7df02b84551445eda7d44d08f15bda4c6159/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1280)

Parameters:

- **constraint** (*BinConstraintT*) - Consistency constraint on tensors
- **counter** ([*int*](https://docs.python.org/3/library/functions.html#int)) - for variable tracking

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]

Returns: Equality and consistency constraints on dimensions