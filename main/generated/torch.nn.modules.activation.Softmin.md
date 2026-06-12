# Softmin

*class*torch.nn.modules.activation.Softmin(*dim=None*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/nn/modules/activation.py#L1709)

Applies the Softmin function to an n-dimensional input Tensor.

Rescales them so that the elements of the n-dimensional output Tensor
lie in the range [0, 1] and sum to 1.

Softmin is defined as:

Softmin(xi)=exp⁡(−xi)∑jexp⁡(−xj)\text{Softmin}(x_{i}) = \frac{\exp(-x_i)}{\sum_j \exp(-x_j)}

Softmin(xi​)=∑j​exp(−xj​)exp(−xi​)​
Shape:

- Input: (∗)(*)(∗) where * means, any number of additional
dimensions
- Output: (∗)(*)(∗), same shape as the input

Parameters:

**dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - A dimension along which Softmin will be computed (so every slice
along dim will sum to 1).

Returns:

a Tensor of the same dimension and shape as the input, with
values in the range [0, 1]

Return type:

None

Examples:

```
>>> m = nn.Softmin(dim=1)
>>> input = torch.randn(2, 3)
>>> output = m(input)
```

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/nn/modules/activation.py#L1758)

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/nn/modules/activation.py#L1752)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)