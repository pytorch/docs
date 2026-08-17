# torch.mtia.set_rng_state_all

torch.mtia.set_rng_state_all(*new_states*)[[source]](https://github.com/pytorch/pytorch/blob/99fcf9fd884002c14d4c19cce5dfe2469ba5a7fc/torch/mtia/__init__.py#L447)

Sets the random number generator state of all devices.

Parameters:

**new_states** (*Iterable**of**torch.ByteTensor*) - The desired state for each device.