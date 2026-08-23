# Softmax2d

*class*torch.nn.modules.activation.Softmax2d(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/nn/modules/activation.py#L1833)

Applies SoftMax over features to each spatial location.

When given an image of `Channels x Height x Width`, it will
apply Softmax to each location (Channels,hi,wj)(Channels, h_i, w_j)(Channels,hi​,wj​)

Shape:

- Input: (N,C,H,W)(N, C, H, W)(N,C,H,W) or (C,H,W)(C, H, W)(C,H,W).
- Output: (N,C,H,W)(N, C, H, W)(N,C,H,W) or (C,H,W)(C, H, W)(C,H,W) (same shape as input)

Returns:

a Tensor of the same dimension and shape as the input with
values in the range [0, 1]

Return type:

None

Examples:

```
>>> m = nn.Softmax2d()
>>> # you softmax over the 2nd dimension
>>> input = torch.randn(2, 3, 12, 13)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/nn/modules/activation.py#L1855)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)