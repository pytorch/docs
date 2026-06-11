# MultiLabelSoftMarginLoss

*class*torch.nn.MultiLabelSoftMarginLoss(*weight=None*, *size_average=None*, *reduce=None*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/63f903c3d6b04c7cb1433d1d67e2b8e21c055bc7/torch/nn/modules/loss.py#L1615)

Creates a criterion that optimizes a multi-label one-versus-all
loss based on max-entropy, between input xxx and target yyy of size
(N,C)(N, C)(N,C).
For each sample in the minibatch:

loss(x,y)=−1C∗∑iy[i]∗log⁡((1+exp⁡(−x[i]))−1)+(1−y[i])∗log⁡(exp⁡(−x[i])(1+exp⁡(−x[i])))loss(x, y) = - \frac{1}{C} * \sum_i y[i] * \log((1 + \exp(-x[i]))^{-1})
 + (1-y[i]) * \log\left(\frac{\exp(-x[i])}{(1 + \exp(-x[i]))}\right)

loss(x,y)=−C1​∗i∑​y[i]∗log((1+exp(−x[i]))−1)+(1−y[i])∗log((1+exp(−x[i]))exp(−x[i])​)

where i∈{0,  ⋯ ,  x.nElement()−1}i \in \left\{0, \; \cdots , \; \text{x.nElement}() - 1\right\}i∈{0,⋯,x.nElement()−1},
y[i]∈{0,  1}y[i] \in \left\{0, \; 1\right\}y[i]∈{0,1}.

Parameters:

- **weight** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - a manual rescaling weight given to each
class. If given, it has to be a Tensor of size C. Otherwise, it is
treated as if having all ones.
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

- Input: (N,C)(N, C)(N,C) where N is the batch size and C is the number of classes.
- Target: (N,C)(N, C)(N,C), label targets must have the same shape as the input.
- Output: scalar. If `reduction` is `'none'`, then (N)(N)(N).

Examples

```
>>> loss = nn.MultiLabelSoftMarginLoss()
>>> input = torch.randn(3, 5, requires_grad=True)
>>> target = torch.empty(3, 5).random_(2)
>>> output = loss(input, target)
>>> output.backward()
```

forward(*input*, *target*)[[source]](https://github.com/pytorch/pytorch/blob/63f903c3d6b04c7cb1433d1d67e2b8e21c055bc7/torch/nn/modules/loss.py#L1664)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)