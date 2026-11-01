# torch.fx.experimental.symbolic_shapes.sym_eq

torch.fx.experimental.symbolic_shapes.sym_eq(*x*, *y*)[[source]](https://github.com/pytorch/pytorch/blob/6728ae647ab077842210f24d515b54df7709e144/torch/fx/experimental/symbolic_shapes.py#L1696)

Like ==, but when run on list/tuple, it will recursively test equality
and use sym_and to join the results together, without guarding.

Return type:

BoolLikeType