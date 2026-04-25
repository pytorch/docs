# MultiMarginLoss

*class*torch.nn.modules.loss.MultiMarginLoss(*p=1*, *margin=1.0*, *weight=None*, *size_average=None*, *reduce=None*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/460262116930c46e505df88f1fcd347abab536c4/torch/nn/modules/loss.py#L1599)

Creates a criterion that optimizes a multi-class classification hinge
loss (margin-based loss) between input xxx (a 2D mini-batch Tensor) and
output yyy (which is a 1D tensor of target class indices,
0≤y≤x.size(1)−10 \leq y \leq \text{x.size}(1)-10≤y≤x.size(1)−1):

For each mini-batch sample, the loss in terms of the 1D input xxx and scalar
output yyy is:

loss(x,y)=∑imax⁡(0,margin−x[y]+x[i])px.size(0)\text{loss}(x, y) = \frac{\sum_i \max(0, \text{margin} - x[y] + x[i])^p}{\text{x.size}(0)}

loss(x,y)=x.size(0)∑i​max(0,margin−x[y]+x[i])p​

where i∈{0,  ⋯ ,  x.size(0)−1}i \in \left\{0, \; \cdots , \; \text{x.size}(0) - 1\right\}i∈{0,⋯,x.size(0)−1}
and i≠yi \neq yi=y.

Optionally, you can give non-equal weighting on the classes by passing
a 1D `weight` tensor into the constructor.

The loss function then becomes:

loss(x,y)=∑iw[y]∗max⁡(0,margin−x[y]+x[i])px.size(0)\text{loss}(x, y) = \frac{\sum_i w[y] * \max(0, \text{margin} - x[y] + x[i])^p}{\text{x.size}(0)}

loss(x,y)=x.size(0)∑i​w[y]∗max(0,margin−x[y]+x[i])p​
Parameters:

- **p** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Has a default value of 111. 111 and 222
are the only supported values.
- **margin** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - Has a default value of 111.
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

- Input: (N,C)(N, C)(N,C) or (C)(C)(C), where NNN is the batch size and CCC is the number of classes.
- Target: (N)(N)(N) or ()()(), where each value is 0≤targets[i]≤C−10 \leq \text{targets}[i] \leq C-10≤targets[i]≤C−1.
- Output: scalar. If `reduction` is `'none'`, then same shape as the target.

Examples

```
>>> loss = nn.MultiMarginLoss()
>>> x = torch.tensor([[0.1, 0.2, 0.4, 0.8]])
>>> y = torch.tensor([3])
>>> # 0.25 * ((1-(0.8-0.1)) + (1-(0.8-0.2)) + (1-(0.8-0.4)))
>>> loss(x, y)
tensor(0.32...)
```

forward(*input*, *target*)[[source]](https://github.com/pytorch/pytorch/blob/460262116930c46e505df88f1fcd347abab536c4/torch/nn/modules/loss.py#L1683)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)