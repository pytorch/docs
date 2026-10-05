# torch.Tensor.byte

Tensor.byte(*memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

`self.byte()` is equivalent to `self.to(torch.uint8)`. See [`to()`](torch.Tensor.to.html#torch.Tensor.to).

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.