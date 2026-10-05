# torch.fx.experimental.symbolic_shapes.has_guarding_hint

torch.fx.experimental.symbolic_shapes.has_guarding_hint(*a*)[[source]](https://github.com/pytorch/pytorch/blob/33758f2ecb591b1bafb30f385b1acb73b6367ba9/torch/fx/experimental/symbolic_shapes.py#L430)

Check if a symbolic value has a hint available for guarding.

Returns True if the value is concrete or if the symbolic node has a hint,
False otherwise.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)