# torch.cuda.set_rng_state

torch.cuda.set_rng_state(*new_state*, *device='cuda'*)[[source]](https://github.com/pytorch/pytorch/blob/e5aa1320b162fc3b9d0d53207fe340a6d3aa03d1/torch/cuda/random.py#L51)

Set the random number generator state of the specified GPU.

Parameters:

- **new_state** (*torch.ByteTensor*) - The desired state
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device to set the RNG state.
Default: `'cuda'` (i.e., `torch.device('cuda')`, the current CUDA device).