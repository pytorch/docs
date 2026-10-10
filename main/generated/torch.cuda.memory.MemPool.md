# MemPool

*class*torch.cuda.memory.MemPool(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/1b51ed6169475ed863f4ee43b7eaa52ecda0f862/torch/cuda/memory.py#L1691)

MemPool represents a pool of memory in a caching allocator. Currently,
it's just the ID of the pool object maintained in the CUDACachingAllocator.

Parameters:

- **allocator** (*torch._C._cuda_CUDAAllocator**,**optional*) - a
torch._C._cuda_CUDAAllocator object that can be used to
define how memory gets allocated in the pool. If `allocator`
is `None` (default), memory allocation follows the default/
current configuration of the CUDACachingAllocator.
- **use_on_oom** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - a bool that indicates if this pool can be used
as a last resort if a memory allocation outside of the pool fails due
to Out Of Memory. This is False by default.
- **no_split** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - a bool that indicates if this pool should not split a segment.
This is False by default.

*classmethod*from_py_allocator(*alloc_fn*, *free_fn*, ***, *use_on_oom=False*, *no_split=False*)[[source]](https://github.com/pytorch/pytorch/blob/1b51ed6169475ed863f4ee43b7eaa52ecda0f862/torch/cuda/memory.py#L1717)

Create a MemPool backed by Python allocation callbacks.

`alloc_fn(size)` allocates a backing segment and returns its device
address as an integer. Return `None` or zero if the allocation cannot
be satisfied. `free_fn(ptr, size)` releases a segment, where `size`
is the backing segment's size. PyTorch makes the segment's device and
allocation stream current while each callback runs.

Parameters:

- **alloc_fn** ([*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*[**[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*]**,*[*int*](https://docs.python.org/3/builtins/functions.html#int)*|**None**]*) - Callable that allocates a segment.
- **free_fn** ([*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*[**[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,*[*int*](https://docs.python.org/3/builtins/functions.html#int)*]**,**None**]*) - Callable that frees a segment and receives its device
address and backing segment size.
- **use_on_oom** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - Whether allocations outside this pool may borrow its
cached blocks as a last resort. Defaults to `False`.
- **no_split** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - Whether the caching allocator should avoid splitting this
pool's segments. Defaults to `False`.

Return type:

*MemPool*

See [Python-defined CUDA allocators](../notes/cuda.html#cuda-memory-python-allocators) for callback requirements and
examples.

*property*id*: [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), [int](https://docs.python.org/3/builtins/functions.html#int)]*

Returns the ID of this pool as a tuple of two ints.

snapshot(*include_traces=True*)[[source]](https://github.com/pytorch/pytorch/blob/1b51ed6169475ed863f4ee43b7eaa52ecda0f862/torch/cuda/memory.py#L1758)

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

use_count()[[source]](https://github.com/pytorch/pytorch/blob/1b51ed6169475ed863f4ee43b7eaa52ecda0f862/torch/cuda/memory.py#L1754)

Returns the reference count of this pool.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)