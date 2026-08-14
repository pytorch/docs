# torch.xpu.set_rng_state

torch.xpu.set_rng_state(*new_state*, *device='xpu'*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/xpu/random.py#L38)

Set the random number generator state of the specified GPU.

Parameters:

- **new_state** (*torch.ByteTensor*) - The desired state
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device to set the RNG state.
Default: `'xpu'` (i.e., `torch.device('xpu')`, the current XPU device).