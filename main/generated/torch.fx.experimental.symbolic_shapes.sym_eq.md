# torch.fx.experimental.symbolic_shapes.sym_eq

torch.fx.experimental.symbolic_shapes.sym_eq(*x*, *y*)[[source]](https://github.com/pytorch/pytorch/blob/8d6343a7cd80821d54ba546bc6f799aad9ccb79c/torch/fx/experimental/symbolic_shapes.py#L1695)

Like ==, but when run on list/tuple, it will recursively test equality
and use sym_and to join the results together, without guarding.

Return type:

BoolLikeType