# AvgPool2d

*class*torch.nn.modules.pooling.AvgPool2d(*kernel_size*, *stride=None*, *padding=0*, *ceil_mode=False*, *count_include_pad=True*, *divisor_override=None*)[[source]](https://github.com/pytorch/pytorch/blob/9abc5460749ef85e489d960cb5facefc8cc1eb7c/torch/nn/modules/pooling.py#L680)

Applies a 2D average pooling over an input signal composed of several input planes.

In the simplest case, the output value of the layer with input size (N,C,H,W)(N, C, H, W)(N,C,H,W),
output (N,C,Hout,Wout)(N, C, H_{out}, W_{out})(N,C,Hout​,Wout​) and `kernel_size` (kH,kW)(kH, kW)(kH,kW)
can be precisely described as:

out(Ni,Cj,h,w)=1kH∗kW∑m=0kH−1∑n=0kW−1input(Ni,Cj,stride[0]×h+m,stride[1]×w+n)out(N_i, C_j, h, w) = \frac{1}{kH * kW} \sum_{m=0}^{kH-1} \sum_{n=0}^{kW-1}
 input(N_i, C_j, stride[0] \times h + m, stride[1] \times w + n)out(Ni​,Cj​,h,w)=kH∗kW1​m=0∑kH−1​n=0∑kW−1​input(Ni​,Cj​,stride[0]×h+m,stride[1]×w+n)

If `padding` is non-zero, then the input is implicitly zero-padded on both sides
for `padding` number of points.

Note

When ceil_mode=True, sliding windows are allowed to go off-bounds if they start within the left padding
or the input. Sliding windows that would start in the right padded region are ignored.

Note

pad should be at most half of effective kernel size.

The parameters `kernel_size`, `stride`, `padding` can either be:

> - a single `int` or a single-element tuple - in which case the same value is used for the height and width dimension
> - a `tuple` of two ints - in which case, the first int is used for the height dimension,
> and the second int for the width dimension

Parameters:

- **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the size of the window
- **stride** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the stride of the window. Default value is `kernel_size`
- **padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - implicit zero padding to be added on both sides
- **ceil_mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - when True, will use ceil instead of floor to compute the output shape
- **count_include_pad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - when True, will include the zero-padding in the averaging calculation
- **divisor_override** ([*int*](https://docs.python.org/3/library/functions.html#int)*|**None*) - if specified, it will be used as divisor, otherwise size of the pooling region will be used.

Shape:

- Input: (N,C,Hin,Win)(N, C, H_{in}, W_{in})(N,C,Hin​,Win​) or (C,Hin,Win)(C, H_{in}, W_{in})(C,Hin​,Win​).
- Output: (N,C,Hout,Wout)(N, C, H_{out}, W_{out})(N,C,Hout​,Wout​) or (C,Hout,Wout)(C, H_{out}, W_{out})(C,Hout​,Wout​), where

Hout=⌊Hin+2×padding[0]−kernel_size[0]stride[0]+1⌋H_{out} = \left\lfloor\frac{H_{in} + 2 \times \text{padding}[0] -
 \text{kernel\_size}[0]}{\text{stride}[0]} + 1\right\rfloor

Hout​=⌊stride[0]Hin​+2×padding[0]−kernel_size[0]​+1⌋
Wout=⌊Win+2×padding[1]−kernel_size[1]stride[1]+1⌋W_{out} = \left\lfloor\frac{W_{in} + 2 \times \text{padding}[1] -
 \text{kernel\_size}[1]}{\text{stride}[1]} + 1\right\rfloor

Wout​=⌊stride[1]Win​+2×padding[1]−kernel_size[1]​+1⌋

Per the note above, if `ceil_mode` is True and (Hout−1)×stride[0]≥Hin+padding[0](H_{out} - 1)\times \text{stride}[0]\geq H_{in}
+ \text{padding}[0](Hout​−1)×stride[0]≥Hin​+padding[0], we skip the last window as it would start in the bottom padded region,
resulting in HoutH_{out}Hout​ being reduced by one.

The same applies for WoutW_{out}Wout​.

Examples:

```
>>> # pool of square window of size=3, stride=2
>>> m = nn.AvgPool2d(3, stride=2)
>>> # pool of non-square window
>>> m = nn.AvgPool2d((3, 2), stride=(2, 1))
>>> input = torch.randn(20, 16, 50, 32)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/9abc5460749ef85e489d960cb5facefc8cc1eb7c/torch/nn/modules/pooling.py#L777)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)