# LogSigmoid

*class*torch.nn.modules.activation.LogSigmoid(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/nn/modules/activation.py#L933)

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

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/nn/modules/activation.py#L952)

Run forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)