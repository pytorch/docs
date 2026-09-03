# torch.fx.experimental.migrate_gradual_types.constraint_transformation.apply_padding

torch.fx.experimental.migrate_gradual_types.constraint_transformation.apply_padding(*e1_var*, *e11*, *e2*, *e12*, *d2*, *d11*, *d12*, *counter*)[[source]](https://github.com/pytorch/pytorch/blob/d7a82dcfcb838549a84f49516bc5c32ecf1eef90/torch/fx/experimental/migrate_gradual_types/constraint_transformation.py#L1115)

We are considering the possibility where one input has less dimensions than
another input, so we apply padding to the broadcasted results

Parameters:

- **e1_var** (*TVar*) - Variable representing the first input where padding will be
- **e11** (*BinConstraintT*) - constraint of the form e11 = Tensortype[d1, ..., dn]
- **e2** (*BinConstraintT*) - constraint of the form e2 = Tensortype[d1, ..., dn]
- **e12** (*BinConstraintT*) - constraint of the form e11 = Tensortype[d1, ..., dn]
- **d2** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**DVar**]*) - Tensor variables for the second input
- **d11** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**DVar**]*) - Tensor variables for the broadcasted first input
- **d12** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**DVar**]*) - Tensor variables for the broadcasted second input
- **counter** ([*int*](https://docs.python.org/3/library/functions.html#int)) - variable tracking

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[*Constraint*, [int](https://docs.python.org/3/library/functions.html#int)]

Returns: A new constraint whose goal is to apply padding to the broadcasted result