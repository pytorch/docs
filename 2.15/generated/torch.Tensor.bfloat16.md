# torch.Tensor.bfloat16

Tensor.bfloat16(*memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

`self.bfloat16()` is equivalent to `self.to(torch.bfloat16)`. See [`to()`](torch.Tensor.to.html#torch.Tensor.to).

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.