# torch.xpu.device_count

torch.xpu.device_count()[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/xpu/__init__.py#L256)

Return the number of XPU device available.

Note

This API will NOT poison fork if Level Zero Sysman discovery succeeds.
See [Poison fork in multiprocessing](../notes/multiprocessing.html#multiprocessing-poison-fork-note) for more details.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)