# torch.mtia.set_rng_state

torch.mtia.set_rng_state(*new_state*, *device='mtia'*)[[source]](https://github.com/pytorch/pytorch/blob/fbab7cc90f5699714d5785aaa2f153c739435d6f/torch/mtia/__init__.py#L422)

Sets the random number generator state of the specified MTIA device.

Parameters:

- **new_state** (*torch.ByteTensor*) - The desired state
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - The device to set the RNG state.
Default: `'mtia'` (i.e., `torch.device('mtia')`, the current mtia device).