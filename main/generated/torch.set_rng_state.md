# torch.set_rng_state

torch.set_rng_state(*new_state*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/random.py#L27)

Sets the random number generator state.

Note

This function only works for CPU. For CUDA, please use
[`torch.manual_seed()`](torch.manual_seed.html#torch.manual_seed), which works for both CPU and CUDA.

Parameters:

**new_state** (*torch.ByteTensor*) - The desired state