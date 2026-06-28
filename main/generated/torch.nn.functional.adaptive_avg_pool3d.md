# torch.nn.functional.adaptive_avg_pool3d

torch.nn.functional.adaptive_avg_pool3d(*input*, *output_size*)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/nn/functional.py#L1456)

Apply a 3D adaptive average pooling over an input signal composed of several input planes.

See [`AdaptiveAvgPool3d`](torch.nn.AdaptiveAvgPool3d.html#torch.nn.AdaptiveAvgPool3d) for details and output shape.

Parameters:

**output_size** (*None*) - the target output size (single integer or
triple-integer tuple)

Return type:

[*Tensor*](../tensors.html#torch.Tensor)