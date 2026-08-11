# LPPool1d

*class*torch.nn.LPPool1d(*norm_type*, *kernel_size*, *stride=None*, *ceil_mode=False*)[[source]](https://github.com/pytorch/pytorch/blob/v2.14.0/torch/nn/modules/pooling.py#L1127)

Applies a 1D power-average pooling over an input signal composed of several input planes.

On each window, the function computed is:

f(X)=∑x∈Xxppf(X) = \sqrt[p]{\sum_{x \in X} x^{p}}

f(X)=p​x∈X∑​xp​

- At p = ∞\infty∞, one gets Max Pooling over absolute values
- At p = 1, one gets Sum Pooling (which is proportional to Average Pooling)

Note

If the sum to the power of p is zero, the gradient of this function is
not defined. This implementation will set the gradient to zero in this case.

Parameters:

- **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - a single int, the size of the window
- **stride** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - a single int, the stride of the window. Default value is `kernel_size`
- **ceil_mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - when True, will use ceil instead of floor to compute the output shape

Note

When `ceil_mode` is `True`, sliding windows may go off-bounds if they start within the
left padding or the input. Sliding windows that would start in the right padded region are ignored.

Shape:

- Input: (N,C,Lin)(N, C, L_{in})(N,C,Lin​) or (C,Lin)(C, L_{in})(C,Lin​).
- Output: (N,C,Lout)(N, C, L_{out})(N,C,Lout​) or (C,Lout)(C, L_{out})(C,Lout​), where

Lout=⌊Lin−kernel_sizestride+1⌋L_{out} = \left\lfloor\frac{L_{in} - \text{kernel\_size}}{\text{stride}} + 1\right\rfloor

Lout​=⌊strideLin​−kernel_size​+1⌋

Examples::

```
>>> # power-2 pool of window of length 3, with stride 2.
>>> m = nn.LPPool1d(2, 3, stride=2)
>>> input = torch.randn(20, 16, 50)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/v2.14.0/torch/nn/modules/pooling.py#L1167)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)