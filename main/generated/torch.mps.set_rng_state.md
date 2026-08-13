# torch.mps.set_rng_state

torch.mps.set_rng_state(*new_state*, *device='mps'*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/mps/__init__.py#L45)

Sets the random number generator state.

Parameters:

- **new_state** (*torch.ByteTensor*) - The desired state
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device to set the RNG state.
Default: `'mps'` (i.e., `torch.device('mps')`, the current MPS device).