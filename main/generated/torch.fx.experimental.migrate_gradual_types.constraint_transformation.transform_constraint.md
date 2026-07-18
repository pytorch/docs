# torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_constraint

torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_constraint(*constraint*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/c8080db61856d74ad76795af1c6aa1fd41b7b862/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L875)

Transforms a constraint into a simpler constraint.
Ex: precision and consistency are transformed to equality
:param constraint: constraint to be transformed
:param counter: for variable tracking

Returns: Constraint

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[*Constraint*, [int](https://docs.python.org/3/library/functions.html#int)]