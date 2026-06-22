# torch.fx.experimental.symbolic_shapes.sym_eq

torch.fx.experimental.symbolic_shapes.sym_eq(*x*, *y*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/fx/experimental/symbolic_shapes.py#L1683)

Like ==, but when run on list/tuple, it will recursively test equality
and use sym_and to join the results together, without guarding.

Return type:

BoolLikeType