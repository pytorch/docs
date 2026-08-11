# torch.Tensor.is_contiguous

Tensor.is_contiguous(*memory_format=torch.contiguous_format*) → [bool](https://docs.python.org/3/library/functions.html#bool)

Returns True if `self` tensor is contiguous in memory in the order specified
by memory format.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - Specifies memory allocation
order. Default: `torch.contiguous_format`.