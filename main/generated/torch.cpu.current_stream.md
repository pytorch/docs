# torch.cpu.current_stream

torch.cpu.current_stream(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/08c2d21eeac45d7bb2b95f497938e99c0250222d/torch/cpu/__init__.py#L172)

Returns the currently selected [`Stream`](torch.cpu.Stream_class.html#torch.cpu.Stream) for a given device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Ignored.

Return type:

[*Stream*](torch.cpu.Stream_class.html#torch.cpu.Stream)

N.B. This function only exists to facilitate device-agnostic code