# torch.fx.experimental.symbolic_shapes.is_accessor_node

torch.fx.experimental.symbolic_shapes.is_accessor_node(*node*)[[source]](https://github.com/pytorch/pytorch/blob/e1994aea9ce307fb82feeb7524ab2c5d36771e4f/torch/fx/experimental/symbolic_shapes.py#L745)

Helper function to determine if a node is trying to access
a symbolic integer such as size, stride, offset or item. Currently
primarily only used in a DCE pass to figure out purity.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)