# torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_get_item_tensor

torch.fx.experimental.migrate_gradual_types.constraint_transformation.transform_get_item_tensor(*constraint*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/8df61039f8235b92b0ca250355cc296020f46e2d/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L235)

When the index is a tuple, then the output will be a tensor
TODO: we have to check if this is the case for all HF models

The cases we are covering here are a tuple with one of:

- slice with default argument
- None

None appends 1 to the input tensor dimensions
so each occurrence of 'None' increases the rank by 1

slice with default arguments does not change the rank

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[*Constraint*, [int](https://docs.python.org/3/library/functions.html#int)]