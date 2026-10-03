# torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_constraint

torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_constraint(*constraint*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/8ab13d788b9dab3e338e618576e65bb8b0c75e1a/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L875)

Transforms a constraint into a simpler constraint.
Ex: precision and consistency are transformed to equality
:param constraint: constraint to be transformed
:param counter: for variable tracking

Returns: Constraint

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[*Constraint*, [int](https://docs.python.org/3/builtins/functions.html#int)]