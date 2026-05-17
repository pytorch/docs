# ReflectionPad1d

*class*torch.nn.modules.padding.ReflectionPad1d(*padding*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/nn/modules/padding.py#L383)

Pads the input tensor using the reflection of the input boundary.

For N-dimensional padding, use [`torch.nn.functional.pad()`](torch.nn.functional.pad.html#torch.nn.functional.pad).

Parameters:

**padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - the size of the padding. If is int, uses the same
padding in all boundaries. If a 2-tuple, uses
(padding_left\text{padding\_left}padding_left, padding_right\text{padding\_right}padding_right)
Note that padding size should be less than the corresponding input dimension.

Shape:

- Input: (C,Win)(C, W_{in})(C,Win​) or (N,C,Win)(N, C, W_{in})(N,C,Win​).
- Output: (C,Wout)(C, W_{out})(C,Wout​) or (N,C,Wout)(N, C, W_{out})(N,C,Wout​), where

Wout=Win+padding_left+padding_rightW_{out} = W_{in} + \text{padding\_left} + \text{padding\_right}Wout​=Win​+padding_left+padding_right

Examples:

```
>>> m = nn.ReflectionPad1d(2)
>>> input = torch.arange(8, dtype=torch.float).reshape(1, 2, 4)
>>> input
tensor([[[0., 1., 2., 3.],
 [4., 5., 6., 7.]]])
>>> m(input)
tensor([[[2., 1., 0., 1., 2., 3., 2., 1.],
 [6., 5., 4., 5., 6., 7., 6., 5.]]])
>>> # using different paddings for different sides
>>> m = nn.ReflectionPad1d((3, 1))
>>> m(input)
tensor([[[3., 2., 1., 0., 1., 2., 3., 2.],
 [7., 6., 5., 4., 5., 6., 7., 6.]]])
```