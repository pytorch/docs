# torch.xpu.current_stream

torch.xpu.current_stream(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/xpu/__init__.py#L676)

Return the currently selected [`Stream`](torch.xpu.Stream_class.html#torch.xpu.Stream) for a given device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - selected device. Returns
the currently selected [`Stream`](torch.xpu.Stream_class.html#torch.xpu.Stream) for the current device, given
by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device), if [`device`](torch.xpu.device.html#torch.xpu.device) is `None`
(default).

Return type:

[Stream](torch.xpu.Stream_class.html#torch.xpu.Stream)