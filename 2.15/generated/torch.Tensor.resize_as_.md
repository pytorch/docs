# torch.Tensor.resize_as_

Tensor.resize_as_(*tensor*, *memory_format=torch.contiguous_format*) → [Tensor](../tensors.html#torch.Tensor)

Resizes the `self` tensor to be the same size as the specified
[`tensor`](torch.tensor.html#torch.tensor). This is equivalent to `self.resize_(tensor.size())`.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
Tensor. Default: `torch.contiguous_format`. Note that memory format of
`self` is going to be unaffected if `self.size()` matches `tensor.size()`.