# torch.fx.experimental.symbolic_shapes.is_accessor_node

torch.fx.experimental.symbolic_shapes.is_accessor_node(*node*)[[source]](https://github.com/pytorch/pytorch/blob/5cd392bfe432d57e7beb9ab67037ddc0fcc01205/torch/fx/experimental/symbolic_shapes.py#L739)

Helper function to determine if a node is trying to access
a symbolic integer such as size, stride, offset or item. Currently
primarily only used in a DCE pass to figure out purity.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)