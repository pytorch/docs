# max_pool2d

*class*torch.ao.nn.quantized.functional.max_pool2d(*input*, *kernel_size*, *stride=None*, *padding=0*, *dilation=1*, *ceil_mode=False*, *return_indices=False*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/ao/nn/quantized/functional.py#L511)

Applies a 2D max pooling over a quantized input signal composed of
several quantized input planes.

Note

The input quantization parameters are propagated to the output.

See `MaxPool2d` for details.