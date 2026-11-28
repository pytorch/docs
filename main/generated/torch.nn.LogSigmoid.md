# LogSigmoid

*class*torch.nn.LogSigmoid(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/nn/modules/activation.py#L936)

Applies the Logsigmoid function element-wise.

LogSigmoid(x)=log⁡(11+exp⁡(−x))\text{LogSigmoid}(x) = \log\left(\frac{ 1 }{ 1 + \exp(-x)}\right)

LogSigmoid(x)=log(1+exp(−x)1​)
Shape:

- Input: (∗)(*)(∗), where ∗*∗ means any number of dimensions.
- Output: (∗)(*)(∗), same shape as the input.

![../_images/LogSigmoid.png](../_images/LogSigmoid.png)

Examples:

```
>>> m = nn.LogSigmoid()
>>> input = torch.randn(2)
>>> output = m(input)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/nn/modules/activation.py#L955)

Run forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)