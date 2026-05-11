# ReflectionPad3d

*class*torch.nn.ReflectionPad3d(*padding*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/nn/modules/padding.py#L480)

Pads the input tensor using the reflection of the input boundary.

For N-dimensional padding, use [`torch.nn.functional.pad()`](torch.nn.functional.pad.html#torch.nn.functional.pad).

Parameters:

**padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - the size of the padding. If is int, uses the same
padding in all boundaries. If a 6-tuple, uses
(padding_left\text{padding\_left}padding_left, padding_right\text{padding\_right}padding_right,
padding_top\text{padding\_top}padding_top, padding_bottom\text{padding\_bottom}padding_bottom,
padding_front\text{padding\_front}padding_front, padding_back\text{padding\_back}padding_back)
Note that padding size should be less than the corresponding input dimension.

Shape:

- Input: (N,C,Din,Hin,Win)(N, C, D_{in}, H_{in}, W_{in})(N,C,Din​,Hin​,Win​) or (C,Din,Hin,Win)(C, D_{in}, H_{in}, W_{in})(C,Din​,Hin​,Win​).
- Output: (N,C,Dout,Hout,Wout)(N, C, D_{out}, H_{out}, W_{out})(N,C,Dout​,Hout​,Wout​) or (C,Dout,Hout,Wout)(C, D_{out}, H_{out}, W_{out})(C,Dout​,Hout​,Wout​),
where

Dout=Din+padding_front+padding_backD_{out} = D_{in} + \text{padding\_front} + \text{padding\_back}Dout​=Din​+padding_front+padding_back

Hout=Hin+padding_top+padding_bottomH_{out} = H_{in} + \text{padding\_top} + \text{padding\_bottom}Hout​=Hin​+padding_top+padding_bottom

Wout=Win+padding_left+padding_rightW_{out} = W_{in} + \text{padding\_left} + \text{padding\_right}Wout​=Win​+padding_left+padding_right

Examples:

```
>>> m = nn.ReflectionPad3d(1)
>>> input = torch.arange(8, dtype=torch.float).reshape(1, 1, 2, 2, 2)
>>> m(input)
tensor([[[[[7., 6., 7., 6.],
 [5., 4., 5., 4.],
 [7., 6., 7., 6.],
 [5., 4., 5., 4.]],
 [[3., 2., 3., 2.],
 [1., 0., 1., 0.],
 [3., 2., 3., 2.],
 [1., 0., 1., 0.]],
 [[7., 6., 7., 6.],
 [5., 4., 5., 4.],
 [7., 6., 7., 6.],
 [5., 4., 5., 4.]],
 [[3., 2., 3., 2.],
 [1., 0., 1., 0.],
 [3., 2., 3., 2.],
 [1., 0., 1., 0.]]]]])
```