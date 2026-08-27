# torch.xpu.random.set_rng_state

torch.xpu.random.set_rng_state(*new_state*, *device='xpu'*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/xpu/random.py#L38)

Set the random number generator state of the specified GPU.

Parameters:

- **new_state** (*torch.ByteTensor*) - The desired state
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device to set the RNG state.
Default: `'xpu'` (i.e., `torch.device('xpu')`, the current XPU device).