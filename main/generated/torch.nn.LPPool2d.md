# LPPool2d

*class*torch.nn.LPPool2d(*norm_type*, *kernel_size*, *stride=None*, *ceil_mode=False*)[[source]](https://github.com/pytorch/pytorch/blob/8fcaa153fa223ca9f7844513d86d4d30a0cf2533/torch/nn/modules/pooling.py#L1178)

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

- **norm_type** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*float*](https://docs.python.org/3/builtins/functions.html#float)) - the power ppp used to compute pooling.
Must be non-zero; positive and negative infinity are supported.
- **kernel_size** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*of*[*int*](https://docs.python.org/3/builtins/functions.html#int)) - the size of the window.
- **stride** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*of*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - the stride of the window.
Default: `kernel_size`.
- **ceil_mode** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*,**optional*) - when `True`, use `ceil` instead of
`floor` to compute the output shape. Default: `False`.

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

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/8fcaa153fa223ca9f7844513d86d4d30a0cf2533/torch/nn/modules/pooling.py#L1235)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)