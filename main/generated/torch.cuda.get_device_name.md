# torch.cuda.get_device_name

torch.cuda.get_device_name(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/55f1d787eeab8196db1c529de1754add16feec18/torch/cuda/__init__.py#L815)

Get the name of a device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**optional*) - device for which to return the
name. This function is a no-op if this argument is a negative
integer. It uses the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if [`device`](torch.cuda.device.html#torch.cuda.device) is `None` (default).

Returns:

the name of the device

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str)