# torch.xpu.device_count

torch.xpu.device_count()[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/xpu/__init__.py#L262)

Return the number of XPU device available.

Note

This API will NOT poison fork if Level Zero Sysman discovery succeeds.
See [Poison fork in multiprocessing](../notes/multiprocessing.html#multiprocessing-poison-fork-note) for more details.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)