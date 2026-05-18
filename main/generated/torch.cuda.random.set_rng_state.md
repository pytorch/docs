# torch.cuda.random.set_rng_state

torch.cuda.random.set_rng_state(*new_state*, *device='cuda'*)[[source]](https://github.com/pytorch/pytorch/blob/6e3cf2e4280672104341718ea51a55799bb3aca4/torch/cuda/random.py#L51)

Set the random number generator state of the specified GPU.

Parameters:

- **new_state** (*torch.ByteTensor*) - The desired state
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device to set the RNG state.
Default: `'cuda'` (i.e., `torch.device('cuda')`, the current CUDA device).