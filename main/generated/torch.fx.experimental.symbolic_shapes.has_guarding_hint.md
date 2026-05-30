# torch.fx.experimental.symbolic_shapes.has_guarding_hint

torch.fx.experimental.symbolic_shapes.has_guarding_hint(*a*)[[source]](https://github.com/pytorch/pytorch/blob/e5aa1320b162fc3b9d0d53207fe340a6d3aa03d1/torch/fx/experimental/symbolic_shapes.py#L424)

Check if a symbolic value has a hint available for guarding.

Returns True if the value is concrete or if the symbolic node has a hint,
False otherwise.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)