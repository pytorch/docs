# torch.nn.functional.adaptive_max_pool2d

torch.nn.functional.adaptive_max_pool2d(*input*, *output_size*, *return_indices=False*)[[source]](https://github.com/pytorch/pytorch/blob/e5aa1320b162fc3b9d0d53207fe340a6d3aa03d1/torch/_jit_internal.py#L627)

Applies a 2D adaptive max pooling over an input signal composed of
several input planes.

See [`AdaptiveMaxPool2d`](torch.nn.AdaptiveMaxPool2d.html#torch.nn.AdaptiveMaxPool2d) for details and output shape.

Parameters:

- **output_size** - the target output size (single integer or
double-integer tuple)
- **return_indices** - whether to return pooling indices. Default: `False`