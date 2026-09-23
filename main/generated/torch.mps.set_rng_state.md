# torch.mps.set_rng_state

torch.mps.set_rng_state(*new_state*, *device='mps'*)[[source]](https://github.com/pytorch/pytorch/blob/8d6343a7cd80821d54ba546bc6f799aad9ccb79c/torch/mps/__init__.py#L45)

Sets the random number generator state.

Parameters:

- **new_state** (*torch.ByteTensor*) - The desired state
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - The device to set the RNG state.
Default: `'mps'` (i.e., `torch.device('mps')`, the current MPS device).