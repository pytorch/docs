# torch.cuda.memory.get_allocator_backend

torch.cuda.memory.get_allocator_backend()[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/cuda/memory.py#L1391)

Return a string describing the active allocator backend as set by
`PYTORCH_ALLOC_CONF`. Currently available backends are
`native` (PyTorch's native caching allocator) and cudaMallocAsync`
(CUDA's built-in asynchronous allocator).

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for details on choosing the allocator backend.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str)