# Softsign

*class*torch.nn.modules.activation.Softsign(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/nn/modules/activation.py#L1657)

Applies the element-wise Softsign function.

SoftSign(x)=x1+∣x∣\text{SoftSign}(x) = \frac{x}{ 1 + |x|}

SoftSign(x)=1+∣x∣x​
Shape:

- Input: (∗)(*)(∗), where ∗*∗ means any number of dimensions.
- Output: (∗)(*)(∗), same shape as the input.

![../_images/Softsign.png](../_images/Softsign.png)

Examples:

```
>>> m = nn.Softsign()
>>> input = torch.randn(2)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/nn/modules/activation.py#L1676)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)