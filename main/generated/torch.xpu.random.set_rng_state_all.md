# torch.xpu.random.set_rng_state_all

torch.xpu.random.set_rng_state_all(*new_states*)[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/xpu/random.py#L65)

Set the random number generator state of all devices.

Parameters:

**new_states** (*Iterable**of**torch.ByteTensor*) - The desired state for each device.