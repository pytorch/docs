# Tanhshrink

*class*torch.nn.Tanhshrink(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/nn/modules/activation.py#L1683)

Applies the element-wise Tanhshrink function.

Tanhshrink(x)=x−tanh⁡(x)\text{Tanhshrink}(x) = x - \tanh(x)

Tanhshrink(x)=x−tanh(x)
Shape:

- Input: (∗)(*)(∗), where ∗*∗ means any number of dimensions.
- Output: (∗)(*)(∗), same shape as the input.

![../_images/Tanhshrink.png](../_images/Tanhshrink.png)

Examples:

```
>>> m = nn.Tanhshrink()
>>> input = torch.randn(2)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/nn/modules/activation.py#L1702)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)