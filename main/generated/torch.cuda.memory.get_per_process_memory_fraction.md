# torch.cuda.memory.get_per_process_memory_fraction

torch.cuda.memory.get_per_process_memory_fraction(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/cuda/memory.py#L206)

Get memory fraction for a process.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - selected device. If it is
`None` the default CUDA device is used.

Returns:

memory fraction, in range 0~1. Allowed memory equals total_memory * fraction.

Return type:

[float](https://docs.python.org/3/builtins/functions.html#float)