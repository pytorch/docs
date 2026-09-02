# torch.set_rng_state

torch.set_rng_state(*new_state*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/random.py#L27)

Sets the random number generator state.

Note

This function only works for CPU. For CUDA, please use
[`torch.manual_seed()`](torch.manual_seed.html#torch.manual_seed), which works for both CPU and CUDA.

Parameters:

**new_state** (*torch.ByteTensor*) - The desired state