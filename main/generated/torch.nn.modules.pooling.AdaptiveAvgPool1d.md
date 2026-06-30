# AdaptiveAvgPool1d

*class*torch.nn.modules.pooling.AdaptiveAvgPool1d(*output_size*)[[source]](https://github.com/pytorch/pytorch/blob/c8f2d26abd0de59995af555e80c82ca1221bc21b/torch/nn/modules/pooling.py#L1446)

Applies a 1D adaptive average pooling over an input signal composed of several input planes.

The output size is LoutL_{out}Lout​, for any input size.
The number of output features is equal to the number of input planes.

Parameters:

**output_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the target output size LoutL_{out}Lout​.

Shape:

- Input: (N,C,Lin)(N, C, L_{in})(N,C,Lin​) or (C,Lin)(C, L_{in})(C,Lin​).
- Output: (N,C,Lout)(N, C, L_{out})(N,C,Lout​) or (C,Lout)(C, L_{out})(C,Lout​), where
Lout=output_sizeL_{out}=\text{output\_size}Lout​=output_size.

Examples

```
>>> # target output size of 5
>>> m = nn.AdaptiveAvgPool1d(5)
>>> input = torch.randn(1, 64, 8)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/c8f2d26abd0de59995af555e80c82ca1221bc21b/torch/nn/modules/pooling.py#L1470)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)