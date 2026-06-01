# torch.cuda.get_device_properties

torch.cuda.get_device_properties(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/5cd392bfe432d57e7beb9ab67037ddc0fcc01205/torch/cuda/__init__.py#L721)

Get the properties of a device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - device for which to return the
properties of the device. It uses the current device, given by
[`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device), if [`device`](torch.cuda.device.html#torch.cuda.device) is `None`
(default).

Returns:

the properties of the device

Return type:

_CudaDeviceProperties