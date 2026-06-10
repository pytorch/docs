# torch.set_rng_state

torch.set_rng_state(*new_state*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/random.py#L27)

Sets the random number generator state.

Note

This function only works for CPU. For CUDA, please use
[`torch.manual_seed()`](torch.manual_seed.html#torch.manual_seed), which works for both CPU and CUDA.

Parameters:

**new_state** (*torch.ByteTensor*) - The desired state