# torch.mps.get_rng_state

torch.mps.get_rng_state(*device='mps'*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/mps/__init__.py#L35)

Returns the random number generator state as a ByteTensor.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - The device to return the RNG state of.
Default: `'mps'` (i.e., `torch.device('mps')`, the current MPS device).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)