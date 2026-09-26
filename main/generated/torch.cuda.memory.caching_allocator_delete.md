# torch.cuda.memory.caching_allocator_delete

torch.cuda.memory.caching_allocator_delete(*mem_ptr*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/cuda/memory.py#L140)

Delete memory allocated using the CUDA memory allocator.

Memory allocated with `caching_allocator_alloc()`.
is freed here. The associated device and stream are tracked inside
the allocator.

Parameters:

**mem_ptr** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - memory address to be freed by the allocator.

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for more details about GPU memory
management.