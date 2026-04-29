# ReplicationPad2d

*class*torch.nn.modules.padding.ReplicationPad2d(*padding*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/nn/modules/padding.py#L590)

Pads the input tensor using replication of the input boundary.

For N-dimensional padding, use [`torch.nn.functional.pad()`](torch.nn.functional.pad.html#torch.nn.functional.pad).

Parameters:

**padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - the size of the padding. If is int, uses the same
padding in all boundaries. If a 4-tuple, uses (padding_left\text{padding\_left}padding_left,
padding_right\text{padding\_right}padding_right, padding_top\text{padding\_top}padding_top, padding_bottom\text{padding\_bottom}padding_bottom)
Note that the output dimensions must remain positive.

Shape:

- Input: (N,C,Hin,Win)(N, C, H_{in}, W_{in})(N,C,Hin​,Win​) or (C,Hin,Win)(C, H_{in}, W_{in})(C,Hin​,Win​).
- Output: (N,C,Hout,Wout)(N, C, H_{out}, W_{out})(N,C,Hout​,Wout​) or (C,Hout,Wout)(C, H_{out}, W_{out})(C,Hout​,Wout​), where

Hout=Hin+padding_top+padding_bottomH_{out} = H_{in} + \text{padding\_top} + \text{padding\_bottom}Hout​=Hin​+padding_top+padding_bottom

Wout=Win+padding_left+padding_rightW_{out} = W_{in} + \text{padding\_left} + \text{padding\_right}Wout​=Win​+padding_left+padding_right

Examples:

```
>>> m = nn.ReplicationPad2d(2)
>>> input = torch.arange(9, dtype=torch.float).reshape(1, 1, 3, 3)
>>> input
tensor([[[[0., 1., 2.],
 [3., 4., 5.],
 [6., 7., 8.]]]])
>>> m(input)
tensor([[[[0., 0., 0., 1., 2., 2., 2.],
 [0., 0., 0., 1., 2., 2., 2.],
 [0., 0., 0., 1., 2., 2., 2.],
 [3., 3., 3., 4., 5., 5., 5.],
 [6., 6., 6., 7., 8., 8., 8.],
 [6., 6., 6., 7., 8., 8., 8.],
 [6., 6., 6., 7., 8., 8., 8.]]]])
>>> # using different paddings for different sides
>>> m = nn.ReplicationPad2d((1, 1, 2, 0))
>>> m(input)
tensor([[[[0., 0., 1., 2., 2.],
 [0., 0., 1., 2., 2.],
 [0., 0., 1., 2., 2.],
 [3., 3., 4., 5., 5.],
 [6., 6., 7., 8., 8.]]]])
```