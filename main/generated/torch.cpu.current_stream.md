# torch.cpu.current_stream

torch.cpu.current_stream(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/cpu/__init__.py#L172)

Returns the currently selected [`Stream`](torch.cpu.Stream_class.html#torch.cpu.Stream) for a given device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Ignored.

Return type:

[*Stream*](torch.cpu.Stream_class.html#torch.cpu.Stream)

N.B. This function only exists to facilitate device-agnostic code