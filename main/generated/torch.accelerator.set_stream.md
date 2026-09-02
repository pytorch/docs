# torch.accelerator.set_stream

torch.accelerator.set_stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/accelerator/__init__.py#L236)

Set the current stream to a given stream.

Parameters:

**stream** ([*torch.Stream*](torch.Stream.html#torch.Stream)) - a given stream that must match the current [accelerator](../torch.html#accelerators) device type.

Note

This function will set the current device index to the device index of the given stream.