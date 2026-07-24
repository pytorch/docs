# torch.cuda.memory.get_allocator_backend

torch.cuda.memory.get_allocator_backend()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/cuda/memory.py#L1298)

Return a string describing the active allocator backend as set by
`PYTORCH_ALLOC_CONF`. Currently available backends are
`native` (PyTorch's native caching allocator) and cudaMallocAsync`
(CUDA's built-in asynchronous allocator).

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for details on choosing the allocator backend.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)