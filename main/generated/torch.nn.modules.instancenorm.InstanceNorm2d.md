# InstanceNorm2d

*class*torch.nn.modules.instancenorm.InstanceNorm2d(*num_features*, *eps=1e-05*, *momentum=0.1*, *affine=False*, *track_running_stats=False*, *device=None*, *dtype=None*, ***, *bias=True*)[[source]](https://github.com/pytorch/pytorch/blob/df83f06a8c49a667b9408934fa9eaae1aaf32d04/torch/nn/modules/instancenorm.py#L254)

Applies Instance Normalization.

This operation applies Instance Normalization
over a 4D input (a mini-batch of 2D inputs
with additional channel dimension) as described in the paper
[Instance Normalization: The Missing Ingredient for Fast Stylization](https://arxiv.org/abs/1607.08022).

y=x−E[x]Var[x]+ϵ∗γ+βy = \frac{x - \mathrm{E}[x]}{ \sqrt{\mathrm{Var}[x] + \epsilon}} * \gamma + \betay=Var[x]+ϵ​x−E[x]​∗γ+β

The mean and standard-deviation are calculated per-dimension separately
for each object in a mini-batch. γ\gammaγ and β\betaβ are learnable parameter vectors
of size C (where C is the input size) if `affine` is `True`.
The standard-deviation is calculated via the biased estimator, equivalent to
torch.var(input, correction=0).

By default, this layer uses instance statistics computed from input data in
both training and evaluation modes.

If `track_running_stats` is set to `True`, during training this
layer keeps running estimates of its computed mean and variance, which are
then used for normalization during evaluation. The running estimates are
kept with a default `momentum` of 0.1.

Note

This `momentum` argument is different from one used in optimizer
classes and the conventional notion of momentum. Mathematically, the
update rule for running statistics here is
x^new=(1−momentum)×x^+momentum×xt\hat{x}_\text{new} = (1 - \text{momentum}) \times \hat{x} + \text{momentum} \times x_tx^new​=(1−momentum)×x^+momentum×xt​,
where x^\hat{x}x^ is the estimated statistic and xtx_txt​ is the
new observed value.

Note

`InstanceNorm2d` and `LayerNorm` are very similar, but
have some subtle differences. `InstanceNorm2d` is applied
on each channel of channeled data like RGB images, but
`LayerNorm` is usually applied on entire sample and often in NLP
tasks. Additionally, `LayerNorm` applies elementwise affine
transform, while `InstanceNorm2d` usually don't apply affine
transform.

Parameters:

- **num_features** ([*int*](https://docs.python.org/3/library/functions.html#int)) - CCC from an expected input of size
(N,C,H,W)(N, C, H, W)(N,C,H,W) or (C,H,W)(C, H, W)(C,H,W)
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)) - a value added to the denominator for numerical stability. Default: 1e-5
- **momentum** ([*float*](https://docs.python.org/3/library/functions.html#float)*|**None*) - the value used for the running_mean and running_var computation. Default: 0.1
- **affine** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - a boolean value that when set to `True`, this module has
learnable affine parameters, initialized the same way as done for batch normalization.
Default: `False`
- **track_running_stats** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - a boolean value that when set to `True`, this
module tracks the running mean and variance, and when set to `False`,
this module does not track such statistics and always uses batch
statistics in both training and eval modes. Default: `False`
- **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If set to `False`, the layer will not learn an additive bias (only relevant if
`affine` is `True`). Default: `True`

Shape:

- Input: (N,C,H,W)(N, C, H, W)(N,C,H,W) or (C,H,W)(C, H, W)(C,H,W)
- Output: (N,C,H,W)(N, C, H, W)(N,C,H,W) or (C,H,W)(C, H, W)(C,H,W) (same shape as input)

Examples:

```
>>> # Without Learnable Parameters
>>> m = nn.InstanceNorm2d(100)
>>> # With Learnable Parameters
>>> m = nn.InstanceNorm2d(100, affine=True)
>>> input = torch.randn(20, 100, 35, 45)
>>> output = m(input)
```