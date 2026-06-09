# torch.fx.experimental.migrate_gradual_types.constraint_transformation.broadcast_dim

torch.fx.experimental.migrate_gradual_types.constraint_transformation.broadcast_dim(*tensor_input1*, *tensor_input2*, *res1*, *res2*, *index*, *padding=False*)[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1070)

Apply broadcasting to the 'index' dimension of tensor_input1.
:param tensor_input1: should represent [d1, ..., d_index, ...] where d_index = 1
:param tensor_input2: represents the second input
:param res1: broadcasted result 1
:param res2: broadcasted result 2
:param index: the index to broadcast
:param padding: If padding was used, then tensor_input1[index] does not exist

Returns:

Return type:

*Constraint*