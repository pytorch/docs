# torch.cuda.device_count

torch.cuda.device_count()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/cuda/__init__.py#L1208)

Return the number of GPUs available.

Note

This API will NOT poison fork if NVML discovery succeeds.
See [Poison fork in multiprocessing](../notes/multiprocessing.html#multiprocessing-poison-fork-note) for more details.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)