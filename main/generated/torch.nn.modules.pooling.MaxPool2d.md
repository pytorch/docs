# MaxPool2d

*class*torch.nn.modules.pooling.MaxPool2d(*kernel_size*, *stride=None*, *padding=0*, *dilation=1*, *return_indices=False*, *ceil_mode=False*)[[source]](https://github.com/pytorch/pytorch/blob/474b9649dd111ae9b0c31728da812cc3dda2c4ae/torch/nn/modules/pooling.py#L155)

Applies a 2D max pooling over an input signal composed of several input planes.

In the simplest case, the output value of the layer with input size (N,C,H,W)(N, C, H, W)(N,C,H,W),
output (N,C,Hout,Wout)(N, C, H_{out}, W_{out})(N,C,Hout​,Wout​) and `kernel_size` (kH,kW)(kH, kW)(kH,kW)
can be precisely described as:

out(Ni,Cj,h,w)=max⁡m=0,...,kH−1max⁡n=0,...,kW−1input(Ni,Cj,stride[0]×h+m,stride[1]×w+n)\begin{aligned}
 out(N_i, C_j, h, w) ={} & \max_{m=0, \ldots, kH-1} \max_{n=0, \ldots, kW-1} \\
 & \text{input}(N_i, C_j, \text{stride[0]} \times h + m,
 \text{stride[1]} \times w + n)
\end{aligned}

out(Ni​,Cj​,h,w)=​m=0,...,kH−1max​n=0,...,kW−1max​input(Ni​,Cj​,stride[0]×h+m,stride[1]×w+n)​

If `padding` is non-zero, then the input is implicitly padded with negative infinity on both sides
for `padding` number of points. `dilation` controls the spacing between the kernel points.
It is harder to describe, but this [link](https://github.com/vdumoulin/conv_arithmetic/blob/master/README.md) has a nice visualization of what `dilation` does.

Note

When ceil_mode=True, sliding windows are allowed to go off-bounds if they start within the left padding
or the input. Sliding windows that would start in the right padded region are ignored.

The parameters `kernel_size`, `stride`, `padding`, `dilation` can either be:

> - a single `int` - in which case the same value is used for the height and width dimension
> - a `tuple` of two ints - in which case, the first int is used for the height dimension,
> and the second int for the width dimension

Parameters:

- **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the size of the window to take a max over
- **stride** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the stride of the window. Default value is `kernel_size`
- **padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - Implicit negative infinity padding to be added on both sides
- **dilation** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - a parameter that controls the stride of elements in the window
- **return_indices** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - if `True`, will return the max indices along with the outputs.
Useful for [`torch.nn.MaxUnpool2d`](torch.nn.MaxUnpool2d.html#torch.nn.MaxUnpool2d) later
- **ceil_mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - when True, will use ceil instead of floor to compute the output shape

Shape:

- Input: (N,C,Hin,Win)(N, C, H_{in}, W_{in})(N,C,Hin​,Win​) or (C,Hin,Win)(C, H_{in}, W_{in})(C,Hin​,Win​)
- Output: (N,C,Hout,Wout)(N, C, H_{out}, W_{out})(N,C,Hout​,Wout​) or (C,Hout,Wout)(C, H_{out}, W_{out})(C,Hout​,Wout​), where

Hout=⌊Hin+2∗padding[0]−dilation[0]×(kernel_size[0]−1)−1stride[0]+1⌋H_{out} = \left\lfloor\frac{H_{in} + 2 * \text{padding[0]} - \text{dilation[0]}
 \times (\text{kernel\_size[0]} - 1) - 1}{\text{stride[0]}} + 1\right\rfloor

Hout​=⌊stride[0]Hin​+2∗padding[0]−dilation[0]×(kernel_size[0]−1)−1​+1⌋
Wout=⌊Win+2∗padding[1]−dilation[1]×(kernel_size[1]−1)−1stride[1]+1⌋W_{out} = \left\lfloor\frac{W_{in} + 2 * \text{padding[1]} - \text{dilation[1]}
 \times (\text{kernel\_size[1]} - 1) - 1}{\text{stride[1]}} + 1\right\rfloor

Wout​=⌊stride[1]Win​+2∗padding[1]−dilation[1]×(kernel_size[1]−1)−1​+1⌋

Examples:

```
>>> # pool of square window of size=3, stride=2
>>> m = nn.MaxPool2d(3, stride=2)
>>> # pool of non-square window
>>> m = nn.MaxPool2d((3, 2), stride=(2, 1))
>>> input = torch.randn(20, 16, 50, 32)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/474b9649dd111ae9b0c31728da812cc3dda2c4ae/torch/nn/modules/pooling.py#L222)

Runs the forward pass.