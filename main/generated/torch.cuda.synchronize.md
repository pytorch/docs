# torch.cuda.synchronize

torch.cuda.synchronize(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/cuda/__init__.py#L1332)

Wait for all kernels in all streams on a CUDA device to complete.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - device for which to synchronize.
It uses the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if [`device`](torch.cuda.device.html#torch.cuda.device) is `None` (default).