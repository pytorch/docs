# torch.mtia.set_rng_state_all

torch.mtia.set_rng_state_all(*new_states*)[[source]](https://github.com/pytorch/pytorch/blob/1b51ed6169475ed863f4ee43b7eaa52ecda0f862/torch/mtia/__init__.py#L447)

Sets the random number generator state of all devices.

Parameters:

**new_states** (*Iterable**of**torch.ByteTensor*) - The desired state for each device.