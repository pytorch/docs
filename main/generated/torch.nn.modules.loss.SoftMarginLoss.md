# SoftMarginLoss

*class*torch.nn.modules.loss.SoftMarginLoss(*size_average=None*, *reduce=None*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/56964c25c21235cf3a06679d2e400195087f64fb/torch/nn/modules/loss.py#L1151)

Creates a criterion that optimizes a two-class classification
logistic loss between input tensor xxx and target tensor yyy
(containing 1 or -1).

loss(x,y)=∑ilog⁡(1+exp⁡(−y[i]∗x[i]))x.nelement()\text{loss}(x, y) = \sum_i \frac{\log(1 + \exp(-y[i]*x[i]))}{\text{x.nelement}()}

loss(x,y)=i∑​x.nelement()log(1+exp(−y[i]∗x[i]))​
Parameters:

- **size_average** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`). By default,
the losses are averaged over each loss element in the batch. Note that for
some losses, there are multiple elements per sample. If the field `size_average`
is set to `False`, the losses are instead summed for each minibatch. Ignored
when `reduce` is `False`. Default: `True`
- **reduce** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`). By default, the
losses are averaged or summed over observations for each minibatch depending
on `size_average`. When `reduce` is `False`, returns a loss per
batch element instead and ignores `size_average`. Default: `True`
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. `'none'`: no reduction will be applied,
`'mean'`: the sum of the output will be divided by the number of
elements in the output, `'sum'`: the output will be summed. Note: `size_average`
and `reduce` are in the process of being deprecated, and in the meantime,
specifying either of those two args will override `reduction`. Default: `'mean'`

Shape:

- Input: (∗)(*)(∗), where ∗*∗ means any number of dimensions.
- Target: (∗)(*)(∗), same shape as the input.
- Output: scalar. If `reduction` is `'none'`, then (∗)(*)(∗), same
shape as input.

Examples

```
>>> loss = nn.SoftMarginLoss()
>>> input = torch.randn(3, 5, requires_grad=True)
>>> target = torch.randn(3, 5).sign()
>>> output = loss(input, target)
>>> output.backward()
```

forward(*input*, *target*)[[source]](https://github.com/pytorch/pytorch/blob/56964c25c21235cf3a06679d2e400195087f64fb/torch/nn/modules/loss.py#L1193)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)