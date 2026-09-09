# torch.nn.functional.adaptive_max_pool1d

torch.nn.functional.adaptive_max_pool1d(*input*, *output_size*, *return_indices=False*)[[source]](https://github.com/pytorch/pytorch/blob/c712ec6ebb4ecd2838e2cafb0bbc7a3c5acfe668/torch/_jit_internal.py#L627)

Applies a 1D adaptive max pooling over an input signal composed of
several input planes.

See [`AdaptiveMaxPool1d`](torch.nn.AdaptiveMaxPool1d.html#torch.nn.AdaptiveMaxPool1d) for details and output shape.

Parameters:

- **output_size** - the target output size (single integer)
- **return_indices** - whether to return pooling indices. Default: `False`