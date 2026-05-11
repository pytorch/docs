# Tanh

*class*torch.nn.Tanh(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/nn/modules/activation.py#L407)

Applies the Hyperbolic Tangent (Tanh) function element-wise.

Tanh is defined as:

Tanh(x)=tanh⁡(x)=exp⁡(x)−exp⁡(−x)exp⁡(x)+exp⁡(−x)\text{Tanh}(x) = \tanh(x) = \frac{\exp(x) - \exp(-x)} {\exp(x) + \exp(-x)}

Tanh(x)=tanh(x)=exp(x)+exp(−x)exp(x)−exp(−x)​
Shape:

- Input: (∗)(*)(∗), where ∗*∗ means any number of dimensions.
- Output: (∗)(*)(∗), same shape as the input.

![../_images/Tanh.png](../_images/Tanh.png)

Examples:

```
>>> m = nn.Tanh()
>>> input = torch.randn(2)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/nn/modules/activation.py#L428)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)