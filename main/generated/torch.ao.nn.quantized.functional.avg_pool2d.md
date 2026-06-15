# avg_pool2d

*class*torch.ao.nn.quantized.functional.avg_pool2d(*input*, *kernel_size*, *stride=None*, *padding=0*, *ceil_mode=False*, *count_include_pad=True*, *divisor_override=None*)[[source]](https://github.com/pytorch/pytorch/blob/6a231d0d3e1ccd63dd51479bcadc969d0a8de2b9/torch/ao/nn/quantized/functional.py#L43)

Applies 2D average-pooling operation in kH×kWkH \times kWkH×kW regions by step size
sH×sWsH \times sWsH×sW steps. The number of output features is equal to the number of
input planes.

Note

The input quantization parameters propagate to the output.

See `AvgPool2d` for details and output shape.

Parameters:

- **input** - quantized input tensor (minibatch,in_channels,iH,iW)(\text{minibatch} , \text{in\_channels} , iH , iW)(minibatch,in_channels,iH,iW)
- **kernel_size** - size of the pooling region. Can be a single number or a
tuple (kH, kW)
- **stride** - stride of the pooling operation. Can be a single number or a
tuple (sH, sW). Default: `kernel_size`
- **padding** - implicit zero paddings on both sides of the input. Can be a
single number or a tuple (padH, padW). Default: 0
- **ceil_mode** - when True, will use ceil instead of floor in the formula
to compute the output shape. Default: `False`
- **count_include_pad** - when True, will include the zero-padding in the
averaging calculation. Default: `True`
- **divisor_override** - if specified, it will be used as divisor, otherwise
size of the pooling region will be used. Default: None