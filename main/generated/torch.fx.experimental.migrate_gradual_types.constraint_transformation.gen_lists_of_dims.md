# torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_lists_of_dims

torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_lists_of_dims(*num_tensors*, *dim_size*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1225)

Generate lists of DVar to represent tensor dimensions
:param num_tensors: the required number of tensors
:param dim_size: the number of dimensions for each tensor
:param counter: variable tracking

Returns: A list of a list of tensor dimensions

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*DVar*]], [int](https://docs.python.org/3/library/functions.html#int)]