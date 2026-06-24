# torch.fx.experimental.symbolic_shapes.sym_eq

torch.fx.experimental.symbolic_shapes.sym_eq(*x*, *y*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/fx/experimental/symbolic_shapes.py#L1683)

Like ==, but when run on list/tuple, it will recursively test equality
and use sym_and to join the results together, without guarding.

Return type:

BoolLikeType