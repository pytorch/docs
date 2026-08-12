# MemPool

*class*torch.cuda.memory.MemPool(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/cuda/memory.py#L1368)

MemPool represents a pool of memory in a caching allocator. Currently,
it's just the ID of the pool object maintained in the CUDACachingAllocator.

Parameters:

- **allocator** (*torch._C._cuda_CUDAAllocator**,**optional*) - a
torch._C._cuda_CUDAAllocator object that can be used to
define how memory gets allocated in the pool. If `allocator`
is `None` (default), memory allocation follows the default/
current configuration of the CUDACachingAllocator.
- **use_on_oom** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - a bool that indicates if this pool can be used
as a last resort if a memory allocation outside of the pool fails due
to Out Of Memory. This is False by default.
- **no_split** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - a bool that indicates if this pool should not split a segment.
This is False by default.

*property*id*: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]*

Returns the ID of this pool as a tuple of two ints.

snapshot(*include_traces=True*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/cuda/memory.py#L1403)

Return a snapshot of the CUDA memory allocator pool state across all
devices.

Interpreting the output of this function requires familiarity with the
memory allocator internals.

Parameters:

**include_traces** - Whether to include trace entries in the snapshot.
If True (default), all trace entries are included.
If False, no trace entries are included (lightweight/fast snapshot).

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for more details about GPU memory
management.

use_count()[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/cuda/memory.py#L1399)

Returns the reference count of this pool.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)