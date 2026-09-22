# MemPool

*class*torch.xpu.memory.MemPool(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/9d784735eb70fb8b0335b0ad7cad9db3ea4babbd/torch/xpu/memory.py#L553)

MemPool represents a pool of memory in a caching allocator. Currently,
it's just the ID of the pool object maintained in the XPUCachingAllocator.

Parameters:

- **allocator** (*torch._C._xpu_XPUAllocator**,**optional*) - a
torch._C._xpu_XPUAllocator object that can be used to
define how memory gets allocated in the pool. If `allocator`
is `None` (default), memory allocation follows the default/
current configuration of the XPUCachingAllocator.
- **use_on_oom** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*,**optional*) - a bool that indicates if this pool may be used as a last
resort when an allocation outside the pool fails with OOM.
Defaults to `False`.
- **no_split** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*,**optional*) - if `True`, cached segments in this pool are
never split to serve smaller allocations. Defaults to `False`.

*property*id*: [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), [int](https://docs.python.org/3/builtins/functions.html#int)]*

Returns the ID of this pool as a tuple of two ints.

snapshot()[[source]](https://github.com/pytorch/pytorch/blob/9d784735eb70fb8b0335b0ad7cad9db3ea4babbd/torch/xpu/memory.py#L588)

Return a snapshot of the XPU memory allocator pool state across all
devices.

Interpreting the output of this function requires familiarity with the
memory allocator internals.

use_count()[[source]](https://github.com/pytorch/pytorch/blob/9d784735eb70fb8b0335b0ad7cad9db3ea4babbd/torch/xpu/memory.py#L584)

Returns the reference count of this pool.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)