# ZeroPad2d

*class*torch.nn.modules.padding.ZeroPad2d(*padding*)[[source]](https://github.com/pytorch/pytorch/blob/54541f51bee1b9b66a0ecb11e69067a677a60487/torch/nn/modules/padding.py#L743)

Pads the input tensor boundaries with zero.

For N-dimensional padding, use [`torch.nn.functional.pad()`](torch.nn.functional.pad.html#torch.nn.functional.pad).

Parameters:

**padding** ([*int*](https://docs.python.org/3/library/functions.html#int)*,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - the size of the padding. If is int, uses the same
padding in all boundaries. If a 4-tuple, uses (padding_left\text{padding\_left}padding_left,
padding_right\text{padding\_right}padding_right, padding_top\text{padding\_top}padding_top, padding_bottom\text{padding\_bottom}padding_bottom)

Shape:

- Input: (N,C,Hin,Win)(N, C, H_{in}, W_{in})(N,C,Hin​,Win​) or (C,Hin,Win)(C, H_{in}, W_{in})(C,Hin​,Win​).
- Output: (N,C,Hout,Wout)(N, C, H_{out}, W_{out})(N,C,Hout​,Wout​) or (C,Hout,Wout)(C, H_{out}, W_{out})(C,Hout​,Wout​), where

Hout=Hin+padding_top+padding_bottomH_{out} = H_{in} + \text{padding\_top} + \text{padding\_bottom}Hout​=Hin​+padding_top+padding_bottom

Wout=Win+padding_left+padding_rightW_{out} = W_{in} + \text{padding\_left} + \text{padding\_right}Wout​=Win​+padding_left+padding_right

Examples:

```
>>> m = nn.ZeroPad2d(2)
>>> input = torch.randn(1, 1, 3, 3)
>>> input
tensor([[[[-0.1678, -0.4418, 1.9466],
 [ 0.9604, -0.4219, -0.5241],
 [-0.9162, -0.5436, -0.6446]]]])
>>> m(input)
tensor([[[[ 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
 [ 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
 [ 0.0000, 0.0000, -0.1678, -0.4418, 1.9466, 0.0000, 0.0000],
 [ 0.0000, 0.0000, 0.9604, -0.4219, -0.5241, 0.0000, 0.0000],
 [ 0.0000, 0.0000, -0.9162, -0.5436, -0.6446, 0.0000, 0.0000],
 [ 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
 [ 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000]]]])
>>> # using different paddings for different sides
>>> m = nn.ZeroPad2d((1, 1, 2, 0))
>>> m(input)
tensor([[[[ 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
 [ 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
 [ 0.0000, -0.1678, -0.4418, 1.9466, 0.0000],
 [ 0.0000, 0.9604, -0.4219, -0.5241, 0.0000],
 [ 0.0000, -0.9162, -0.5436, -0.6446, 0.0000]]]])
```

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/54541f51bee1b9b66a0ecb11e69067a677a60487/torch/nn/modules/padding.py#L793)

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)