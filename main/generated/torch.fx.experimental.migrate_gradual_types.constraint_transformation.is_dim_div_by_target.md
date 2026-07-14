# torch.fx.experimental.migrate_gradual_types.constraint_transformation.is_dim_div_by_target

torch.fx.experimental.migrate_gradual_types.constraint_transformation.is_dim_div_by_target(*target*, *dim*)[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1008)

Generate constraints to check if the input dimensions is divisible by the target dimensions
:param target: Target dimensions
:param dim: Input dimensions

Returns: Constraints to check divisibility

Return type:

*BinConstraintD*