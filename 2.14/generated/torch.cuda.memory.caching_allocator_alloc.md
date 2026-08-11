# torch.cuda.memory.caching_allocator_alloc

torch.cuda.memory.caching_allocator_alloc(*size*, *device=None*, *stream=None*)[[source]](https://github.com/pytorch/pytorch/blob/v2.14.0/torch/cuda/memory.py#L103)

Perform a memory allocation using the CUDA memory allocator.

Memory is allocated for a given device and a stream, this
function is intended to be used for interoperability with other
frameworks. Allocated memory is released through
`caching_allocator_delete()`.

Parameters:

- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - number of bytes to be allocated.
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. If it is
`None` the default CUDA device is used.
- **stream** ([*torch.cuda.Stream*](torch.cuda.Stream_class.html#torch.cuda.Stream)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected stream. If is `None` then
the default stream for the selected device is used.

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for more details about GPU memory
management.