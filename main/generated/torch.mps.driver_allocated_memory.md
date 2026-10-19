# torch.mps.driver_allocated_memory

torch.mps.driver_allocated_memory()[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/mps/__init__.py#L120)

Returns total GPU memory allocated by Metal driver for the process in bytes.

Note

The returned size includes cached allocations in MPSAllocator pools
as well as allocations from MPS/MPSGraph frameworks.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)