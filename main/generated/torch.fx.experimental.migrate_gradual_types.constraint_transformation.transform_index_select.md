# torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_index_select

torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_index_select(*constraint*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L147)

The constraints consider the given tensor size, checks if the index is valid
and if so, generates a constraint for replacing the input dimension
with the required dimension

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[*Constraint*, [int](https://docs.python.org/3/builtins/functions.html#int)]