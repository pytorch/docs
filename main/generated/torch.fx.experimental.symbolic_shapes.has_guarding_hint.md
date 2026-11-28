# torch.fx.experimental.symbolic_shapes.has_guarding_hint

torch.fx.experimental.symbolic_shapes.has_guarding_hint(*a*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/fx/experimental/symbolic_shapes.py#L463)

Check if a symbolic value has a hint available for guarding.

Returns True if the value is concrete or if the symbolic node has a hint,
False otherwise.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)