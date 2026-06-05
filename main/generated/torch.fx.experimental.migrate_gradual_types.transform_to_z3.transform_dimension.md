# torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_dimension

torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_dimension(*dimension*, *counter*, *dimension_dict*)[[source]](https://github.com/pytorch/pytorch/blob/784e50bb03d4ff5f8fdc368da8449558a8fb4a43/torch/fx/experimental/migrate_gradual_types/transform_to_z3.py#L311)

Takes a dimension variable or a number and transforms it to a tuple
according to our scheme
:param dimension: The dimension to be transformed
:param counter: variable tracking

Returns: tuple and the current counter

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any), [int](https://docs.python.org/3/library/functions.html#int)]