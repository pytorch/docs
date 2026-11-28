# torch.cuda.device_count

torch.cuda.device_count()[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/cuda/__init__.py#L1316)

Return the number of GPUs available.

Note

This API will NOT poison fork if NVML discovery succeeds.
See [Poison fork in multiprocessing](../notes/multiprocessing.html#multiprocessing-poison-fork-note) for more details.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)