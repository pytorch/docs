# torch.nn.functional.adaptive_max_pool3d

torch.nn.functional.adaptive_max_pool3d(*input*, *output_size*, *return_indices=False*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/_jit_internal.py#L627)

Applies a 3D adaptive max pooling over an input signal composed of
several input planes.

See [`AdaptiveMaxPool3d`](torch.nn.AdaptiveMaxPool3d.html#torch.nn.AdaptiveMaxPool3d) for details and output shape.

Parameters:

- **output_size** - the target output size (single integer or
triple-integer tuple)
- **return_indices** - whether to return pooling indices. Default: `False`