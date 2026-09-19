# torch.cuda.memory.get_per_process_memory_fraction

torch.cuda.memory.get_per_process_memory_fraction(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/b7954b2399da4803024b9a2850e39c588522015f/torch/cuda/memory.py#L202)

Get memory fraction for a process.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - selected device. If it is
`None` the default CUDA device is used.

Returns:

memory fraction, in range 0~1. Allowed memory equals total_memory * fraction.

Return type:

[float](https://docs.python.org/3/builtins/functions.html#float)