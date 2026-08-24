# torch.xpu.memory.memory_snapshot

torch.xpu.memory.memory_snapshot(*mempool_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/xpu/memory.py#L260)

Return a snapshot of the XPU memory allocator state across all devices.
Provides detailed information for each memory segment managed by the allocator
including its size, owning pool, associated stream, call stack traces, and other relevant attributes.

Parameters:

**mempool_id** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*] or**None**,**optional*) - The memory pool id. If None, the default memory pool is used.

Returns:

List of memory segments and their attributes.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Any]]