# torch.xpu.random.set_rng_state_all

torch.xpu.random.set_rng_state_all(*new_states*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/xpu/random.py#L65)

Set the random number generator state of all devices.

Parameters:

**new_states** (*Iterable**of**torch.ByteTensor*) - The desired state for each device.