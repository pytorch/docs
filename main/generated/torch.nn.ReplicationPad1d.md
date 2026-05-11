# ReplicationPad1d

*class*torch.nn.ReplicationPad1d(*padding*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/nn/modules/padding.py#L547)

Pads the input tensor using replication of the input boundary.

For N-dimensional padding, use [`torch.nn.functional.pad()`](torch.nn.functional.pad.html#torch.nn.functional.pad).

Parameters:

**padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - the size of the padding. If is int, uses the same
padding in all boundaries. If a 2-tuple, uses
(padding_left\text{padding\_left}padding_left, padding_right\text{padding\_right}padding_right)
Note that the output dimensions must remain positive.

Shape:

- Input: (C,Win)(C, W_{in})(C,Win​) or (N,C,Win)(N, C, W_{in})(N,C,Win​).
- Output: (C,Wout)(C, W_{out})(C,Wout​) or (N,C,Wout)(N, C, W_{out})(N,C,Wout​), where

Wout=Win+padding_left+padding_rightW_{out} = W_{in} + \text{padding\_left} + \text{padding\_right}Wout​=Win​+padding_left+padding_right

Examples:

```
>>> m = nn.ReplicationPad1d(2)
>>> input = torch.arange(8, dtype=torch.float).reshape(1, 2, 4)
>>> input
tensor([[[0., 1., 2., 3.],
 [4., 5., 6., 7.]]])
>>> m(input)
tensor([[[0., 0., 0., 1., 2., 3., 3., 3.],
 [4., 4., 4., 5., 6., 7., 7., 7.]]])
>>> # using different paddings for different sides
>>> m = nn.ReplicationPad1d((3, 1))
>>> m(input)
tensor([[[0., 0., 0., 0., 1., 2., 3., 3.],
 [4., 4., 4., 4., 5., 6., 7., 7.]]])
```