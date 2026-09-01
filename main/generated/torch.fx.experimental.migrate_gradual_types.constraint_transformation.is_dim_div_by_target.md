# torch.fx.experimental.migrate_gradual_types.constraint_transformation.is_dim_div_by_target

torch.fx.experimental.migrate_gradual_types.constraint_transformation.is_dim_div_by_target(*target*, *dim*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1008)

Generate constraints to check if the input dimensions is divisible by the target dimensions
:param target: Target dimensions
:param dim: Input dimensions

Returns: Constraints to check divisibility

Return type:

*BinConstraintD*