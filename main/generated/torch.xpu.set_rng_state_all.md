# torch.xpu.set_rng_state_all

torch.xpu.set_rng_state_all(*new_states*)[[source]](https://github.com/pytorch/pytorch/blob/be79392a0cedbbc0b5d2d3288173316425f90af4/torch/xpu/random.py#L65)

Set the random number generator state of all devices.

Parameters:

**new_states** (*Iterable**of**torch.ByteTensor*) - The desired state for each device.