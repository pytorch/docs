# torch.accelerator.random.initial_seed

torch.accelerator.random.initial_seed(*device=None*, */*)[[source]](https://github.com/pytorch/pytorch/blob/3fadfe4be9707a8a43a23db6e0da32dc1b507694/torch/accelerator/random.py#L7)

Return the initial seed of the default [`torch.Generator`](torch.Generator.html#torch.Generator) for the current [accelerator](../torch.html#accelerators)
on the specified device.

Parameters:

**device** ([`torch.device`](../tensor_attributes.html#torch.device), str, int, optional) - The device to return the initial seed of.
If not given, uses [`torch.accelerator.current_device_index()`](torch.accelerator.current_device_index.html#torch.accelerator.current_device_index) by default.

Returns:

the initial seed of the default generator for the specified device.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

Warning

This function eagerly initializes the accelerator runtime.