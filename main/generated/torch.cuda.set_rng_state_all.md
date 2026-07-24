# torch.cuda.set_rng_state_all

torch.cuda.set_rng_state_all(*new_states*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/cuda/random.py#L79)

Set the random number generator state of all devices.

Parameters:

**new_states** (*Iterable**of**torch.ByteTensor*) - The desired state for each device.