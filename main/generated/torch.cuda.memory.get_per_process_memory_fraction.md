# torch.cuda.memory.get_per_process_memory_fraction

torch.cuda.memory.get_per_process_memory_fraction(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/c9b5004c45376c912422325d032b2d74b4828d5c/torch/cuda/memory.py#L206)

Get memory fraction for a process.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - selected device. If it is
`None` the default CUDA device is used.

Returns:

memory fraction, in range 0~1. Allowed memory equals total_memory * fraction.

Return type:

[float](https://docs.python.org/3/builtins/functions.html#float)