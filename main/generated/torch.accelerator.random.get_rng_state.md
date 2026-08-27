# torch.accelerator.random.get_rng_state

torch.accelerator.random.get_rng_state(*device=None*, */*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/accelerator/random.py#L26)

Return the RNG state of the default [`torch.Generator`](torch.Generator.html#torch.Generator) for the current [accelerator](../torch.html#accelerators)
as a torch.Tensor of dtype torch.uint8 for the specified accelerator device.

Parameters:

**device** ([`torch.device`](../tensor_attributes.html#torch.device), str, int, optional) - The device to return the RNG state of.
If not given, uses [`torch.accelerator.current_device_index()`](torch.accelerator.current_device_index.html#torch.accelerator.current_device_index) by default.

Returns:

the RNG state of the default generator for the specified device.

Return type:

[torch.Tensor](../tensors.html#torch.Tensor)

Warning

This function eagerly initializes the accelerator runtime.