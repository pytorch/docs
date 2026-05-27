# CircularPad2d

*class*torch.nn.modules.padding.CircularPad2d(*padding*)[[source]](https://github.com/pytorch/pytorch/blob/34424f27313fbcddaafe4a1a855000f17e05a260/torch/nn/modules/padding.py#L99)

Pads the input tensor using circular padding of the input boundary.

Tensor values at the beginning of the dimension are used to pad the end,
and values at the end are used to pad the beginning. If negative padding is
applied then the ends of the tensor get removed.

For N-dimensional padding, use [`torch.nn.functional.pad()`](torch.nn.functional.pad.html#torch.nn.functional.pad).

Parameters:

**padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - the size of the padding. If is int, uses the same
padding in all boundaries. If a 4-tuple, uses (padding_left\text{padding\_left}padding_left,
padding_right\text{padding\_right}padding_right, padding_top\text{padding\_top}padding_top, padding_bottom\text{padding\_bottom}padding_bottom)
Note that padding size should be less than or equal to the corresponding input dimension.

Shape:

- Input: (N,C,Hin,Win)(N, C, H_{in}, W_{in})(N,C,Hin​,Win​) or (C,Hin,Win)(C, H_{in}, W_{in})(C,Hin​,Win​).
- Output: (N,C,Hout,Wout)(N, C, H_{out}, W_{out})(N,C,Hout​,Wout​) or (C,Hout,Wout)(C, H_{out}, W_{out})(C,Hout​,Wout​), where

Hout=Hin+padding_top+padding_bottomH_{out} = H_{in} + \text{padding\_top} + \text{padding\_bottom}Hout​=Hin​+padding_top+padding_bottom

Wout=Win+padding_left+padding_rightW_{out} = W_{in} + \text{padding\_left} + \text{padding\_right}Wout​=Win​+padding_left+padding_right

Examples:

```
>>> m = nn.CircularPad2d(2)
>>> input = torch.arange(9, dtype=torch.float).reshape(1, 1, 3, 3)
>>> input
tensor([[[[0., 1., 2.],
 [3., 4., 5.],
 [6., 7., 8.]]]])
>>> m(input)
tensor([[[[4., 5., 3., 4., 5., 3., 4.],
 [7., 8., 6., 7., 8., 6., 7.],
 [1., 2., 0., 1., 2., 0., 1.],
 [4., 5., 3., 4., 5., 3., 4.],
 [7., 8., 6., 7., 8., 6., 7.],
 [1., 2., 0., 1., 2., 0., 1.],
 [4., 5., 3., 4., 5., 3., 4.]]]])
>>> # using different paddings for different sides
>>> m = nn.CircularPad2d((1, 1, 2, 0))
>>> m(input)
tensor([[[[5., 3., 4., 5., 3.],
 [8., 6., 7., 8., 6.],
 [2., 0., 1., 2., 0.],
 [5., 3., 4., 5., 3.],
 [8., 6., 7., 8., 6.]]]])
```