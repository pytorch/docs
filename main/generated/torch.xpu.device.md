# device

*class*torch.xpu.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/2dc676a67d91491beadb4615ae9fe15e144086ea/torch/xpu/__init__.py#L393)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.