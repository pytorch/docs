# torch.mtia.default_stream

torch.mtia.default_stream(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/mtia/__init__.py#L193)

Return the default [`Stream`](torch.mtia.Stream_class.html#torch.mtia.Stream) for a given device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Returns
the default [`Stream`](torch.mtia.Stream_class.html#torch.mtia.Stream) for the current device, given by
[`current_device()`](torch.mtia.current_device.html#torch.mtia.current_device), if [`device`](torch.mtia.device.html#torch.mtia.device) is `None`
(default).

Return type:

[*Stream*](torch.Stream.html#torch.Stream)