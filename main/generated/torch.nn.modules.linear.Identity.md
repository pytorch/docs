# Identity

*class*torch.nn.modules.linear.Identity(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/nn/modules/linear.py#L22)

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

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/nn/modules/linear.py#L46)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)