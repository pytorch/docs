# torch.nn.functional.adaptive_max_pool1d

torch.nn.functional.adaptive_max_pool1d(*input*, *output_size*, *return_indices=False*)[[source]](https://github.com/pytorch/pytorch/blob/f7811aa3c052ace6751fbc2f6bc93908b9ea6b9f/torch/_jit_internal.py#L627)

Applies a 1D adaptive max pooling over an input signal composed of
several input planes.

See [`AdaptiveMaxPool1d`](torch.nn.AdaptiveMaxPool1d.html#torch.nn.AdaptiveMaxPool1d) for details and output shape.

Parameters:

- **output_size** - the target output size (single integer)
- **return_indices** - whether to return pooling indices. Default: `False`