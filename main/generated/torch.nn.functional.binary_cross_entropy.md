# torch.nn.functional.binary_cross_entropy

torch.nn.functional.binary_cross_entropy(*input*, *target*, *weight=None*, *size_average=None*, *reduce=None*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/8df61039f8235b92b0ca250355cc296020f46e2d/torch/nn/functional.py#L3524)

Compute Binary Cross Entropy between the target and input probabilities.

See [`BCELoss`](torch.nn.BCELoss.html#torch.nn.BCELoss) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Tensor of arbitrary shape as probabilities.
- **target** ([*Tensor*](../tensors.html#torch.Tensor)) - Tensor of the same shape as input with values between 0 and 1.
- **weight** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - a manual rescaling weight
if provided it's repeated to match input tensor shape
- **size_average** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduce** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. `'none'`: no reduction will be applied,
`'mean'`: the sum of the output will be divided by the number of
elements in the output, `'sum'`: the output will be summed. Note: `size_average`
and `reduce` are in the process of being deprecated, and in the meantime,
specifying either of those two args will override `reduction`. Default: `'mean'`

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Examples:

```
>>> input = torch.randn(3, 2, requires_grad=True)
>>> target = torch.rand(3, 2, requires_grad=False)
>>> loss = F.binary_cross_entropy(torch.sigmoid(input), target)
>>> loss.backward()
```