# torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_consistency_constraints

torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_consistency_constraints(*constraint*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1280)

Parameters:

- **constraint** (*BinConstraintT*) - Consistency constraint on tensors
- **counter** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - for variable tracking

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*Constraint*], [int](https://docs.python.org/3/builtins/functions.html#int)]

Returns: Equality and consistency constraints on dimensions