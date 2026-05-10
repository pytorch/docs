# InstanceNorm1d

*class*torch.nn.InstanceNorm1d(*num_features*, *eps=1e-05*, *momentum=0.1*, *affine=False*, *track_running_stats=False*, *device=None*, *dtype=None*, ***, *bias=True*)[[source]](https://github.com/pytorch/pytorch/blob/063b516448b60c5818cfe255e27825810710849a/torch/nn/modules/instancenorm.py#L136)

Applies Instance Normalization.

This operation applies Instance Normalization
over a 2D (unbatched) or 3D (batched) input as described in the paper
[Instance Normalization: The Missing Ingredient for Fast Stylization](https://arxiv.org/abs/1607.08022).

y=x−E[x]Var[x]+ϵ∗γ+βy = \frac{x - \mathrm{E}[x]}{ \sqrt{\mathrm{Var}[x] + \epsilon}} * \gamma + \betay=Var[x]+ϵ​x−E[x]​∗γ+β

The mean and standard-deviation are calculated per-dimension separately
for each object in a mini-batch. γ\gammaγ and β\betaβ are learnable parameter vectors
of size C (where C is the number of features or channels of the input) if `affine` is `True`.
The variance is calculated via the biased estimator, equivalent to
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

`InstanceNorm1d` and [`LayerNorm`](torch.nn.LayerNorm.html#torch.nn.LayerNorm) are very similar, but
have some subtle differences. `InstanceNorm1d` is applied
on each channel of channeled data like multidimensional time series, but
[`LayerNorm`](torch.nn.LayerNorm.html#torch.nn.LayerNorm) is usually applied on entire sample and often in NLP
tasks. Additionally, [`LayerNorm`](torch.nn.LayerNorm.html#torch.nn.LayerNorm) applies elementwise affine
transform, while `InstanceNorm1d` usually don't apply affine
transform.

Parameters:

- **num_features** ([*int*](https://docs.python.org/3/library/functions.html#int)) - number of features or channels CCC of the input
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

- Input: (N,C,L)(N, C, L)(N,C,L) or (C,L)(C, L)(C,L)
- Output: (N,C,L)(N, C, L)(N,C,L) or (C,L)(C, L)(C,L) (same shape as input)

Examples:

```
>>> # Without Learnable Parameters
>>> m = nn.InstanceNorm1d(100)
>>> # With Learnable Parameters
>>> m = nn.InstanceNorm1d(100, affine=True)
>>> input = torch.randn(20, 100, 40)
>>> output = m(input)
```