# torch.cuda.memory.get_allocator_backend

torch.cuda.memory.get_allocator_backend()[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/cuda/memory.py#L1201)

Return a string describing the active allocator backend as set by
`PYTORCH_ALLOC_CONF`. Currently available backends are
`native` (PyTorch's native caching allocator) and cudaMallocAsync`
(CUDA's built-in asynchronous allocator).

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for details on choosing the allocator backend.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)