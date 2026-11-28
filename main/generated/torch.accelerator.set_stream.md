# torch.accelerator.set_stream

torch.accelerator.set_stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/accelerator/__init__.py#L237)

Set the current stream to a given stream.

Parameters:

**stream** ([*torch.Stream*](torch.Stream.html#torch.Stream)) - a given stream that must match the current [accelerator](../torch.html#accelerators) device type.

Note

This function will set the current device index to the device index of the given stream.