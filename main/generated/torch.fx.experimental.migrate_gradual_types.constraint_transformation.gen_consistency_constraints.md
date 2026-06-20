# torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_consistency_constraints

torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_consistency_constraints(*constraint*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/27b52de22e4e5fa572c07a4065423083a41b8756/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1280)

Parameters:

- **constraint** (*BinConstraintT*) - Consistency constraint on tensors
- **counter** ([*int*](https://docs.python.org/3/library/functions.html#int)) - for variable tracking

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]

Returns: Equality and consistency constraints on dimensions