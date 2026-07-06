# LPPool2d

*class*torch.nn.LPPool2d(*norm_type*, *kernel_size*, *stride=None*, *ceil_mode=False*)[[source]](https://github.com/pytorch/pytorch/blob/a059c4af8933be96044a8625669869fe560baf61/torch/nn/modules/pooling.py#L1174)

Applies a 2D power-average pooling over an input signal composed of several input planes.

On each window, the function computed is:

f(X)=∑x∈Xxppf(X) = \sqrt[p]{\sum_{x \in X} x^{p}}

f(X)=p​x∈X∑​xp​

- At p = ∞\infty∞, one gets Max Pooling over absolute values
- At p = 1, one gets Sum Pooling (which is proportional to average pooling)

The parameters `kernel_size`, `stride` can either be:

> - a single `int` - in which case the same value is used for the height and width dimension
> - a `tuple` of two ints - in which case, the first int is used for the height dimension,
> and the second int for the width dimension

Note

If the sum to the power of p is zero, the gradient of this function is
not defined. This implementation will set the gradient to zero in this case.

Parameters:

- **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the size of the window
- **stride** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the stride of the window. Default value is `kernel_size`
- **ceil_mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - when True, will use ceil instead of floor to compute the output shape

Note

When `ceil_mode` is `True`, sliding windows may go off-bounds if they start within the
left padding or the input. Sliding windows that would start in the right padded region are ignored.

Shape:

- Input: (N,C,Hin,Win)(N, C, H_{in}, W_{in})(N,C,Hin​,Win​) or (C,Hin,Win)(C, H_{in}, W_{in})(C,Hin​,Win​).
- Output: (N,C,Hout,Wout)(N, C, H_{out}, W_{out})(N,C,Hout​,Wout​) or (C,Hout,Wout)(C, H_{out}, W_{out})(C,Hout​,Wout​), where

Hout=⌊Hin−kernel_size[0]stride[0]+1⌋H_{out} = \left\lfloor\frac{H_{in} - \text{kernel\_size}[0]}{\text{stride}[0]} + 1\right\rfloor

Hout​=⌊stride[0]Hin​−kernel_size[0]​+1⌋
Wout=⌊Win−kernel_size[1]stride[1]+1⌋W_{out} = \left\lfloor\frac{W_{in} - \text{kernel\_size}[1]}{\text{stride}[1]} + 1\right\rfloor

Wout​=⌊stride[1]Win​−kernel_size[1]​+1⌋

Examples:

```
>>> # power-2 pool of square window of size=3, stride=2
>>> m = nn.LPPool2d(2, 3, stride=2)
>>> # pool of non-square window of power 1.2
>>> m = nn.LPPool2d(1.2, (3, 2), stride=(2, 1))
>>> input = torch.randn(20, 16, 50, 32)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/a059c4af8933be96044a8625669869fe560baf61/torch/nn/modules/pooling.py#L1227)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)