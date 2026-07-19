# torch.nn.functional.torch.nn.parallel.data_parallel

torch.nn.parallel.data_parallel(*module*, *inputs*, *device_ids=None*, *output_device=None*, *dim=0*, *module_kwargs=None*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/nn/parallel/data_parallel.py#L221)

Evaluate module(input) in parallel across the GPUs given in device_ids.

This is the functional version of the DataParallel module.

Parameters:

- **module** ([*Module*](torch.nn.Module.html#torch.nn.Module)) - the module to evaluate in parallel
- **inputs** ([*Tensor*](../tensors.html#torch.Tensor)) - inputs to the module
- **device_ids** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*of*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*torch.device*](../tensor_attributes.html#torch.device)) - GPU ids on which to replicate module
- **output_device** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*of*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*torch.device*](../tensor_attributes.html#torch.device)) - GPU location of the output Use -1 to indicate the CPU.
(default: device_ids[0])

Returns:

a Tensor containing the result of module(input) located on
output_device

Return type:

[*Tensor*](../tensors.html#torch.Tensor)