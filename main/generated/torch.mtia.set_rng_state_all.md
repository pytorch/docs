# torch.mtia.set_rng_state_all

torch.mtia.set_rng_state_all(*new_states*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/mtia/__init__.py#L447)

Sets the random number generator state of all devices.

Parameters:

**new_states** (*Iterable**of**torch.ByteTensor*) - The desired state for each device.