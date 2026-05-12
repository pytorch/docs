# torch.nn.functional.adaptive_max_pool2d

torch.nn.functional.adaptive_max_pool2d(*input*, *output_size*, *return_indices=False*)[[source]](https://github.com/pytorch/pytorch/blob/8df61039f8235b92b0ca250355cc296020f46e2d/torch/_jit_internal.py#L627)

Applies a 2D adaptive max pooling over an input signal composed of
several input planes.

See [`AdaptiveMaxPool2d`](torch.nn.AdaptiveMaxPool2d.html#torch.nn.AdaptiveMaxPool2d) for details and output shape.

Parameters:

- **output_size** - the target output size (single integer or
double-integer tuple)
- **return_indices** - whether to return pooling indices. Default: `False`