# AdaptiveAvgPool3d

*class*torch.nn.modules.pooling.AdaptiveAvgPool3d(*output_size*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/nn/modules/pooling.py#L1513)

Applies a 3D adaptive average pooling over an input signal composed of several input planes.

The output is of size D x H x W, for any input size.
The number of output features is equal to the number of input planes.

Parameters:

**output_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|**None**|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*|**None**,*[*int*](https://docs.python.org/3/library/functions.html#int)*|**None**,*[*int*](https://docs.python.org/3/library/functions.html#int)*|**None**]*) - the target output size of the form D x H x W.
Can be a tuple (D, H, W) or a single number D for a cube D x D x D.
D, H and W can be either a `int`, or `None` which means the size will
be the same as that of the input.

Shape:

- Input: (N,C,Din,Hin,Win)(N, C, D_{in}, H_{in}, W_{in})(N,C,Din​,Hin​,Win​) or (C,Din,Hin,Win)(C, D_{in}, H_{in}, W_{in})(C,Din​,Hin​,Win​).
- Output: (N,C,S0,S1,S2)(N, C, S_{0}, S_{1}, S_{2})(N,C,S0​,S1​,S2​) or (C,S0,S1,S2)(C, S_{0}, S_{1}, S_{2})(C,S0​,S1​,S2​),
where S=output_sizeS=\text{output\_size}S=output_size.

Examples

```
>>> # target output size of 5x7x9
>>> m = nn.AdaptiveAvgPool3d((5, 7, 9))
>>> input = torch.randn(1, 64, 8, 9, 10)
>>> output = m(input)
>>> # target output size of 7x7x7 (cube)
>>> m = nn.AdaptiveAvgPool3d(7)
>>> input = torch.randn(1, 64, 10, 9, 8)
>>> output = m(input)
>>> # target output size of 7x9x8
>>> m = nn.AdaptiveAvgPool3d((7, None, None))
>>> input = torch.randn(1, 64, 10, 9, 8)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/nn/modules/pooling.py#L1548)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)