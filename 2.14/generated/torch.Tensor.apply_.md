# torch.Tensor.apply_

Tensor.apply_(*callable*) → [Tensor](../tensors.html#torch.Tensor)

Applies the function `callable` to each element in the tensor, replacing
each element with the value returned by `callable`.

Note

This function only works with CPU tensors and should not be used in code
sections that require high performance.