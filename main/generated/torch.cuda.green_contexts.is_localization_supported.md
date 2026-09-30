# torch.cuda.green_contexts.is_localization_supported

torch.cuda.green_contexts.is_localization_supported(*device_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/c96c0d945cc30cd4317ca02911049a75e43972b7/torch/cuda/green_contexts.py#L135)

Return whether the software supports localization on a multi-domain GPU.

Returns `False` when the required software is unavailable or the device
has at most one locality domain. Before driver initialization, attempts a
best-effort NVML capability check based on architecture and system
configuration, raising if NVML cannot determine support. Once the driver
is initialized, queries CUDA directly; invalid devices and failed queries
raise. This function does not initialize the driver or a context and does
not poison subsequent forks. Splitting and context creation always use CUDA
to validate the actual resources.

Parameters:

**device_id** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Device index. Default: current PyTorch device
if PyTorch CUDA is initialized, otherwise `0`.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)