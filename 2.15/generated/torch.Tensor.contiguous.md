# torch.Tensor.contiguous

Tensor.contiguous(*memory_format=torch.contiguous_format*) → [Tensor](../tensors.html#torch.Tensor)

Returns a contiguous in memory tensor containing the same data as `self` tensor. If
`self` tensor is already in the specified memory format, this function returns the
`self` tensor.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.contiguous_format`.