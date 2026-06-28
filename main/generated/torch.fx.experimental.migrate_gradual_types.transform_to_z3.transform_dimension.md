# torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_dimension

torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_dimension(*dimension*, *counter*, *dimension_dict*)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/fx/experimental/migrate_gradual_types/transform_to_z3.py#L311)

Takes a dimension variable or a number and transforms it to a tuple
according to our scheme
:param dimension: The dimension to be transformed
:param counter: variable tracking

Returns: tuple and the current counter

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any), [int](https://docs.python.org/3/library/functions.html#int)]