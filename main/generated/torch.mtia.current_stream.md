# torch.mtia.current_stream

torch.mtia.current_stream(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/63f903c3d6b04c7cb1433d1d67e2b8e21c055bc7/torch/mtia/__init__.py#L180)

Return the currently selected [`Stream`](torch.mtia.Stream_class.html#torch.mtia.Stream) for a given device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Returns
the currently selected [`Stream`](torch.mtia.Stream_class.html#torch.mtia.Stream) for the current device, given
by [`current_device()`](torch.mtia.current_device.html#torch.mtia.current_device), if [`device`](torch.mtia.device.html#torch.mtia.device) is `None`
(default).

Return type:

[*Stream*](torch.Stream.html#torch.Stream)