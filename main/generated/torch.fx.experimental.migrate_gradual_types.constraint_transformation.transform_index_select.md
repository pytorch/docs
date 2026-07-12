# torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_index_select

torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_index_select(*constraint*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/dea5f568512cef2ab009ee7858b1cfd9be8ba924/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L147)

The constraints consider the given tensor size, checks if the index is valid
and if so, generates a constraint for replacing the input dimension
with the required dimension

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[*Constraint*, [int](https://docs.python.org/3/library/functions.html#int)]