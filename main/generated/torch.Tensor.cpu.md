# torch.Tensor.cpu

Tensor.cpu(*memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

Returns a copy of this object in CPU memory.

If this object is already in CPU memory,
then no copy is performed and the original object is returned.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.