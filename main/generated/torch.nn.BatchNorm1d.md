# BatchNorm1d

*class*torch.nn.BatchNorm1d(*num_features*, *eps=1e-05*, *momentum=0.1*, *affine=True*, *track_running_stats=True*, *device=None*, *dtype=None*, ***, *bias=True*)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/nn/modules/batchnorm.py#L306)

Applies Batch Normalization over a 2D or 3D input.

Method described in the paper
[Batch Normalization: Accelerating Deep Network Training by Reducing
Internal Covariate Shift](https://arxiv.org/abs/1502.03167) .

y=x−E[x]Var[x]+ϵ∗γ+βy = \frac{x - \mathrm{E}[x]}{\sqrt{\mathrm{Var}[x] + \epsilon}} * \gamma + \betay=Var[x]+ϵ​x−E[x]​∗γ+β

The mean and standard-deviation are calculated per-dimension over
the mini-batches and γ\gammaγ and β\betaβ are learnable parameter vectors
of size C (where C is the number of features or channels of the input). By default, the
elements of γ\gammaγ are set to 1 and the elements of β\betaβ are set to 0.
At train time in the forward pass, the variance is calculated via the biased estimator,
equivalent to `torch.var(input, correction=0)`. However, the value stored in the
moving average of the variance is calculated via the unbiased estimator, equivalent to
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
on (N, L) slices, it's common terminology to call this Temporal Batch Normalization.

Parameters:

- **num_features** ([*int*](https://docs.python.org/3/library/functions.html#int)) - number of features or channels CCC of the input
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

- Input: (N,C)(N, C)(N,C) or (N,C,L)(N, C, L)(N,C,L), where NNN is the batch size,
CCC is the number of features or channels, and LLL is the sequence length
- Output: (N,C)(N, C)(N,C) or (N,C,L)(N, C, L)(N,C,L) (same shape as input)

Examples:

```
>>> # With Learnable Parameters
>>> m = nn.BatchNorm1d(100)
>>> # Without Learnable Parameters
>>> m = nn.BatchNorm1d(100, affine=False)
>>> input = torch.randn(20, 100)
>>> output = m(input)
```