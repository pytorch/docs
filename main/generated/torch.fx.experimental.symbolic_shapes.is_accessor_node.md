# torch.fx.experimental.symbolic_shapes.is_accessor_node

torch.fx.experimental.symbolic_shapes.is_accessor_node(*node*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/fx/experimental/symbolic_shapes.py#L739)

Helper function to determine if a node is trying to access
a symbolic integer such as size, stride, offset or item. Currently
primarily only used in a DCE pass to figure out purity.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)