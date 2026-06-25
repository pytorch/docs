# avg_pool3d

*class*torch.ao.nn.quantized.functional.avg_pool3d(*input*, *kernel_size*, *stride=None*, *padding=0*, *ceil_mode=False*, *count_include_pad=True*, *divisor_override=None*)[[source]](https://github.com/pytorch/pytorch/blob/847b7df02b84551445eda7d44d08f15bda4c6159/torch/ao/nn/quantized/functional.py#L89)

Applies 3D average-pooling operation in kD timeskH×kWkD \ times kH \times kWkD timeskH×kW regions by step size
sD×sH×sWsD \times sH \times sWsD×sH×sW steps. The number of output features is equal to the number of
input planes.

Note

The input quantization parameters propagate to the output.

Parameters:

- **input** - quantized input tensor (minibatch,in_channels,iH,iW)(\text{minibatch} , \text{in\_channels} , iH , iW)(minibatch,in_channels,iH,iW)
- **kernel_size** - size of the pooling region. Can be a single number or a
tuple (kD, kH, kW)
- **stride** - stride of the pooling operation. Can be a single number or a
tuple (sD, sH, sW). Default: `kernel_size`
- **padding** - implicit zero paddings on both sides of the input. Can be a
single number or a tuple (padD, padH, padW). Default: 0
- **ceil_mode** - when True, will use ceil instead of floor in the formula
to compute the output shape. Default: `False`
- **count_include_pad** - when True, will include the zero-padding in the
averaging calculation. Default: `True`
- **divisor_override** - if specified, it will be used as divisor, otherwise
size of the pooling region will be used. Default: None