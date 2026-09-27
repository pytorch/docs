# torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_var

torch.fx.experimental.migrate_gradual_types.transform_to_z3.transform_var(*tensor*, *counter*, *dimension_dict*)[[source]](https://github.com/pytorch/pytorch/blob/8bea8e2d91031a1dee02417397d5a065e31c43c8/torch/fx/experimental/migrate_gradual_types/transform_to_z3.py#L269)

Transforms tensor variables to a format understood by z3
:param tensor: Tensor variable or a tensor type potentially with variable dimensions

Returns: Transformed variable to a z3 format

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any), [int](https://docs.python.org/3/builtins/functions.html#int)]