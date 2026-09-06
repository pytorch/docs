# HuberLoss

*class*torch.nn.HuberLoss(*reduction='mean'*, *delta=1.0*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/nn/modules/loss.py#L1081)

Creates a criterion that uses a squared term if the absolute
element-wise error falls below delta and a delta-scaled L1 term otherwise.
This loss combines advantages of both [`L1Loss`](torch.nn.L1Loss.html#torch.nn.L1Loss) and [`MSELoss`](torch.nn.MSELoss.html#torch.nn.MSELoss); the
delta-scaled L1 region makes the loss less sensitive to outliers than [`MSELoss`](torch.nn.MSELoss.html#torch.nn.MSELoss),
while the L2 region provides smoothness over [`L1Loss`](torch.nn.L1Loss.html#torch.nn.L1Loss) near 0. See
[Huber loss](https://en.wikipedia.org/wiki/Huber_loss) for more information.

For a batch of size NNN, the unreduced loss can be described as:

ℓ(x,y)=L={l1,...,lN}T\ell(x, y) = L = \{l_1, ..., l_N\}^T

ℓ(x,y)=L={l1​,...,lN​}T

with

ln={0.5(xn−yn)2,if ∣xn−yn∣<deltadelta∗(∣xn−yn∣−0.5∗delta),otherwise l_n = \begin{cases}
0.5 (x_n - y_n)^2, & \text{if } |x_n - y_n| < delta \\
delta * (|x_n - y_n| - 0.5 * delta), & \text{otherwise }
\end{cases}

ln​={0.5(xn​−yn​)2,delta∗(∣xn​−yn​∣−0.5∗delta),​if ∣xn​−yn​∣<deltaotherwise ​

If reduction is not none, then:

ℓ(x,y)={mean⁡(L),if reduction='mean';sum⁡(L),if reduction='sum'.\ell(x, y) =
\begin{cases}
 \operatorname{mean}(L), & \text{if reduction} = \text{`mean';}\\
 \operatorname{sum}(L), & \text{if reduction} = \text{`sum'.}
\end{cases}

ℓ(x,y)={mean(L),sum(L),​if reduction='mean';if reduction='sum'.​

Note

When delta is set to 1, this loss is equivalent to [`SmoothL1Loss`](torch.nn.SmoothL1Loss.html#torch.nn.SmoothL1Loss).
In general, this loss differs from [`SmoothL1Loss`](torch.nn.SmoothL1Loss.html#torch.nn.SmoothL1Loss) by a factor of delta (AKA beta
in Smooth L1).
See [`SmoothL1Loss`](torch.nn.SmoothL1Loss.html#torch.nn.SmoothL1Loss) for additional discussion on the differences in behavior
between the two losses.

Parameters:

- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. `'none'`: no reduction will be applied,
`'mean'`: the sum of the output will be divided by the number of
elements in the output, `'sum'`: the output will be summed. Default: `'mean'`
- **delta** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - Specifies the threshold at which to change between delta-scaled L1 and L2 loss.
The value must be positive. Default: 1.0

Shape:

- Input: (∗)(*)(∗) where ∗*∗ means any number of dimensions.
- Target: (∗)(*)(∗), same shape as the input.
- Output: scalar. If `reduction` is `'none'`, then (∗)(*)(∗), same shape as the input.

Examples

```
>>> loss = nn.HuberLoss()
>>> input = torch.randn(3, 5, requires_grad=True)
>>> target = torch.randn(3, 5)
>>> output = loss(input, target)
>>> output.backward()
```

forward(*input*, *target*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/nn/modules/loss.py#L1148)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)