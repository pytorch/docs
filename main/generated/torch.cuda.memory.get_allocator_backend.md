# torch.cuda.memory.get_allocator_backend

torch.cuda.memory.get_allocator_backend()[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cuda/memory.py#L1289)

Return a string describing the active allocator backend as set by
`PYTORCH_ALLOC_CONF`. Currently available backends are
`native` (PyTorch's native caching allocator) and cudaMallocAsync`
(CUDA's built-in asynchronous allocator).

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for details on choosing the allocator backend.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)