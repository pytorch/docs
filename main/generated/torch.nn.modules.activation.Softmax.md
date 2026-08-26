# Softmax

*class*torch.nn.modules.activation.Softmax(*dim=None*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/nn/modules/activation.py#L1766)

Applies the Softmax function to an n-dimensional input Tensor.

Rescales them so that the elements of the n-dimensional output Tensor
lie in the range [0,1] and sum to 1.

Softmax is defined as:

Softmax(xi)=exp⁡(xi)∑jexp⁡(xj)\text{Softmax}(x_{i}) = \frac{\exp(x_i)}{\sum_j \exp(x_j)}

Softmax(xi​)=∑j​exp(xj​)exp(xi​)​

When the input Tensor is a sparse tensor then the unspecified
values are treated as `-inf`.

Shape:

- Input: (∗)(*)(∗) where * means, any number of additional
dimensions
- Output: (∗)(*)(∗), same shape as the input

Returns:

a Tensor of the same dimension and shape as the input with
values in the range [0, 1]

Parameters:

**dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - A dimension along which Softmax will be computed (so every slice
along dim will sum to 1).

Return type:

None

Note

This module doesn't work directly with NLLLoss,
which expects the Log to be computed between the Softmax and itself.
Use LogSoftmax instead (it's faster and has better numerical properties).

Examples:

```
>>> m = nn.Softmax(dim=1)
>>> input = torch.randn(2, 3)
>>> output = m(input)
```

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/nn/modules/activation.py#L1826)

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/nn/modules/activation.py#L1820)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)