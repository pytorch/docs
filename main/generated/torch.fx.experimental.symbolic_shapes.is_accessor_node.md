# torch.fx.experimental.symbolic_shapes.is_accessor_node

torch.fx.experimental.symbolic_shapes.is_accessor_node(*node*)[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/fx/experimental/symbolic_shapes.py#L743)

Helper function to determine if a node is trying to access
a symbolic integer such as size, stride, offset or item. Currently
primarily only used in a DCE pass to figure out purity.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)