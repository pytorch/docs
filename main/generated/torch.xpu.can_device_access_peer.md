# torch.xpu.can_device_access_peer

torch.xpu.can_device_access_peer(*device*, *peer*)[[source]](https://github.com/pytorch/pytorch/blob/e5aa1320b162fc3b9d0d53207fe340a6d3aa03d1/torch/xpu/__init__.py#L548)

Query whether a device can access a peer device's memory.

Parameters:

- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)) - selected device.
- **peer** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)) - peer device to query access to.

Returns:

`True` if `device` can access `peer`, `False` otherwise.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)