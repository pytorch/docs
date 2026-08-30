# MSELoss

*class*torch.nn.MSELoss(*size_average=None*, *reduce=None*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/nn/modules/loss.py#L567)

Creates a criterion that measures the mean squared error (squared L2 norm) between
each element in the input xxx and target yyy.

The unreduced (i.e. with `reduction` set to `'none'`) loss can be described as:

ℓ(x,y)=L={l1,...,lN}⊤,ln=(xn−yn)2,\ell(x, y) = L = \{l_1,\dots,l_N\}^\top, \quad
l_n = \left( x_n - y_n \right)^2,

ℓ(x,y)=L={l1​,...,lN​}⊤,ln​=(xn​−yn​)2,

where NNN is the batch size. If `reduction` is not `'none'`
(default `'mean'`), then:

ℓ(x,y)={mean⁡(L),if reduction='mean';sum⁡(L),if reduction='sum'.\ell(x, y) =
\begin{cases}
 \operatorname{mean}(L), & \text{if reduction} = \text{`mean';}\\
 \operatorname{sum}(L), & \text{if reduction} = \text{`sum'.}
\end{cases}

ℓ(x,y)={mean(L),sum(L),​if reduction='mean';if reduction='sum'.​

xxx and yyy are tensors of arbitrary shapes with a total
of NNN elements each.

The mean operation still operates over all the elements, and divides by NNN.

The division by NNN can be avoided if one sets `reduction = 'sum'`.

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

Examples

```
>>> loss = nn.MSELoss()
>>> input = torch.randn(3, 5, requires_grad=True)
>>> target = torch.randn(3, 5)
>>> output = loss(input, target)
>>> output.backward()
```

forward(*input*, *target*)[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/nn/modules/loss.py#L626)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)