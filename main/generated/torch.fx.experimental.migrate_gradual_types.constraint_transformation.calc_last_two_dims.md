# torch.fx.experimental.migrate_gradual_types.constraint_transformation.calc_last_two_dims

torch.fx.experimental.migrate_gradual_types.constraint_transformation.calc_last_two_dims(*constraint*, *d*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L895)

Generates constraints for the last two dimensions of a convolution or a maxpool output
:param constraint: CalcConv or CalcMaxPool
:param d: The list of output dimensions

Returns: Constraints for calculating the last two dimensions of the output

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[*Constraint*, *Constraint*]