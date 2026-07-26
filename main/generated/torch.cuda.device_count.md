# torch.cuda.device_count

torch.cuda.device_count()[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/cuda/__init__.py#L1208)

Return the number of GPUs available.

Note

This API will NOT poison fork if NVML discovery succeeds.
See [Poison fork in multiprocessing](../notes/multiprocessing.html#multiprocessing-poison-fork-note) for more details.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)