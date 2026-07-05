# torch.cuda.default_stream

torch.cuda.default_stream(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/cuda/__init__.py#L1273)

Return the default [`Stream`](torch.cuda.Stream_class.html#torch.cuda.Stream) for a given device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Returns
the default [`Stream`](torch.cuda.Stream_class.html#torch.cuda.Stream) for the current device, given by
[`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device), if [`device`](torch.cuda.device.html#torch.cuda.device) is `None`
(default).

Return type:

[*Stream*](torch.cuda.streams.Stream.html#torch.cuda.streams.Stream)