# torch.set_rng_state

torch.set_rng_state(*new_state*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/random.py#L27)

Sets the random number generator state.

Note

This function only works for CPU. For CUDA, please use
[`torch.manual_seed()`](torch.manual_seed.html#torch.manual_seed), which works for both CPU and CUDA.

Parameters:

**new_state** (*torch.ByteTensor*) - The desired state