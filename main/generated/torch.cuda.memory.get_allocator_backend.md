# torch.cuda.memory.get_allocator_backend

torch.cuda.memory.get_allocator_backend()[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/cuda/memory.py#L1406)

Return a string describing the active allocator backend as set by
`PYTORCH_ALLOC_CONF`. Currently available backends are
`native` (PyTorch's native caching allocator) and cudaMallocAsync`
(CUDA's built-in asynchronous allocator).

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for details on choosing the allocator backend.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str)