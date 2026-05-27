# adaptive_avg_pool3d

*class*torch.ao.nn.quantized.functional.adaptive_avg_pool3d(*input*, *output_size*)[[source]](https://github.com/pytorch/pytorch/blob/34424f27313fbcddaafe4a1a855000f17e05a260/torch/ao/nn/quantized/functional.py#L153)

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