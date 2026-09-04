# torch.fx.experimental.migrate_gradual_types.constraint_transformation.is_dim_div_by_target

torch.fx.experimental.migrate_gradual_types.constraint_transformation.is_dim_div_by_target(*target*, *dim*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1008)

Generate constraints to check if the input dimensions is divisible by the target dimensions
:param target: Target dimensions
:param dim: Input dimensions

Returns: Constraints to check divisibility

Return type:

*BinConstraintD*