# ConstantPad2d

*class*torch.nn.modules.padding.ConstantPad2d(*padding*, *value*)[[source]](https://github.com/pytorch/pytorch/blob/0f5932e5e82c3a4da21331c6cf7cddf6bce55cff/torch/nn/modules/padding.py#L279)

Pads the input tensor boundaries with a constant value.

For N-dimensional padding, use [`torch.nn.functional.pad()`](torch.nn.functional.pad.html#torch.nn.functional.pad).

Parameters:

**padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - the size of the padding. If it is int, uses the same
padding in all boundaries. If a 4-tuple, uses (padding_left\text{padding\_left}padding_left,
padding_right\text{padding\_right}padding_right, padding_top\text{padding\_top}padding_top, padding_bottom\text{padding\_bottom}padding_bottom)

Shape:

- Input: (N,C,Hin,Win)(N, C, H_{in}, W_{in})(N,C,Hin​,Win​) or (C,Hin,Win)(C, H_{in}, W_{in})(C,Hin​,Win​).
- Output: (N,C,Hout,Wout)(N, C, H_{out}, W_{out})(N,C,Hout​,Wout​) or (C,Hout,Wout)(C, H_{out}, W_{out})(C,Hout​,Wout​), where

Hout=Hin+padding_top+padding_bottomH_{out} = H_{in} + \text{padding\_top} + \text{padding\_bottom}Hout​=Hin​+padding_top+padding_bottom

Wout=Win+padding_left+padding_rightW_{out} = W_{in} + \text{padding\_left} + \text{padding\_right}Wout​=Win​+padding_left+padding_right

Examples:

```
>>> m = nn.ConstantPad2d(2, 3.5)
>>> input = torch.randn(1, 2, 2)
>>> input
tensor([[[ 1.6585, 0.4320],
 [-0.8701, -0.4649]]])
>>> m(input)
tensor([[[ 3.5000, 3.5000, 3.5000, 3.5000, 3.5000, 3.5000],
 [ 3.5000, 3.5000, 3.5000, 3.5000, 3.5000, 3.5000],
 [ 3.5000, 3.5000, 1.6585, 0.4320, 3.5000, 3.5000],
 [ 3.5000, 3.5000, -0.8701, -0.4649, 3.5000, 3.5000],
 [ 3.5000, 3.5000, 3.5000, 3.5000, 3.5000, 3.5000],
 [ 3.5000, 3.5000, 3.5000, 3.5000, 3.5000, 3.5000]]])
>>> # using different paddings for different sides
>>> m = nn.ConstantPad2d((3, 0, 2, 1), 3.5)
>>> m(input)
tensor([[[ 3.5000, 3.5000, 3.5000, 3.5000, 3.5000],
 [ 3.5000, 3.5000, 3.5000, 3.5000, 3.5000],
 [ 3.5000, 3.5000, 3.5000, 1.6585, 0.4320],
 [ 3.5000, 3.5000, 3.5000, -0.8701, -0.4649],
 [ 3.5000, 3.5000, 3.5000, 3.5000, 3.5000]]])
```