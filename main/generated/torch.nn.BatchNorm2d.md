# BatchNorm2d

*class*torch.nn.BatchNorm2d(*num_features*, *eps=1e-05*, *momentum=0.1*, *affine=True*, *track_running_stats=True*, *device=None*, *dtype=None*, ***, *bias=True*)[[source]](https://github.com/pytorch/pytorch/blob/55d182046edce7face6d9eb894f23b3a2588d876/torch/nn/modules/batchnorm.py#L420)

Applies Batch Normalization over a 4D input.

4D is a mini-batch of 2D inputs
with additional channel dimension. Method described in the paper
[Batch Normalization: Accelerating Deep Network Training by Reducing
Internal Covariate Shift](https://arxiv.org/abs/1502.03167) .

y=x−E[x]Var[x]+ϵ∗γ+βy = \frac{x - \mathrm{E}[x]}{ \sqrt{\mathrm{Var}[x] + \epsilon}} * \gamma + \betay=Var[x]+ϵ​x−E[x]​∗γ+β

The mean and standard-deviation are calculated per-dimension over
the mini-batches and γ\gammaγ and β\betaβ are learnable parameter vectors
of size C (where C is the input size). By default, the elements of γ\gammaγ are set
to 1 and the elements of β\betaβ are set to 0. At train time in the forward pass, the
standard-deviation is calculated via the biased estimator, equivalent to
`torch.var(input, correction=0)`. However, the value stored in the moving average of the
standard-deviation is calculated via the unbiased estimator, equivalent to
`torch.var(input, correction=1)`.

Also by default, during training this layer keeps running estimates of its
computed mean and variance, which are then used for normalization during
evaluation. The running estimates are kept with a default `momentum`
of 0.1.

If `track_running_stats` is set to `False`, this layer then does not
keep running estimates, and batch statistics are instead used during
evaluation time as well.

Note

This `momentum` argument is different from one used in optimizer
classes and the conventional notion of momentum. Mathematically, the
update rule for running statistics here is
x^new=(1−momentum)×x^+momentum×xt\hat{x}_\text{new} = (1 - \text{momentum}) \times \hat{x} + \text{momentum} \times x_tx^new​=(1−momentum)×x^+momentum×xt​,
where x^\hat{x}x^ is the estimated statistic and xtx_txt​ is the
new observed value.

Because the Batch Normalization is done over the C dimension, computing statistics
on (N, H, W) slices, it's common terminology to call this Spatial Batch Normalization.

Parameters:

- **num_features** ([*int*](https://docs.python.org/3/library/functions.html#int)) - CCC from an expected input of size
(N,C,H,W)(N, C, H, W)(N,C,H,W)
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)) - a value added to the denominator for numerical stability.
Default: 1e-5
- **momentum** ([*float*](https://docs.python.org/3/library/functions.html#float)*|**None*) - the value used for the running_mean and running_var
computation. Can be set to `None` for cumulative moving average
(i.e. simple average). Default: 0.1
- **affine** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - a boolean value that when set to `True`, this module has
learnable affine parameters. Default: `True`
- **track_running_stats** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - a boolean value that when set to `True`, this
module tracks the running mean and variance, and when set to `False`,
this module does not track such statistics, and initializes statistics
buffers `running_mean` and `running_var` as `None`.
When these buffers are `None`, this module always uses batch statistics.
in both training and eval modes. Default: `True`
- **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If set to `False`, the layer will not learn an additive bias (only relevant if
`affine` is `True`). Default: `True`

Shape:

- Input: (N,C,H,W)(N, C, H, W)(N,C,H,W)
- Output: (N,C,H,W)(N, C, H, W)(N,C,H,W) (same shape as input)

Examples:

```
>>> # With Learnable Parameters
>>> m = nn.BatchNorm2d(100)
>>> # Without Learnable Parameters
>>> m = nn.BatchNorm2d(100, affine=False)
>>> input = torch.randn(20, 100, 35, 45)
>>> output = m(input)
```