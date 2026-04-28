# torch.Tensor.xpu

Tensor.xpu(*device=None*, *non_blocking=False*, *memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

Returns a copy of this object in XPU memory.

If this object is already in XPU memory and on the correct device,
then no copy is performed and the original object is returned.

Parameters:

- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - The destination XPU device.
Defaults to the current XPU device.
- **non_blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `True` and the source is in pinned memory,
the copy will be asynchronous with respect to the host.
Otherwise, the argument has no effect. Default: `False`.
- **memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.