# MaxPool3d

*class*torch.nn.MaxPool3d(*kernel_size*, *stride=None*, *padding=0*, *dilation=1*, *return_indices=False*, *ceil_mode=False*)[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/nn/modules/pooling.py#L235)

Applies a 3D max pooling over an input signal composed of several input planes.

In the simplest case, the output value of the layer with input size (N,C,D,H,W)(N, C, D, H, W)(N,C,D,H,W),
output (N,C,Dout,Hout,Wout)(N, C, D_{out}, H_{out}, W_{out})(N,C,Dout​,Hout​,Wout​) and `kernel_size` (kD,kH,kW)(kD, kH, kW)(kD,kH,kW)
can be precisely described as:

out(Ni,Cj,d,h,w)=max⁡k=0,...,kD−1max⁡m=0,...,kH−1max⁡n=0,...,kW−1input(Ni,Cj,stride[0]×d+k,stride[1]×h+m,stride[2]×w+n)\begin{aligned}
 \text{out}(N_i, C_j, d, h, w) ={} & \max_{k=0, \ldots, kD-1} \max_{m=0, \ldots, kH-1} \max_{n=0, \ldots, kW-1} \\
 & \text{input}(N_i, C_j, \text{stride[0]} \times d + k,
 \text{stride[1]} \times h + m, \text{stride[2]} \times w + n)
\end{aligned}

out(Ni​,Cj​,d,h,w)=​k=0,...,kD−1max​m=0,...,kH−1max​n=0,...,kW−1max​input(Ni​,Cj​,stride[0]×d+k,stride[1]×h+m,stride[2]×w+n)​

If `padding` is non-zero, then the input is implicitly padded with negative infinity on both sides
for `padding` number of points. `dilation` controls the spacing between the kernel points.
It is harder to describe, but this [link](https://github.com/vdumoulin/conv_arithmetic/blob/master/README.md) has a nice visualization of what `dilation` does.

Note

When ceil_mode=True, sliding windows are allowed to go off-bounds if they start within the left padding
or the input. Sliding windows that would start in the right padded region are ignored.

The parameters `kernel_size`, `stride`, `padding`, `dilation` can either be:

> - a single `int` - in which case the same value is used for the depth, height and width dimension
> - a `tuple` of three ints - in which case, the first int is used for the depth dimension,
> the second int for the height dimension and the third int for the width dimension

Parameters:

- **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the size of the window to take a max over
- **stride** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the stride of the window. Default value is `kernel_size`
- **padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - Implicit negative infinity padding to be added on all three sides
- **dilation** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - a parameter that controls the stride of elements in the window
- **return_indices** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - if `True`, will return the max indices along with the outputs.
Useful for [`torch.nn.MaxUnpool3d`](torch.nn.MaxUnpool3d.html#torch.nn.MaxUnpool3d) later
- **ceil_mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - when True, will use ceil instead of floor to compute the output shape

Shape:

- Input: (N,C,Din,Hin,Win)(N, C, D_{in}, H_{in}, W_{in})(N,C,Din​,Hin​,Win​) or (C,Din,Hin,Win)(C, D_{in}, H_{in}, W_{in})(C,Din​,Hin​,Win​).
- Output: (N,C,Dout,Hout,Wout)(N, C, D_{out}, H_{out}, W_{out})(N,C,Dout​,Hout​,Wout​) or (C,Dout,Hout,Wout)(C, D_{out}, H_{out}, W_{out})(C,Dout​,Hout​,Wout​), where

Dout=⌊Din+2×padding[0]−dilation[0]×(kernel_size[0]−1)−1stride[0]+1⌋D_{out} = \left\lfloor\frac{D_{in} + 2 \times \text{padding}[0] - \text{dilation}[0] \times
 (\text{kernel\_size}[0] - 1) - 1}{\text{stride}[0]} + 1\right\rfloor

Dout​=⌊stride[0]Din​+2×padding[0]−dilation[0]×(kernel_size[0]−1)−1​+1⌋
Hout=⌊Hin+2×padding[1]−dilation[1]×(kernel_size[1]−1)−1stride[1]+1⌋H_{out} = \left\lfloor\frac{H_{in} + 2 \times \text{padding}[1] - \text{dilation}[1] \times
 (\text{kernel\_size}[1] - 1) - 1}{\text{stride}[1]} + 1\right\rfloor

Hout​=⌊stride[1]Hin​+2×padding[1]−dilation[1]×(kernel_size[1]−1)−1​+1⌋
Wout=⌊Win+2×padding[2]−dilation[2]×(kernel_size[2]−1)−1stride[2]+1⌋W_{out} = \left\lfloor\frac{W_{in} + 2 \times \text{padding}[2] - \text{dilation}[2] \times
 (\text{kernel\_size}[2] - 1) - 1}{\text{stride}[2]} + 1\right\rfloor

Wout​=⌊stride[2]Win​+2×padding[2]−dilation[2]×(kernel_size[2]−1)−1​+1⌋

Examples:

```
>>> # pool of square window of size=3, stride=2
>>> m = nn.MaxPool3d(3, stride=2)
>>> # pool of non-square window
>>> m = nn.MaxPool3d((3, 2, 2), stride=(2, 1, 2))
>>> input = torch.randn(20, 16, 50, 44, 31)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/nn/modules/pooling.py#L306)

Runs the forward pass.