# XPUPluggableAllocator

*class*torch.xpu.memory.XPUPluggableAllocator(*path_to_lib_file*, *alloc_fn_name*, *free_fn_name*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/xpu/memory.py#L490)

XPU memory allocator loaded dynamically from a shared library.

This lets users provide custom allocation and free functions implemented
in a separate shared library. The allocator is registered and could become
available for use via [`change_current_allocator()`](torch.xpu.memory.change_current_allocator.html#torch.xpu.memory.change_current_allocator).

Parameters:

- **path_to_lib_file** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Filesystem path to the shared library file containing the allocation
and free functions.
- **alloc_fn_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) -

Name of the allocation function exported from the shared library.
The function must have the signature:

> `void* alloc_fn(size_t size, int device, sycl::queue* queue);`
- **free_fn_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) -

Name of the free function exported from the shared library.
The function must have the signature:

> `void free_fn(void* ptr, size_t size, int device, sycl::queue* queue);`