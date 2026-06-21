# AdaptiveAvgPool2d

*class*torch.nn.AdaptiveAvgPool2d(*output_size*)[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/nn/modules/pooling.py#L1475)

Applies a 2D adaptive average pooling over an input signal composed of several input planes.

The output is of size H x W, for any input size.
The number of output features is equal to the number of input planes.

Parameters:

**output_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*|**None**|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*|**None**,*[*int*](https://docs.python.org/3/library/functions.html#int)*|**None**]*) - the target output size of the image of the form H x W.
Can be a tuple (H, W) or a single H for a square image H x H.
H and W can be either a `int`, or `None` which means the size will
be the same as that of the input.

Shape:

- Input: (N,C,Hin,Win)(N, C, H_{in}, W_{in})(N,C,Hin​,Win​) or (C,Hin,Win)(C, H_{in}, W_{in})(C,Hin​,Win​).
- Output: (N,C,S0,S1)(N, C, S_{0}, S_{1})(N,C,S0​,S1​) or (C,S0,S1)(C, S_{0}, S_{1})(C,S0​,S1​), where
S=output_sizeS=\text{output\_size}S=output_size.

Examples

```
>>> # target output size of 5x7
>>> m = nn.AdaptiveAvgPool2d((5, 7))
>>> input = torch.randn(1, 64, 8, 9)
>>> output = m(input)
>>> # target output size of 7x7 (square)
>>> m = nn.AdaptiveAvgPool2d(7)
>>> input = torch.randn(1, 64, 10, 9)
>>> output = m(input)
>>> # target output size of 10x7
>>> m = nn.AdaptiveAvgPool2d((None, 7))
>>> input = torch.randn(1, 64, 10, 9)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/nn/modules/pooling.py#L1510)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)