# LPPool3d

*class*torch.nn.modules.pooling.LPPool3d(*norm_type*, *kernel_size*, *stride=None*, *ceil_mode=False*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/nn/modules/pooling.py#L1234)

Applies a 3D power-average pooling over an input signal composed of several input planes.

On each window, the function computed is:

f(X)=∑x∈Xxppf(X) = \sqrt[p]{\sum_{x \in X} x^{p}}

f(X)=p​x∈X∑​xp​

- At p = ∞\infty∞, one gets Max Pooling over absolute values
- At p = 1, one gets Sum Pooling (which is proportional to average pooling)

The parameters `kernel_size`, `stride` can either be:

> - a single `int` - in which case the same value is used for the height, width and depth dimension
> - a `tuple` of three ints - in which case, the first int is used for the depth dimension,
> the second int for the height dimension and the third int for the width dimension

Note

If the sum to the power of p is zero, the gradient of this function is
not defined. This implementation will set the gradient to zero in this case.

Parameters:

- **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the size of the window
- **stride** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the stride of the window. Default value is `kernel_size`
- **ceil_mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - when True, will use ceil instead of floor to compute the output shape

Note

When `ceil_mode` is `True`, sliding windows may go off-bounds if they start within the
left padding or the input. Sliding windows that would start in the right padded region are ignored.

Shape:

- Input: (N,C,Din,Hin,Win)(N, C, D_{in}, H_{in}, W_{in})(N,C,Din​,Hin​,Win​) or (C,Din,Hin,Win)(C, D_{in}, H_{in}, W_{in})(C,Din​,Hin​,Win​).
- Output: (N,C,Dout,Hout,Wout)(N, C, D_{out}, H_{out}, W_{out})(N,C,Dout​,Hout​,Wout​) or
(C,Dout,Hout,Wout)(C, D_{out}, H_{out}, W_{out})(C,Dout​,Hout​,Wout​), where

Dout=⌊Din−kernel_size[0]stride[0]+1⌋D_{out} = \left\lfloor\frac{D_{in} - \text{kernel\_size}[0]}{\text{stride}[0]} + 1\right\rfloor

Dout​=⌊stride[0]Din​−kernel_size[0]​+1⌋
Hout=⌊Hin−kernel_size[1]stride[1]+1⌋H_{out} = \left\lfloor\frac{H_{in} - \text{kernel\_size}[1]}{\text{stride}[1]} + 1\right\rfloor

Hout​=⌊stride[1]Hin​−kernel_size[1]​+1⌋
Wout=⌊Win−kernel_size[2]stride[2]+1⌋W_{out} = \left\lfloor\frac{W_{in} - \text{kernel\_size}[2]}{\text{stride}[2]} + 1\right\rfloor

Wout​=⌊stride[2]Win​−kernel_size[2]​+1⌋

Examples:

```
>>> # power-2 pool of square window of size=3, stride=2
>>> m = nn.LPPool3d(2, 3, stride=2)
>>> # pool of non-square window of power 1.2
>>> m = nn.LPPool3d(1.2, (3, 2, 2), stride=(2, 1, 2))
>>> input = torch.randn(20, 16, 50, 44, 31)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/nn/modules/pooling.py#L1291)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)