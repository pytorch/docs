# torch.cuda.memory.caching_allocator_delete

torch.cuda.memory.caching_allocator_delete(*mem_ptr*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/cuda/memory.py#L144)

Delete memory allocated using the CUDA memory allocator.

Memory allocated with `caching_allocator_alloc()`.
is freed here. The associated device and stream are tracked inside
the allocator.

Parameters:

**mem_ptr** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - memory address to be freed by the allocator.

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for more details about GPU memory
management.