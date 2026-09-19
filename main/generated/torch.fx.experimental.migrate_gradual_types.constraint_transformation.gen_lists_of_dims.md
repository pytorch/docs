# torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_lists_of_dims

torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_lists_of_dims(*num_tensors*, *dim_size*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/b7954b2399da4803024b9a2850e39c588522015f/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1225)

Generate lists of DVar to represent tensor dimensions
:param num_tensors: the required number of tensors
:param dim_size: the number of dimensions for each tensor
:param counter: variable tracking

Returns: A list of a list of tensor dimensions

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[*DVar*]], [int](https://docs.python.org/3/builtins/functions.html#int)]