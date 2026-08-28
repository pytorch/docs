# torch.fx.experimental.migrate_gradual_types.constraint_transformation.valid_index_tensor

torch.fx.experimental.migrate_gradual_types.constraint_transformation.valid_index_tensor(*index*, *dims*)[[source]](https://github.com/pytorch/pytorch/blob/7e9fd4e82a01d43fc8afdf03258cf85ee22db2ea/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L220)

if the slice instances exceed the length of the dimensions
then this is a type error so we return False

Return type:

*Constraint*