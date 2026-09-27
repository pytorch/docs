# torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_dimension

torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_dimension(*dimension*, *counter*, *dimension_dict*)[[source]](https://github.com/pytorch/pytorch/blob/8bea8e2d91031a1dee02417397d5a065e31c43c8/torch/fx/experimental/migrate_gradual_types/transform_to_z3.py#L311)

Takes a dimension variable or a number and transforms it to a tuple
according to our scheme
:param dimension: The dimension to be transformed
:param counter: variable tracking

Returns: tuple and the current counter

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any), [int](https://docs.python.org/3/builtins/functions.html#int)]