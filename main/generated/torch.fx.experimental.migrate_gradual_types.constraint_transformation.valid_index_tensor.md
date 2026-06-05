# torch.fx.experimental.migrate_gradual_types.constraint_transformation.valid_index_tensor

torch.fx.experimental.migrate_gradual_types.constraint_transformation.valid_index_tensor(*index*, *dims*)[[source]](https://github.com/pytorch/pytorch/blob/784e50bb03d4ff5f8fdc368da8449558a8fb4a43/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L220)

if the slice instances exceed the length of the dimensions
then this is a type error so we return False

Return type:

*Constraint*