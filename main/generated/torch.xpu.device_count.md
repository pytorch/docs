# torch.xpu.device_count

torch.xpu.device_count()[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/xpu/__init__.py#L297)

Return the number of XPU device available.

Note

This API will NOT poison fork if Level Zero Sysman discovery succeeds.
See [Poison fork in multiprocessing](../notes/multiprocessing.html#multiprocessing-poison-fork-note) for more details.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)