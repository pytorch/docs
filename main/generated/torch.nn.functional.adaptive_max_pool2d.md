# torch.nn.functional.adaptive_max_pool2d

torch.nn.functional.adaptive_max_pool2d(*input*, *output_size*, *return_indices=False*)[[source]](https://github.com/pytorch/pytorch/blob/7e9fd4e82a01d43fc8afdf03258cf85ee22db2ea/torch/_jit_internal.py#L627)

Applies a 2D adaptive max pooling over an input signal composed of
several input planes.

See [`AdaptiveMaxPool2d`](torch.nn.AdaptiveMaxPool2d.html#torch.nn.AdaptiveMaxPool2d) for details and output shape.

Parameters:

- **output_size** - the target output size (single integer or
double-integer tuple)
- **return_indices** - whether to return pooling indices. Default: `False`