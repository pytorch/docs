# AvgPool3d

*class*torch.nn.modules.pooling.AvgPool3d(*kernel_size*, *stride=None*, *padding=0*, *ceil_mode=False*, *count_include_pad=True*, *divisor_override=None*)[[source]](https://github.com/pytorch/pytorch/blob/4ff2d1161191378e895e560774c1622dba40076d/torch/nn/modules/pooling.py#L790)

Applies a 3D average pooling over an input signal composed of several input planes.

In the simplest case, the output value of the layer with input size (N,C,D,H,W)(N, C, D, H, W)(N,C,D,H,W),
output (N,C,Dout,Hout,Wout)(N, C, D_{out}, H_{out}, W_{out})(N,C,Dout​,Hout​,Wout​) and `kernel_size` (kD,kH,kW)(kD, kH, kW)(kD,kH,kW)
can be precisely described as:

out(Ni,Cj,d,h,w)=∑k=0kD−1∑m=0kH−1∑n=0kW−1input(Ni,Cj,stride[0]×d+k,stride[1]×h+m,stride[2]×w+n)kD×kH×kW\begin{aligned}
 \text{out}(N_i, C_j, d, h, w) ={} & \sum_{k=0}^{kD-1} \sum_{m=0}^{kH-1} \sum_{n=0}^{kW-1} \\
 & \frac{\text{input}(N_i, C_j, \text{stride}[0] \times d + k,
 \text{stride}[1] \times h + m, \text{stride}[2] \times w + n)}
 {kD \times kH \times kW}
\end{aligned}

out(Ni​,Cj​,d,h,w)=​k=0∑kD−1​m=0∑kH−1​n=0∑kW−1​kD×kH×kWinput(Ni​,Cj​,stride[0]×d+k,stride[1]×h+m,stride[2]×w+n)​​

If `padding` is non-zero, then the input is implicitly zero-padded on all three sides
for `padding` number of points.

Note

When ceil_mode=True, sliding windows are allowed to go off-bounds if they start within the left padding
or the input. Sliding windows that would start in the right padded region are ignored.

Note

pad should be at most half of effective kernel size.

The parameters `kernel_size`, `stride` can either be:

> - a single `int` - in which case the same value is used for the depth, height and width dimension
> - a `tuple` of three ints - in which case, the first int is used for the depth dimension,
> the second int for the height dimension and the third int for the width dimension

Parameters:

- **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the size of the window
- **stride** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the stride of the window. Default value is `kernel_size`
- **padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - implicit zero padding to be added on all three sides
- **ceil_mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - when True, will use ceil instead of floor to compute the output shape
- **count_include_pad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - when True, will include the zero-padding in the averaging calculation
- **divisor_override** ([*int*](https://docs.python.org/3/library/functions.html#int)*|**None*) - if specified, it will be used as divisor, otherwise `kernel_size` will be used

Shape:

- Input: (N,C,Din,Hin,Win)(N, C, D_{in}, H_{in}, W_{in})(N,C,Din​,Hin​,Win​) or (C,Din,Hin,Win)(C, D_{in}, H_{in}, W_{in})(C,Din​,Hin​,Win​).
- Output: (N,C,Dout,Hout,Wout)(N, C, D_{out}, H_{out}, W_{out})(N,C,Dout​,Hout​,Wout​) or
(C,Dout,Hout,Wout)(C, D_{out}, H_{out}, W_{out})(C,Dout​,Hout​,Wout​), where

Dout=⌊Din+2×padding[0]−kernel_size[0]stride[0]+1⌋D_{out} = \left\lfloor\frac{D_{in} + 2 \times \text{padding}[0] -
 \text{kernel\_size}[0]}{\text{stride}[0]} + 1\right\rfloor

Dout​=⌊stride[0]Din​+2×padding[0]−kernel_size[0]​+1⌋
Hout=⌊Hin+2×padding[1]−kernel_size[1]stride[1]+1⌋H_{out} = \left\lfloor\frac{H_{in} + 2 \times \text{padding}[1] -
 \text{kernel\_size}[1]}{\text{stride}[1]} + 1\right\rfloor

Hout​=⌊stride[1]Hin​+2×padding[1]−kernel_size[1]​+1⌋
Wout=⌊Win+2×padding[2]−kernel_size[2]stride[2]+1⌋W_{out} = \left\lfloor\frac{W_{in} + 2 \times \text{padding}[2] -
 \text{kernel\_size}[2]}{\text{stride}[2]} + 1\right\rfloor

Wout​=⌊stride[2]Win​+2×padding[2]−kernel_size[2]​+1⌋

Per the note above, if `ceil_mode` is True and (Dout−1)×stride[0]≥Din+padding[0](D_{out} - 1)\times \text{stride}[0]\geq D_{in}
+ \text{padding}[0](Dout​−1)×stride[0]≥Din​+padding[0], we skip the last window as it would start in the padded region,
resulting in DoutD_{out}Dout​ being reduced by one.

The same applies for WoutW_{out}Wout​ and HoutH_{out}Hout​.

Examples:

```
>>> # pool of square window of size=3, stride=2
>>> m = nn.AvgPool3d(3, stride=2)
>>> # pool of non-square window
>>> m = nn.AvgPool3d((3, 2, 2), stride=(2, 1, 2))
>>> input = torch.randn(20, 16, 50, 44, 31)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/4ff2d1161191378e895e560774c1622dba40076d/torch/nn/modules/pooling.py#L894)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)