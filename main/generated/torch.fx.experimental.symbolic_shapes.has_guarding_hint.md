# torch.fx.experimental.symbolic_shapes.has_guarding_hint

torch.fx.experimental.symbolic_shapes.has_guarding_hint(*a*)[[source]](https://github.com/pytorch/pytorch/blob/7a37a01092627acd59ddfcb9cefe5a578f5f6996/torch/fx/experimental/symbolic_shapes.py#L428)

Check if a symbolic value has a hint available for guarding.

Returns True if the value is concrete or if the symbolic node has a hint,
False otherwise.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)