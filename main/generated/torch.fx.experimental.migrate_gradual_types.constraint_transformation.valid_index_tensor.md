# torch.fx.experimental.migrate_gradual_types.constraint_transformation.valid_index_tensor

torch.fx.experimental.migrate_gradual_types.constraint_transformation.valid_index_tensor(*index*, *dims*)[[source]](https://github.com/pytorch/pytorch/blob/6f990b7ff484061525619d9776bb4c8174e00a4c/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L220)

if the slice instances exceed the length of the dimensions
then this is a type error so we return False

Return type:

*Constraint*