# torch.cuda.synchronize

torch.cuda.synchronize(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/cuda/__init__.py#L1375)

Wait for all kernels in all streams on a CUDA device to complete.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - device for which to synchronize.
It uses the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if [`device`](torch.cuda.device.html#torch.cuda.device) is `None` (default).