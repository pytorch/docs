# SmoothL1Loss

*class*torch.nn.modules.loss.SmoothL1Loss(*size_average=None*, *reduce=None*, *reduction='mean'*, *beta=1.0*)[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/nn/modules/loss.py#L988)

Creates a criterion that uses a squared term if the absolute
element-wise error falls below beta and an L1 term otherwise.
It is less sensitive to outliers than [`torch.nn.MSELoss`](torch.nn.MSELoss.html#torch.nn.MSELoss) and in some cases
prevents exploding gradients (e.g. see the paper [Fast R-CNN](https://arxiv.org/abs/1504.08083) by Ross Girshick).

For a batch of size NNN, the unreduced loss can be described as:

ℓ(x,y)=L={l1,...,lN}T\ell(x, y) = L = \{l_1, ..., l_N\}^T

ℓ(x,y)=L={l1​,...,lN​}T

with

ln={0.5(xn−yn)2/beta,if ∣xn−yn∣<beta∣xn−yn∣−0.5∗beta,otherwise l_n = \begin{cases}
0.5 (x_n - y_n)^2 / beta, & \text{if } |x_n - y_n| < beta \\
|x_n - y_n| - 0.5 * beta, & \text{otherwise }
\end{cases}

ln​={0.5(xn​−yn​)2/beta,∣xn​−yn​∣−0.5∗beta,​if ∣xn​−yn​∣<betaotherwise ​

If reduction is not none, then:

ℓ(x,y)={mean⁡(L),if reduction='mean';sum⁡(L),if reduction='sum'.\ell(x, y) =
\begin{cases}
 \operatorname{mean}(L), & \text{if reduction} = \text{`mean';}\\
 \operatorname{sum}(L), & \text{if reduction} = \text{`sum'.}
\end{cases}

ℓ(x,y)={mean(L),sum(L),​if reduction='mean';if reduction='sum'.​

Note

Smooth L1 loss can be seen as exactly [`L1Loss`](torch.nn.modules.loss.L1Loss.html#torch.nn.modules.loss.L1Loss), but with the ∣x−y∣<beta|x - y| < beta∣x−y∣<beta
portion replaced with a quadratic function such that its slope is 1 at ∣x−y∣=beta|x - y| = beta∣x−y∣=beta.
The quadratic segment smooths the L1 loss near ∣x−y∣=0|x - y| = 0∣x−y∣=0.

Note

Smooth L1 loss is closely related to [`HuberLoss`](torch.nn.modules.loss.HuberLoss.html#torch.nn.modules.loss.HuberLoss), being
equivalent to huber(x,y)/betahuber(x, y) / betahuber(x,y)/beta (note that Smooth L1's beta hyper-parameter is
also known as delta for Huber). This leads to the following differences:

- As beta -> 0, Smooth L1 loss converges to [`L1Loss`](torch.nn.modules.loss.L1Loss.html#torch.nn.modules.loss.L1Loss), while [`HuberLoss`](torch.nn.modules.loss.HuberLoss.html#torch.nn.modules.loss.HuberLoss)
converges to a constant 0 loss. When beta is 0, Smooth L1 loss is equivalent to L1 loss.
- As beta -> +∞+\infty+∞, Smooth L1 loss converges to a constant 0 loss, while
[`HuberLoss`](torch.nn.modules.loss.HuberLoss.html#torch.nn.modules.loss.HuberLoss) converges to [`MSELoss`](torch.nn.modules.loss.MSELoss.html#torch.nn.modules.loss.MSELoss).
- For Smooth L1 loss, as beta varies, the L1 segment of the loss has a constant slope of 1.
For [`HuberLoss`](torch.nn.modules.loss.HuberLoss.html#torch.nn.modules.loss.HuberLoss), the slope of the L1 segment is beta.

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
- **beta** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - Specifies the threshold at which to change between L1 and L2 loss.
The value must be non-negative. Default: 1.0

Shape:

- Input: (∗)(*)(∗), where ∗*∗ means any number of dimensions.
- Target: (∗)(*)(∗), same shape as the input.
- Output: scalar. If `reduction` is `'none'`, then (∗)(*)(∗), same shape as the input.

Examples

```
>>> loss = nn.SmoothL1Loss()
>>> input = torch.randn(3, 5, requires_grad=True)
>>> target = torch.randn(3, 5)
>>> output = loss(input, target)
>>> output.backward()
```

forward(*input*, *target*)[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/nn/modules/loss.py#L1076)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)