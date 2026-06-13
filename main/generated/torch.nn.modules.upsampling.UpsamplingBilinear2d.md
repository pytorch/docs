# UpsamplingBilinear2d

*class*torch.nn.modules.upsampling.UpsamplingBilinear2d(*size=None*, *scale_factor=None*)[[source]](https://github.com/pytorch/pytorch/blob/19afbb4e2e81cc5702fa8cc34c48e1879b98a5aa/torch/nn/modules/upsampling.py#L250)

Applies a 2D bilinear upsampling to an input signal composed of several input channels.

To specify the scale, it takes either the `size` or the `scale_factor`
as its constructor argument.

When `size` is given, it is the output size of the image (h, w).

Parameters:

- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)*or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - output spatial sizes
- **scale_factor** ([*float*](https://docs.python.org/3/library/functions.html#float)*or**Tuple**[*[*float*](https://docs.python.org/3/library/functions.html#float)*,*[*float*](https://docs.python.org/3/library/functions.html#float)*]**,**optional*) - multiplier for
spatial size.

Warning

This class is deprecated in favor of `interpolate()`. It is
equivalent to `nn.functional.interpolate(..., mode='bilinear', align_corners=True)`.

Shape:

- Input: (N,C,Hin,Win)(N, C, H_{in}, W_{in})(N,C,Hin​,Win​)
- Output: (N,C,Hout,Wout)(N, C, H_{out}, W_{out})(N,C,Hout​,Wout​) where

Hout=⌊Hin×scale_factor⌋H_{out} = \left\lfloor H_{in} \times \text{scale\_factor} \right\rfloor

Hout​=⌊Hin​×scale_factor⌋
Wout=⌊Win×scale_factor⌋W_{out} = \left\lfloor W_{in} \times \text{scale\_factor} \right\rfloor

Wout​=⌊Win​×scale_factor⌋

Examples:

```
>>> input = torch.arange(1, 5, dtype=torch.float32).view(1, 1, 2, 2)
>>> input
tensor([[[[1., 2.],
 [3., 4.]]]])

>>> m = nn.UpsamplingBilinear2d(scale_factor=2)
>>> m(input)
tensor([[[[1.0000, 1.3333, 1.6667, 2.0000],
 [1.6667, 2.0000, 2.3333, 2.6667],
 [2.3333, 2.6667, 3.0000, 3.3333],
 [3.0000, 3.3333, 3.6667, 4.0000]]]])
```