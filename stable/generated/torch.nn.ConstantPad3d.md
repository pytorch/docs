# ConstantPad3d

*class*torch.nn.ConstantPad3d(*padding*, *value*)[[source]](https://github.com/pytorch/pytorch/blob/v2.14.0/torch/nn/modules/padding.py#L331)

Pads the input tensor boundaries with a constant value.

For N-dimensional padding, use [`torch.nn.functional.pad()`](torch.nn.functional.pad.html#torch.nn.functional.pad).

Parameters:

**padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - the size of the padding. If it is int, uses the same
padding in all boundaries. If a 6-tuple, uses
(padding_left\text{padding\_left}padding_left, padding_right\text{padding\_right}padding_right,
padding_top\text{padding\_top}padding_top, padding_bottom\text{padding\_bottom}padding_bottom,
padding_front\text{padding\_front}padding_front, padding_back\text{padding\_back}padding_back)

Shape:

- Input: (N,C,Din,Hin,Win)(N, C, D_{in}, H_{in}, W_{in})(N,C,Din​,Hin​,Win​) or (C,Din,Hin,Win)(C, D_{in}, H_{in}, W_{in})(C,Din​,Hin​,Win​).
- Output: (N,C,Dout,Hout,Wout)(N, C, D_{out}, H_{out}, W_{out})(N,C,Dout​,Hout​,Wout​) or
(C,Dout,Hout,Wout)(C, D_{out}, H_{out}, W_{out})(C,Dout​,Hout​,Wout​), where

Dout=Din+padding_front+padding_backD_{out} = D_{in} + \text{padding\_front} + \text{padding\_back}Dout​=Din​+padding_front+padding_back

Hout=Hin+padding_top+padding_bottomH_{out} = H_{in} + \text{padding\_top} + \text{padding\_bottom}Hout​=Hin​+padding_top+padding_bottom

Wout=Win+padding_left+padding_rightW_{out} = W_{in} + \text{padding\_left} + \text{padding\_right}Wout​=Win​+padding_left+padding_right

Examples:

```
>>> m = nn.ConstantPad3d(3, 3.5)
>>> input = torch.randn(16, 3, 10, 20, 30)
>>> output = m(input)
>>> # using different paddings for different sides
>>> m = nn.ConstantPad3d((3, 3, 6, 6, 0, 1), 3.5)
>>> output = m(input)
```