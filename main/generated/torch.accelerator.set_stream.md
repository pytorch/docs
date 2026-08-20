# torch.accelerator.set_stream

torch.accelerator.set_stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/accelerator/__init__.py#L236)

Set the current stream to a given stream.

Parameters:

**stream** ([*torch.Stream*](torch.Stream.html#torch.Stream)) - a given stream that must match the current [accelerator](../torch.html#accelerators) device type.

Note

This function will set the current device index to the device index of the given stream.