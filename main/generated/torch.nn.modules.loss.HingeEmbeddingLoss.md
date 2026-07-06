# HingeEmbeddingLoss

*class*torch.nn.modules.loss.HingeEmbeddingLoss(*margin=1.0*, *size_average=None*, *reduce=None*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/a059c4af8933be96044a8625669869fe560baf61/torch/nn/modules/loss.py#L847)

Measures the loss given an input tensor xxx and a labels tensor yyy
(containing 1 or -1).
This is usually used for measuring whether two inputs are similar or
dissimilar, e.g. using the L1 pairwise distance as xxx, and is typically
used for learning nonlinear embeddings or semi-supervised learning.

The loss function for nnn-th sample in the mini-batch is

ln={xn,if  yn=1,max⁡{0,margin−xn},if  yn=−1,l_n = \begin{cases}
 x_n, & \text{if}\; y_n = 1,\\
 \max \{0, margin - x_n\}, & \text{if}\; y_n = -1,
\end{cases}

ln​={xn​,max{0,margin−xn​},​ifyn​=1,ifyn​=−1,​

and the total loss functions is

ℓ(x,y)={mean⁡(L),if reduction='mean';sum⁡(L),if reduction='sum'.\ell(x, y) = \begin{cases}
 \operatorname{mean}(L), & \text{if reduction} = \text{`mean';}\\
 \operatorname{sum}(L), & \text{if reduction} = \text{`sum'.}
\end{cases}

ℓ(x,y)={mean(L),sum(L),​if reduction='mean';if reduction='sum'.​

where L={l1,...,lN}⊤L = \{l_1,\dots,l_N\}^\topL={l1​,...,lN​}⊤.

Parameters:

- **margin** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - Has a default value of 1.
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

- Input: (∗)(*)(∗) where ∗*∗ means, any number of dimensions. The sum operation
operates over all the elements.
- Target: (∗)(*)(∗), same shape as the input
- Output: scalar. If `reduction` is `'none'`, then same shape as the input

Examples

```
>>> loss = nn.HingeEmbeddingLoss()
>>> input = torch.randn(3, 5, requires_grad=True)
>>> target = torch.randn(3, 5).sign()
>>> output = loss(input, target)
>>> output.backward()
```

forward(*input*, *target*)[[source]](https://github.com/pytorch/pytorch/blob/a059c4af8933be96044a8625669869fe560baf61/torch/nn/modules/loss.py#L918)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)