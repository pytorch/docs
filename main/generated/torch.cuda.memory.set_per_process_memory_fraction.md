# torch.cuda.memory.set_per_process_memory_fraction

torch.cuda.memory.set_per_process_memory_fraction(*fraction*, *device=None*)[[source]](https://github.com/pytorch/pytorch/blob/9179f2014ca7f941551131fc2315cfcf9e206bd3/torch/cuda/memory.py#L174)

Set memory fraction for a process.

The fraction is used to limit an caching allocator to allocated memory on a CUDA device.
The allowed value equals the total visible memory multiplied fraction.
If trying to allocate more than the allowed value in a process, will raise an out of
memory error in allocator.

Parameters:

- **fraction** ([*float*](https://docs.python.org/3/library/functions.html#float)) - Range: 0~1. Allowed memory equals total_memory * fraction.
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. If it is
`None` the default CUDA device is used.

Note

In general, the total available free memory is less than the total capacity.