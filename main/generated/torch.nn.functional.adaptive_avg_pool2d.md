# torch.nn.functional.adaptive_avg_pool2d

torch.nn.functional.adaptive_avg_pool2d(*input*, *output_size*)[[source]](https://github.com/pytorch/pytorch/blob/8ab13d788b9dab3e338e618576e65bb8b0c75e1a/torch/nn/functional.py#L1440)

Apply a 2D adaptive average pooling over an input signal composed of several input planes.

See [`AdaptiveAvgPool2d`](torch.nn.AdaptiveAvgPool2d.html#torch.nn.AdaptiveAvgPool2d) for details and output shape.

Parameters:

**output_size** (*None*) - the target output size (single integer or
double-integer tuple)

Return type:

[*Tensor*](../tensors.html#torch.Tensor)