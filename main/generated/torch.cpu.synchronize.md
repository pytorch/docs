# torch.cpu.synchronize

torch.cpu.synchronize(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/cpu/__init__.py#L126)

Waits for all kernels in all streams on the CPU device to complete.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - ignored, there's only one CPU device.

N.B. This function only exists to facilitate device-agnostic code.