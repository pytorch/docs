# torch.xpu.can_device_access_peer

torch.xpu.can_device_access_peer(*device*, *peer*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/xpu/__init__.py#L549)

Query whether a device can access a peer device's memory.

Parameters:

- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)) - selected device.
- **peer** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)) - peer device to query access to.

Returns:

`True` if `device` can access `peer`, `False` otherwise.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)