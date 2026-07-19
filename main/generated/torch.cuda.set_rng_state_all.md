# torch.cuda.set_rng_state_all

torch.cuda.set_rng_state_all(*new_states*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/cuda/random.py#L79)

Set the random number generator state of all devices.

Parameters:

**new_states** (*Iterable**of**torch.ByteTensor*) - The desired state for each device.