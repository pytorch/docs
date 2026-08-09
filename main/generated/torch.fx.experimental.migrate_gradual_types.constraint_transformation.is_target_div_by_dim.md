# torch.fx.experimental.migrate_gradual_types.constraint_transformation.is_target_div_by_dim

torch.fx.experimental.migrate_gradual_types.constraint_transformation.is_target_div_by_dim(*target*, *dim*)[[source]](https://github.com/pytorch/pytorch/blob/a471a58d241b08025dcb4ec69c2d30e5a49a757a/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L993)

Generate constraints to check if the target dimensions are divisible by the input dimensions
:param target: Target dimensions
:param dim: Input dimensions

Returns: Constraints to check divisibility

Return type:

*BinConstraintD*