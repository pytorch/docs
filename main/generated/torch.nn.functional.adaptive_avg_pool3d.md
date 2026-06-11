# torch.nn.functional.adaptive_avg_pool3d

torch.nn.functional.adaptive_avg_pool3d(*input*, *output_size*)[[source]](https://github.com/pytorch/pytorch/blob/63f903c3d6b04c7cb1433d1d67e2b8e21c055bc7/torch/nn/functional.py#L1450)

Apply a 3D adaptive average pooling over an input signal composed of several input planes.

See [`AdaptiveAvgPool3d`](torch.nn.AdaptiveAvgPool3d.html#torch.nn.AdaptiveAvgPool3d) for details and output shape.

Parameters:

**output_size** (*None*) - the target output size (single integer or
triple-integer tuple)

Return type:

[*Tensor*](../tensors.html#torch.Tensor)