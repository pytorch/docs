# torch.mps.get_rng_state

torch.mps.get_rng_state(*device='mps'*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/mps/__init__.py#L35)

Returns the random number generator state as a ByteTensor.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device to return the RNG state of.
Default: `'mps'` (i.e., `torch.device('mps')`, the current MPS device).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)