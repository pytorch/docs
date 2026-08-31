# torch.cuda.current_stream

torch.cuda.current_stream(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/c9fded8194d3b089ed610b586eb746a6e74c6616/torch/cuda/__init__.py#L1309)

Return the currently selected [`Stream`](torch.cuda.Stream_class.html#torch.cuda.Stream) for a given device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Returns
the currently selected [`Stream`](torch.cuda.Stream_class.html#torch.cuda.Stream) for the current device, given
by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device), if [`device`](torch.cuda.device.html#torch.cuda.device) is `None`
(default).

Return type:

[*Stream*](torch.cuda.streams.Stream.html#torch.cuda.streams.Stream)