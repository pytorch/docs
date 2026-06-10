# torch.xpu.device_count

torch.xpu.device_count()[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/xpu/__init__.py#L262)

Return the number of XPU device available.

Note

This API will NOT poison fork if Level Zero Sysman discovery succeeds.
See [Poison fork in multiprocessing](../notes/multiprocessing.html#multiprocessing-poison-fork-note) for more details.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)