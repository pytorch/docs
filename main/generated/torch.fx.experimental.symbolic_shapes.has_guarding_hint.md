# torch.fx.experimental.symbolic_shapes.has_guarding_hint

torch.fx.experimental.symbolic_shapes.has_guarding_hint(*a*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/fx/experimental/symbolic_shapes.py#L429)

Check if a symbolic value has a hint available for guarding.

Returns True if the value is concrete or if the symbolic node has a hint,
False otherwise.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)