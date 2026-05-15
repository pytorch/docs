# torch.cuda.get_device_capability

torch.cuda.get_device_capability(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/cuda/__init__.py#L703)

Get the cuda capability of a device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - device for which to return the
device capability. This function is a no-op if this argument is
a negative integer. It uses the current device, given by
[`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device), if [`device`](torch.cuda.device.html#torch.cuda.device) is `None`
(default).

Returns:

the major and minor cuda capability of the device

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)([int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int))