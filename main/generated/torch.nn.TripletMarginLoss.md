# TripletMarginLoss

*class*torch.nn.TripletMarginLoss(*margin=1.0*, *p=2.0*, *eps=1e-06*, *swap=False*, *size_average=None*, *reduce=None*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/nn/modules/loss.py#L1906)

Creates a criterion that measures the triplet loss given an input
tensors x1x1x1, x2x2x2, x3x3x3 and a margin with a value greater than 000.
This is used for measuring a relative similarity between samples. A triplet
is composed by a, p and n (i.e., anchor, positive examples and negative
examples respectively). The shapes of all input tensors should be
(N,D)(N, D)(N,D).

The distance swap is described in detail in the paper [Learning shallow
convolutional feature descriptors with triplet losses](https://bmva-archive.org.uk/bmvc/2016/papers/paper119/index.html) by
V. Balntas, E. Riba et al.

The loss function for each sample in the mini-batch is:

L(a,p,n)=max⁡{d(ai,pi)−d(ai,ni)+margin,0}L(a, p, n) = \max \{d(a_i, p_i) - d(a_i, n_i) + {\rm margin}, 0\}

L(a,p,n)=max{d(ai​,pi​)−d(ai​,ni​)+margin,0}

where

d(xi,yi)=∥xi−yi∥pd(x_i, y_i) = \left\lVert {\bf x}_i - {\bf y}_i \right\rVert_p

d(xi​,yi​)=∥xi​−yi​∥p​

The norm is calculated using the specified p value and a small constant ε\varepsilonε is
added for numerical stability.

See also [`TripletMarginWithDistanceLoss`](torch.nn.TripletMarginWithDistanceLoss.html#torch.nn.TripletMarginWithDistanceLoss), which computes the
triplet margin loss for input tensors using a custom distance function.

Parameters:

- **margin** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - Default: 111.
- **p** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The norm degree for pairwise distance. Default: 222.
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - Small constant for numerical stability. Default: 1e−61e-61e−6.
- **swap** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - The distance swap is described in detail in the paper
Learning shallow convolutional feature descriptors with triplet losses by
V. Balntas, E. Riba et al. Default: `False`.
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

- Input: (N,D)(N, D)(N,D) or (D)(D)(D) where DDD is the vector dimension.
- Output: A Tensor of shape (N)(N)(N) if `reduction` is `'none'` and
input shape is (N,D)(N, D)(N,D); a scalar otherwise.

Examples:

```
>>> triplet_loss = nn.TripletMarginLoss(margin=1.0, p=2, eps=1e-7)
>>> anchor = torch.randn(100, 128, requires_grad=True)
>>> positive = torch.randn(100, 128, requires_grad=True)
>>> negative = torch.randn(100, 128, requires_grad=True)
>>> output = triplet_loss(anchor, positive, negative)
>>> output.backward()
```

forward(*anchor*, *positive*, *negative*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/nn/modules/loss.py#L2002)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)