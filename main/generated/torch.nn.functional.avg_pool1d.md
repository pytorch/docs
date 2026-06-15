# torch.nn.functional.avg_pool1d

torch.nn.functional.avg_pool1d(*input*, *kernel_size*, *stride=None*, *padding=0*, *ceil_mode=False*, *count_include_pad=True*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/6a231d0d3e1ccd63dd51479bcadc969d0a8de2b9/torch/nn/functional.py#L345)

Applies a 1D average pooling over an input signal composed of several
input planes.

See [`AvgPool1d`](torch.nn.AvgPool1d.html#torch.nn.AvgPool1d) for details and output shape.

Parameters:

- **input** - input tensor of shape (minibatch,in_channels,iW)(\text{minibatch} , \text{in\_channels} , iW)(minibatch,in_channels,iW)
- **kernel_size** - the size of the window. Can be a single number or a
tuple (kW,)
- **stride** - the stride of the window. Can be a single number or a tuple
(sW,). Default: `kernel_size`
- **padding** - implicit zero paddings on both sides of the input. Can be a single
number or a tuple (padW,). Should be at most half of effective kernel
size, that is ((kernelSize−1)∗dilation+1)/2((kernelSize - 1) * dilation + 1) / 2((kernelSize−1)∗dilation+1)/2. Default: 0
- **ceil_mode** - when True, will use ceil instead of floor to compute the
output shape. Default: `False`
- **count_include_pad** - when True, will include the zero-padding in the
averaging calculation. Default: `True`

Examples:

```
>>> # pool of square window of size=3, stride=2
>>> input = torch.tensor([[[1, 2, 3, 4, 5, 6, 7]]], dtype=torch.float32)
>>> F.avg_pool1d(input, kernel_size=3, stride=2)
tensor([[[ 2., 4., 6.]]])
```