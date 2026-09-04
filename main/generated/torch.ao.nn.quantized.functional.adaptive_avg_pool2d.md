# adaptive_avg_pool2d

*class*torch.ao.nn.quantized.functional.adaptive_avg_pool2d(*input*, *output_size*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/ao/nn/quantized/functional.py#L133)

Applies a 2D adaptive average pooling over a quantized input signal composed
of several quantized input planes.

Note

The input quantization parameters propagate to the output.

See `AdaptiveAvgPool2d` for details and output shape.

Parameters:

**output_size** (*None*) - the target output size (single integer or
double-integer tuple)

Return type:

[*Tensor*](../tensors.html#torch.Tensor)