# torch.mtia.set_rng_state_all

torch.mtia.set_rng_state_all(*new_states*)[[source]](https://github.com/pytorch/pytorch/blob/09c9b1ec9c2e88520d11a9c64b206359e8ca912b/torch/mtia/__init__.py#L447)

Sets the random number generator state of all devices.

Parameters:

**new_states** (*Iterable**of**torch.ByteTensor*) - The desired state for each device.