# CircularPad3d

*class*torch.nn.CircularPad3d(*padding*)[[source]](https://github.com/pytorch/pytorch/blob/63f903c3d6b04c7cb1433d1d67e2b8e21c055bc7/torch/nn/modules/padding.py#L160)

Pads the input tensor using circular padding of the input boundary.

Tensor values at the beginning of the dimension are used to pad the end,
and values at the end are used to pad the beginning. If negative padding is
applied then the ends of the tensor get removed.

For N-dimensional padding, use [`torch.nn.functional.pad()`](torch.nn.functional.pad.html#torch.nn.functional.pad).

Parameters:

**padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - the size of the padding. If is int, uses the same
padding in all boundaries. If a 6-tuple, uses
(padding_left\text{padding\_left}padding_left, padding_right\text{padding\_right}padding_right,
padding_top\text{padding\_top}padding_top, padding_bottom\text{padding\_bottom}padding_bottom,
padding_front\text{padding\_front}padding_front, padding_back\text{padding\_back}padding_back)
Note that padding size should be less than or equal to the corresponding input dimension.

Shape:

- Input: (N,C,Din,Hin,Win)(N, C, D_{in}, H_{in}, W_{in})(N,C,Din​,Hin​,Win​) or (C,Din,Hin,Win)(C, D_{in}, H_{in}, W_{in})(C,Din​,Hin​,Win​).
- Output: (N,C,Dout,Hout,Wout)(N, C, D_{out}, H_{out}, W_{out})(N,C,Dout​,Hout​,Wout​) or (C,Dout,Hout,Wout)(C, D_{out}, H_{out}, W_{out})(C,Dout​,Hout​,Wout​),
where

Dout=Din+padding_front+padding_backD_{out} = D_{in} + \text{padding\_front} + \text{padding\_back}Dout​=Din​+padding_front+padding_back

Hout=Hin+padding_top+padding_bottomH_{out} = H_{in} + \text{padding\_top} + \text{padding\_bottom}Hout​=Hin​+padding_top+padding_bottom

Wout=Win+padding_left+padding_rightW_{out} = W_{in} + \text{padding\_left} + \text{padding\_right}Wout​=Win​+padding_left+padding_right

Examples:

```
>>> m = nn.CircularPad3d(3)
>>> input = torch.randn(16, 3, 8, 320, 480)
>>> output = m(input)
>>> # using different paddings for different sides
>>> m = nn.CircularPad3d((3, 3, 6, 6, 1, 1))
>>> output = m(input)
```