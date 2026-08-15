# LogSoftmax

*class*torch.nn.modules.activation.LogSoftmax(*dim=None*)[[source]](https://github.com/pytorch/pytorch/blob/55dfacc69b3a9156f68cfe07b61553e4bdc7de29/torch/nn/modules/activation.py#L1866)

Applies the log⁡(Softmax(x))\log(\text{Softmax}(x))log(Softmax(x)) function to an n-dimensional input Tensor.

The LogSoftmax formulation can be simplified as:

LogSoftmax(xi)=log⁡(exp⁡(xi)∑jexp⁡(xj))\text{LogSoftmax}(x_{i}) = \log\left(\frac{\exp(x_i) }{ \sum_j \exp(x_j)} \right)

LogSoftmax(xi​)=log(∑j​exp(xj​)exp(xi​)​)
Shape:

- Input: (∗)(*)(∗) where * means, any number of additional
dimensions
- Output: (∗)(*)(∗), same shape as the input

Parameters:

**dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - A dimension along which LogSoftmax will be computed.

Returns:

a Tensor of the same dimension and shape as the input with
values in the range [-inf, 0)

Return type:

None

Examples:

```
>>> m = nn.LogSoftmax(dim=1)
>>> input = torch.randn(2, 3)
>>> output = m(input)
```

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/55dfacc69b3a9156f68cfe07b61553e4bdc7de29/torch/nn/modules/activation.py#L1913)

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/55dfacc69b3a9156f68cfe07b61553e4bdc7de29/torch/nn/modules/activation.py#L1907)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)