# torch.fx.experimental.migrate_gradual_types.constraint_transformation.valid_index_tensor

torch.fx.experimental.migrate_gradual_types.constraint_transformation.valid_index_tensor(*index*, *dims*)[[source]](https://github.com/pytorch/pytorch/blob/c5a2c86d66eda12ed122b796baae9cb0aaf5aefb/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L220)

if the slice instances exceed the length of the dimensions
then this is a type error so we return False

Return type:

*Constraint*