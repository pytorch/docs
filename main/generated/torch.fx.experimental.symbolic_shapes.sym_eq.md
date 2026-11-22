# torch.fx.experimental.symbolic_shapes.sym_eq

torch.fx.experimental.symbolic_shapes.sym_eq(*x*, *y*)[[source]](https://github.com/pytorch/pytorch/blob/65e101a3cc8242711ae1cb467ed6cde097135821/torch/fx/experimental/symbolic_shapes.py#L1728)

Like ==, but when run on list/tuple, it will recursively test equality
and use sym_and to join the results together, without guarding.

Return type:

BoolLikeType