# torch.fx.experimental.migrate_gradual_types.constraint_transformation.valid_index_tensor

torch.fx.experimental.migrate_gradual_types.constraint_transformation.valid_index_tensor(*index*, *dims*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L220)

if the slice instances exceed the length of the dimensions
then this is a type error so we return False

Return type:

*Constraint*