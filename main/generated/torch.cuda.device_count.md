# torch.cuda.device_count

torch.cuda.device_count()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/cuda/__init__.py#L1224)

Return the number of GPUs available.

Note

This API will NOT poison fork if NVML discovery succeeds.
See [Poison fork in multiprocessing](../notes/multiprocessing.html#multiprocessing-poison-fork-note) for more details.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)