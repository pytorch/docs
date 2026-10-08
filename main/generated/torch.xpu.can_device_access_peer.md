# torch.xpu.can_device_access_peer

torch.xpu.can_device_access_peer(*device*, *peer*)[[source]](https://github.com/pytorch/pytorch/blob/5ba7f2bf58f6177091cdf890429ffd5f5dc2139a/torch/xpu/__init__.py#L546)

Query whether a device can access a peer device's memory.

Parameters:

- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - selected device.
- **peer** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - peer device to query access to.

Returns:

`True` if `device` can access `peer`, `False` otherwise.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)