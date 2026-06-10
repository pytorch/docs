# torch.Tensor.as_subclass

Tensor.as_subclass(*cls*) → [Tensor](../tensors.html#torch.Tensor)

Makes a `cls` instance with the same data pointer as `self`. Changes
in the output mirror changes in `self`, and the output stays attached
to the autograd graph. `cls` must be a subclass of `Tensor`.