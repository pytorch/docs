# AvgPool1d

*class*torch.nn.modules.pooling.AvgPool1d(*kernel_size*, *stride=None*, *padding=0*, *ceil_mode=False*, *count_include_pad=True*)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/nn/modules/pooling.py#L595)

Applies a 1D average pooling over an input signal composed of several input planes.

In the simplest case, the output value of the layer with input size (N,C,L)(N, C, L)(N,C,L),
output (N,C,Lout)(N, C, L_{out})(N,C,Lout​) and `kernel_size` kkk
can be precisely described as:

out(Ni,Cj,l)=1k∑m=0k−1input(Ni,Cj,stride×l+m)\text{out}(N_i, C_j, l) = \frac{1}{k} \sum_{m=0}^{k-1}
 \text{input}(N_i, C_j, \text{stride} \times l + m)out(Ni​,Cj​,l)=k1​m=0∑k−1​input(Ni​,Cj​,stride×l+m)

If `padding` is non-zero, then the input is implicitly zero-padded on both sides
for `padding` number of points.

Note

When ceil_mode=True, sliding windows are allowed to go off-bounds if they start within the left padding
or the input. Sliding windows that would start in the right padded region are ignored.

Note

pad should be at most half of effective kernel size.

The parameters `kernel_size`, `stride`, `padding` can each be
an `int` or a one-element tuple.

Parameters:

- **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the size of the window
- **stride** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the stride of the window. Default value is `kernel_size`
- **padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - implicit zero padding to be added on both sides
- **ceil_mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - when True, will use ceil instead of floor to compute the output shape
- **count_include_pad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - when True, will include the zero-padding in the averaging calculation

Shape:

- Input: (N,C,Lin)(N, C, L_{in})(N,C,Lin​) or (C,Lin)(C, L_{in})(C,Lin​).
- Output: (N,C,Lout)(N, C, L_{out})(N,C,Lout​) or (C,Lout)(C, L_{out})(C,Lout​), where

Lout=⌊Lin+2×padding−kernel_sizestride+1⌋L_{out} = \left\lfloor \frac{L_{in} +
2 \times \text{padding} - \text{kernel\_size}}{\text{stride}} + 1\right\rfloor

Lout​=⌊strideLin​+2×padding−kernel_size​+1⌋

Per the note above, if `ceil_mode` is True and (Lout−1)×stride≥Lin+padding(L_{out} - 1) \times \text{stride} \geq L_{in}
+ \text{padding}(Lout​−1)×stride≥Lin​+padding, we skip the last window as it would start in the right padded region, resulting in
LoutL_{out}Lout​ being reduced by one.

Examples:

```
>>> # pool with window of size=3, stride=2
>>> m = nn.AvgPool1d(3, stride=2)
>>> m(torch.tensor([[[1., 2, 3, 4, 5, 6, 7]]]))
tensor([[[2., 4., 6.]]])
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/nn/modules/pooling.py#L668)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)