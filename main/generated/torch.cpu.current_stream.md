# torch.cpu.current_stream

torch.cpu.current_stream(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/cpu/__init__.py#L172)

Returns the currently selected [`Stream`](torch.cpu.Stream_class.html#torch.cpu.Stream) for a given device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Ignored.

Return type:

[*Stream*](torch.cpu.Stream_class.html#torch.cpu.Stream)

N.B. This function only exists to facilitate device-agnostic code