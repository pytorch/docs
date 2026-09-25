# torch.accelerator.random.initial_seed

torch.accelerator.random.initial_seed(*device=None*, */*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/accelerator/random.py#L8)

Return the initial seed of the default [`torch.Generator`](torch.Generator.html#torch.Generator) for the current [accelerator](../torch.html#accelerators)
on the specified device.

Parameters:

**device** ([`torch.device`](../tensor_attributes.html#torch.device), str, int, optional) - The device to return the initial seed of.
If not given, uses [`torch.accelerator.current_device_index()`](torch.accelerator.current_device_index.html#torch.accelerator.current_device_index) by default.

Returns:

the initial seed of the default generator for the specified device.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)

Warning

This function eagerly initializes the accelerator runtime.