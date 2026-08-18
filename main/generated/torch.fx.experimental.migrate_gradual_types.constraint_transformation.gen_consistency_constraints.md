# torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_consistency_constraints

torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_consistency_constraints(*constraint*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1280)

Parameters:

- **constraint** (*BinConstraintT*) - Consistency constraint on tensors
- **counter** ([*int*](https://docs.python.org/3/library/functions.html#int)) - for variable tracking

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/library/functions.html#int)]

Returns: Equality and consistency constraints on dimensions