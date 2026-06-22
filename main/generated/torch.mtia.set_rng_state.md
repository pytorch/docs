# torch.mtia.set_rng_state

torch.mtia.set_rng_state(*new_state*, *device='mtia'*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/mtia/__init__.py#L422)

Sets the random number generator state of the specified MTIA device.

Parameters:

- **new_state** (*torch.ByteTensor*) - The desired state
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device to set the RNG state.
Default: `'mtia'` (i.e., `torch.device('mtia')`, the current mtia device).