# torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_var

torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_var(*tensor*, *counter*, *dimension_dict*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/fx/experimental/migrate_gradual_types/transform_to_z3.py#L269)

Transforms tensor variables to a format understood by z3
:param tensor: Tensor variable or a tensor type potentially with variable dimensions

Returns: Transformed variable to a z3 format

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any), [int](https://docs.python.org/3/library/functions.html#int)]