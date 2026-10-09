# torch.get_rng_state

torch.get_rng_state()[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/random.py#L39)

Returns the random number generator state as a torch.ByteTensor.

Note

The returned state is for the default generator on CPU only.

See also: [`torch.random.fork_rng()`](../random.html#torch.random.fork_rng).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)