# torch.xpu.set_rng_state

torch.xpu.set_rng_state(*new_state*, *device='xpu'*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/xpu/random.py#L38)

Set the random number generator state of the specified GPU.

Parameters:

- **new_state** (*torch.ByteTensor*) - The desired state
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device to set the RNG state.
Default: `'xpu'` (i.e., `torch.device('xpu')`, the current XPU device).