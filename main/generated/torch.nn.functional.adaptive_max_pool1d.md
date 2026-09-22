# torch.nn.functional.adaptive_max_pool1d

torch.nn.functional.adaptive_max_pool1d(*input*, *output_size*, *return_indices=False*)[[source]](https://github.com/pytorch/pytorch/blob/9d784735eb70fb8b0335b0ad7cad9db3ea4babbd/torch/_jit_internal.py#L627)

Applies a 1D adaptive max pooling over an input signal composed of
several input planes.

See [`AdaptiveMaxPool1d`](torch.nn.AdaptiveMaxPool1d.html#torch.nn.AdaptiveMaxPool1d) for details and output shape.

Parameters:

- **output_size** - the target output size (single integer)
- **return_indices** - whether to return pooling indices. Default: `False`