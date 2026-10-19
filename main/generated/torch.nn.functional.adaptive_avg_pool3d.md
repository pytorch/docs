# torch.nn.functional.adaptive_avg_pool3d

torch.nn.functional.adaptive_avg_pool3d(*input*, *output_size*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/nn/functional.py#L1486)

Apply a 3D adaptive average pooling over an input signal composed of several input planes.

See [`AdaptiveAvgPool3d`](torch.nn.AdaptiveAvgPool3d.html#torch.nn.AdaptiveAvgPool3d) for details and output shape.

Parameters:

**output_size** (*None*) - the target output size (single integer or
triple-integer tuple)

Return type:

[*Tensor*](../tensors.html#torch.Tensor)