# adaptive_avg_pool3d

*class*torch.ao.nn.quantized.functional.adaptive_avg_pool3d(*input*, *output_size*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/ao/nn/quantized/functional.py#L153)

Applies a 3D adaptive average pooling over a quantized input signal composed
of several quantized input planes.

Note

The input quantization parameters propagate to the output.

See `AdaptiveAvgPool3d` for details and output shape.

Parameters:

**output_size** (*None*) - the target output size (single integer or
double-integer tuple)

Return type:

[*Tensor*](../tensors.html#torch.Tensor)