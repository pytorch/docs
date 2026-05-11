# torch.xpu.set_device

torch.xpu.set_device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/xpu/__init__.py#L424)

Set the current device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)) - selected device. This function is a
no-op if this argument is negative.