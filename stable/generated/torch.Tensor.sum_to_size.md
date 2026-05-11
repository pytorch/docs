# torch.Tensor.sum_to_size

Tensor.sum_to_size(**size*) → [Tensor](../tensors.html#torch.Tensor)

Sum `this` tensor to [`size`](torch.Tensor.size.html#torch.Tensor.size).
[`size`](torch.Tensor.size.html#torch.Tensor.size) must be broadcastable to `this` tensor size.

Parameters:

**size** ([*int*](https://docs.python.org/3/library/functions.html#int)*...*) - a sequence of integers defining the shape of the output tensor.