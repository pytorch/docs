# torch.xpu.set_device

torch.xpu.set_device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/xpu/__init__.py#L466)

Set the current device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - selected device. This function is a
no-op if this argument is negative.