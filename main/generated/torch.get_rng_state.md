# torch.get_rng_state

torch.get_rng_state()[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/random.py#L39)

Returns the random number generator state as a torch.ByteTensor.

Note

The returned state is for the default generator on CPU only.

See also: [`torch.random.fork_rng()`](../random.html#torch.random.fork_rng).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)