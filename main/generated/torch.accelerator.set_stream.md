# torch.accelerator.set_stream

torch.accelerator.set_stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/accelerator/__init__.py#L236)

Set the current stream to a given stream.

Parameters:

**stream** ([*torch.Stream*](torch.Stream.html#torch.Stream)) - a given stream that must match the current [accelerator](../torch.html#accelerators) device type.

Note

This function will set the current device index to the device index of the given stream.