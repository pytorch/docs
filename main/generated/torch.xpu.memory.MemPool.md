# MemPool

*class*torch.xpu.memory.MemPool(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/ab02f71479d3b0fb41d5b722bbe1943340f2022b/torch/xpu/memory.py#L553)

MemPool represents a pool of memory in a caching allocator. Currently,
it's just the ID of the pool object maintained in the XPUCachingAllocator.

Parameters:

- **allocator** (*torch._C._xpu_XPUAllocator**,**optional*) - a
torch._C._xpu_XPUAllocator object that can be used to
define how memory gets allocated in the pool. If `allocator`
is `None` (default), memory allocation follows the default/
current configuration of the XPUCachingAllocator.
- **use_on_oom** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - a bool that indicates if this pool can be used
as a last resort if a memory allocation outside of the pool fails due
to Out Of Memory. This is `False` by default.

*property*allocator*: _xpu_XPUAllocator | [None](https://docs.python.org/3/library/constants.html#None)*

Returns the allocator this MemPool routes allocations to.

*property*id*: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]*

Returns the ID of this pool as a tuple of two ints.

snapshot()[[source]](https://github.com/pytorch/pytorch/blob/ab02f71479d3b0fb41d5b722bbe1943340f2022b/torch/xpu/memory.py#L589)

Return a snapshot of the XPU memory allocator pool state across all
devices.

Interpreting the output of this function requires familiarity with the
memory allocator internals.

use_count()[[source]](https://github.com/pytorch/pytorch/blob/ab02f71479d3b0fb41d5b722bbe1943340f2022b/torch/xpu/memory.py#L585)

Returns the reference count of this pool.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)