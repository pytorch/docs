# torch.cuda.random.set_rng_state_all

torch.cuda.random.set_rng_state_all(*new_states*)[[source]](https://github.com/pytorch/pytorch/blob/3565a492def04bf126af9d46958533d16fb88274/torch/cuda/random.py#L79)

Set the random number generator state of all devices.

Parameters:

**new_states** (*Iterable**of**torch.ByteTensor*) - The desired state for each device.