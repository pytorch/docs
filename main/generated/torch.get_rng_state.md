# torch.get_rng_state

torch.get_rng_state()[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/random.py#L39)

Returns the random number generator state as a torch.ByteTensor.

Note

The returned state is for the default generator on CPU only.

See also: [`torch.random.fork_rng()`](../random.html#torch.random.fork_rng).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)