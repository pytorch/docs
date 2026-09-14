# torch.xpu.memory.memory_snapshot

torch.xpu.memory.memory_snapshot(*mempool_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/b8bd7cf750ea02a2390d8a5440261e2c6ed5ddc7/torch/xpu/memory.py#L260)

Return a snapshot of the XPU memory allocator state across all devices.
Provides detailed information for each memory segment managed by the allocator
including its size, owning pool, associated stream, call stack traces, and other relevant attributes.

Parameters:

**mempool_id** ([*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,*[*int*](https://docs.python.org/3/builtins/functions.html#int)*] or**None**,**optional*) - The memory pool id. If None, the default memory pool is used.

Returns:

List of memory segments and their attributes.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), Any]]