# torch.xpu.random.set_rng_state_all

torch.xpu.random.set_rng_state_all(*new_states*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/xpu/random.py#L65)

Set the random number generator state of all devices.

Parameters:

**new_states** (*Iterable**of**torch.ByteTensor*) - The desired state for each device.