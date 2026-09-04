# torch.nn.functional.avg_pool2d

torch.nn.functional.avg_pool2d(*input*, *kernel_size*, *stride=None*, *padding=0*, *ceil_mode=False*, *count_include_pad=True*, *divisor_override=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/nn/functional.py#L380)

Applies 2D average-pooling operation in kH×kWkH \times kWkH×kW regions by step size
sH×sWsH \times sWsH×sW steps. The number of output features is equal to the number of
input planes.

See [`AvgPool2d`](torch.nn.AvgPool2d.html#torch.nn.AvgPool2d) for details and output shape.

Parameters:

- **input** - input tensor (minibatch,in_channels,iH,iW)(\text{minibatch} , \text{in\_channels} , iH , iW)(minibatch,in_channels,iH,iW)
- **kernel_size** - size of the pooling region. Can be a single number, a single-element tuple or a
tuple (kH, kW)
- **stride** - stride of the pooling operation. Can be a single number, a single-element tuple or a
tuple (sH, sW). Default: `kernel_size`
- **padding** - implicit zero paddings on both sides of the input. Can be a
single number, a single-element tuple or a tuple (padH, padW).
Should be at most half of effective kernel size, that
is ((kernelSize−1)∗dilation+1)/2((kernelSize - 1) * dilation + 1) / 2((kernelSize−1)∗dilation+1)/2. Default: 0
- **ceil_mode** - when True, will use ceil instead of floor in the formula
to compute the output shape. Default: `False`
- **count_include_pad** - when True, will include the zero-padding in the
averaging calculation. Default: `True`
- **divisor_override** - if specified, it will be used as divisor, otherwise
size of the pooling region will be used. Default: None