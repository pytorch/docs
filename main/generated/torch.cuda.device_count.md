# torch.cuda.device_count

torch.cuda.device_count()[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/cuda/__init__.py#L1312)

Return the number of GPUs available.

Note

This API will NOT poison fork if NVML discovery succeeds.
See [Poison fork in multiprocessing](../notes/multiprocessing.html#multiprocessing-poison-fork-note) for more details.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)