# torch.mps.driver_allocated_memory

torch.mps.driver_allocated_memory()[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/mps/__init__.py#L120)

Returns total GPU memory allocated by Metal driver for the process in bytes.

Note

The returned size includes cached allocations in MPSAllocator pools
as well as allocations from MPS/MPSGraph frameworks.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)