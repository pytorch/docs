# torch.accelerator.device_count

torch.accelerator.device_count()[[source]](https://github.com/pytorch/pytorch/blob/8ab13d788b9dab3e338e618576e65bb8b0c75e1a/torch/accelerator/__init__.py#L56)

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