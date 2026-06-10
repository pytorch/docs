# torch.accelerator.set_stream

torch.accelerator.set_stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/accelerator/__init__.py#L235)

Set the current stream to a given stream.

Parameters:

**stream** ([*torch.Stream*](torch.Stream.html#torch.Stream)) - a given stream that must match the current [accelerator](../torch.html#accelerators) device type.

Note

This function will set the current device index to the device index of the given stream.