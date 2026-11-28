# torch.get_rng_state

torch.get_rng_state()[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/random.py#L39)

Returns the random number generator state as a torch.ByteTensor.

Note

The returned state is for the default generator on CPU only.

See also: [`torch.random.fork_rng()`](../random.html#torch.random.fork_rng).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)