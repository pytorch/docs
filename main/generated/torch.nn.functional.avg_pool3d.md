# torch.nn.functional.avg_pool3d

torch.nn.functional.avg_pool3d(*input*, *kernel_size*, *stride=None*, *padding=0*, *ceil_mode=False*, *count_include_pad=True*, *divisor_override=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/nn/functional.py#L410)

Applies 3D average-pooling operation in kT×kH×kWkT \times kH \times kWkT×kH×kW regions by step
size sT×sH×sWsT \times sH \times sWsT×sH×sW steps. The number of output features is equal to
⌊input planessT⌋\lfloor\frac{\text{input planes}}{sT}\rfloor⌊sTinput planes​⌋.

See [`AvgPool3d`](torch.nn.AvgPool3d.html#torch.nn.AvgPool3d) for details and output shape.

Parameters:

- **input** - input tensor (minibatch,in_channels,iT×iH,iW)(\text{minibatch} , \text{in\_channels} , iT \times iH , iW)(minibatch,in_channels,iT×iH,iW)
- **kernel_size** - size of the pooling region. Can be a single number or a
tuple (kT, kH, kW)
- **stride** - stride of the pooling operation. Can be a single number or a
tuple (sT, sH, sW). Default: `kernel_size`
- **padding** - implicit zero paddings on both sides of the input. Can be a
single number or a tuple (padT, padH, padW). Should be at most half
of effective kernel size, that is ((kernelSize−1)∗dilation+1)/2((kernelSize - 1) * dilation + 1) / 2((kernelSize−1)∗dilation+1)/2.
Default: 0
- **ceil_mode** - when True, will use ceil instead of floor in the formula
to compute the output shape
- **count_include_pad** - when True, will include the zero-padding in the
averaging calculation
- **divisor_override** - if specified, it will be used as divisor, otherwise
size of the pooling region will be used. Default: None