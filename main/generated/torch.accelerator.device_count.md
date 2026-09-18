# torch.accelerator.device_count

torch.accelerator.device_count()[[source]](https://github.com/pytorch/pytorch/blob/0c8b4a78ffbbce776adc0823e790158b26435f40/torch/accelerator/__init__.py#L56)

Return the number of current [accelerator](../torch.html#accelerators) available.

Returns:

the number of the current [accelerator](../torch.html#accelerators) available.

If there are no available accelerators, return 0.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)

Note

This API delegates to the device-specific version of device_count.
On CUDA, this API will NOT poison fork if NVML discovery succeeds.
Otherwise, it will. For more details, see [Poison fork in multiprocessing](../notes/multiprocessing.html#multiprocessing-poison-fork-note).