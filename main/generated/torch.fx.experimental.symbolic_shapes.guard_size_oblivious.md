# torch.fx.experimental.symbolic_shapes.guard_size_oblivious

torch.fx.experimental.symbolic_shapes.guard_size_oblivious(*expr*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/fx/experimental/symbolic_shapes.py#L530)

Perform a guard on a symbolic boolean expression in a size oblivious way.
This is typically used when a non-oblivious test would result in a guard
on a data dependent value of which we don't know the value of at compile time.
When a guard is tested this way, we may diverge in behavior from how regular
PyTorch semantics would treat it. For more information, see
[pytorch/pytorch#118579](https://github.com/pytorch/pytorch/pull/118579)

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)