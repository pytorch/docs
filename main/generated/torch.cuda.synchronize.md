# torch.cuda.synchronize

torch.cuda.synchronize(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/cuda/__init__.py#L1267)

Wait for all kernels in all streams on a CUDA device to complete.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - device for which to synchronize.
It uses the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if [`device`](torch.cuda.device.html#torch.cuda.device) is `None` (default).