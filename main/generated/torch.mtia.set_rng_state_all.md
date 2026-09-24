# torch.mtia.set_rng_state_all

torch.mtia.set_rng_state_all(*new_states*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/mtia/__init__.py#L447)

Sets the random number generator state of all devices.

Parameters:

**new_states** (*Iterable**of**torch.ByteTensor*) - The desired state for each device.