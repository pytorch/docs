# torch.fx.experimental.migrate_gradual_types.constraint_transformation.is_target_div_by_dim

torch.fx.experimental.migrate_gradual_types.constraint_transformation.is_target_div_by_dim(*target*, *dim*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L993)

Generate constraints to check if the target dimensions are divisible by the input dimensions
:param target: Target dimensions
:param dim: Input dimensions

Returns: Constraints to check divisibility

Return type:

*BinConstraintD*