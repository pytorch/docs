# torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_index_select

torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_index_select(*constraint*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L147)

The constraints consider the given tensor size, checks if the index is valid
and if so, generates a constraint for replacing the input dimension
with the required dimension

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[*Constraint*, [int](https://docs.python.org/3/library/functions.html#int)]