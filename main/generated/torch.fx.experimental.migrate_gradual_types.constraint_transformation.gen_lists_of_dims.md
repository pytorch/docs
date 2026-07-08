# torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_lists_of_dims

torch.fx.experimental.migrate_gradual_types.constraint_transformation.gen_lists_of_dims(*num_tensors*, *dim_size*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/502e93eb52e0fcf07a908796ccd61af06c4b58b9/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1225)

Generate lists of DVar to represent tensor dimensions
:param num_tensors: the required number of tensors
:param dim_size: the number of dimensions for each tensor
:param counter: variable tracking

Returns: A list of a list of tensor dimensions

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[*DVar*]], [int](https://docs.python.org/3/library/functions.html#int)]