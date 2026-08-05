# torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_all_broadcasting_possibilities_no_padding

torch.fx.experimental.migrate_gradual_types.constraint_transformation.generate_all_broadcasting_possibilities_no_padding(*d1*, *d2*, *d11*, *d12*)[[source]](https://github.com/pytorch/pytorch/blob/e3b3670d208b9e770a7ca36a3fed1ea0f052f799/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1361)

Generate broadcasting constraints assuming no padding. Broadcasting can happen at any dimension.
We look at all combinations for all dimensions in d1 and d2
:param d1: input1 dimensions
:param d2: input2 dimensions
:param d11: broadcasted input1 dimensions
:param d12: broadcasted input2 dimensions

Returns: broadcasting constraints relating the input dimensions to the broadcasted dimensions

Return type:

*Constraint*