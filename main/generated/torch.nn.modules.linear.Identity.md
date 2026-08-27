# Identity

*class*torch.nn.modules.linear.Identity(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/nn/modules/linear.py#L22)

A placeholder identity operator that is argument-insensitive.

Parameters:

- **args** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)) - any argument (unused)
- **kwargs** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)) - any keyword argument (unused)

Shape:

- Input: (∗)(*)(∗), where ∗*∗ means any number of dimensions.
- Output: (∗)(*)(∗), same shape as the input.

Examples:

```
>>> m = nn.Identity(54, unused_argument1=0.1, unused_argument2=False)
>>> input = torch.randn(128, 20)
>>> output = m(input)
>>> print(output.size())
torch.Size([128, 20])
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/nn/modules/linear.py#L46)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)