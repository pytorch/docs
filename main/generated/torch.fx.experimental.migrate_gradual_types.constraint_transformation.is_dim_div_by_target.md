# torch.fx.experimental.migrate_gradual_types.constraint_transformation.is_dim_div_by_target

torch.fx.experimental.migrate_gradual_types.constraint_transformation.is_dim_div_by_target(*target*, *dim*)[[source]](https://github.com/pytorch/pytorch/blob/55f1d787eeab8196db1c529de1754add16feec18/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1008)

Generate constraints to check if the input dimensions is divisible by the target dimensions
:param target: Target dimensions
:param dim: Input dimensions

Returns: Constraints to check divisibility

Return type:

*BinConstraintD*