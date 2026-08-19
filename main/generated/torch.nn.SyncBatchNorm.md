# SyncBatchNorm

*class*torch.nn.SyncBatchNorm(*num_features*, *eps=1e-05*, *momentum=0.1*, *affine=True*, *track_running_stats=True*, *process_group=None*, *device=None*, *dtype=None*, ***, *bias=True*)[[source]](https://github.com/pytorch/pytorch/blob/3af07571b9d7402fd74352d079e6ff5fa307ec5f/torch/nn/modules/batchnorm.py#L650)

Applies Batch Normalization over a N-Dimensional input.

The N-D input is a mini-batch of [N-2]D inputs with additional channel dimension as described in the paper
[Batch Normalization: Accelerating Deep Network Training by Reducing
Internal Covariate Shift](https://arxiv.org/abs/1502.03167) .

y=x−E[x]Var[x]+ϵ∗γ+βy = \frac{x - \mathrm{E}[x]}{ \sqrt{\mathrm{Var}[x] + \epsilon}} * \gamma + \betay=Var[x]+ϵ​x−E[x]​∗γ+β

The mean and standard-deviation are calculated per-dimension over all
mini-batches of the same process groups. γ\gammaγ and β\betaβ
are learnable parameter vectors of size C (where C is the input size).
By default, the elements of γ\gammaγ are sampled from
U(0,1)\mathcal{U}(0, 1)U(0,1) and the elements of β\betaβ are set to 0.
The standard-deviation is calculated via the biased estimator, equivalent to
torch.var(input, correction=0).

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

Because the Batch Normalization is done for each channel in the `C` dimension, computing
statistics on `(N, +)` slices, it's common terminology to call this Volumetric Batch
Normalization or Spatio-temporal Batch Normalization.

Currently `SyncBatchNorm` only supports
`DistributedDataParallel` (DDP) with single GPU per process. Use
`torch.nn.SyncBatchNorm.convert_sync_batchnorm()` to convert
`BatchNorm*D` layer to `SyncBatchNorm` before wrapping
Network with DDP.

Parameters:

- **num_features** ([*int*](https://docs.python.org/3/library/functions.html#int)) - CCC from an expected input of size
(N,C,+)(N, C, +)(N,C,+)
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)) - a value added to the denominator for numerical stability.
Default: `1e-5`
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
- **process_group** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*|**None*) - synchronization of stats happen within each process group
individually. Default behavior is synchronization across the whole
world
- **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If set to `False`, the layer will not learn an additive bias (only relevant if
`affine` is `True`). Default: `True`

Shape:

- Input: (N,C,+)(N, C, +)(N,C,+)
- Output: (N,C,+)(N, C, +)(N,C,+) (same shape as input)

Note

Synchronization of batchnorm statistics occurs only while training, i.e.
synchronization is disabled when `model.eval()` is set or if
`self.training` is otherwise `False`.

Examples:

```
>>> # With Learnable Parameters
>>> m = nn.SyncBatchNorm(100)
>>> # creating process group (optional)
>>> # ranks is a list of int identifying rank ids.
>>> ranks = list(range(8))
>>> r1, r2 = ranks[:4], ranks[4:]
>>> # Note: every rank calls into new_group for every
>>> # process group created, even if that rank is not
>>> # part of the group.
>>> process_groups = [torch.distributed.new_group(pids) for pids in [r1, r2]]
>>> process_group = process_groups[0 if dist.get_rank() <= 3 else 1]
>>> # Without Learnable Parameters
>>> m = nn.BatchNorm3d(100, affine=False, process_group=process_group)
>>> input = torch.randn(20, 100, 35, 45, 10)
>>> output = m(input)

>>> # network is nn.BatchNorm layer
>>> sync_bn_network = nn.SyncBatchNorm.convert_sync_batchnorm(network, process_group)
>>> # only single gpu per process is currently supported
>>> ddp_sync_bn_network = torch.nn.parallel.DistributedDataParallel(
>>> sync_bn_network,
>>> device_ids=[args.local_rank],
>>> output_device=args.local_rank)
```

*classmethod*convert_sync_batchnorm(*module*, *process_group=None*)[[source]](https://github.com/pytorch/pytorch/blob/3af07571b9d7402fd74352d079e6ff5fa307ec5f/torch/nn/modules/batchnorm.py#L889)

Converts all `BatchNorm*D` layers in the model to `torch.nn.SyncBatchNorm` layers.

Parameters:

- **module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - module containing one or more `BatchNorm*D` layers
- **process_group** (*optional*) - process group to scope synchronization,
default is the whole world

Returns:

The original `module` with the converted `torch.nn.SyncBatchNorm`
layers. If the original `module` is a `BatchNorm*D` layer,
a new `torch.nn.SyncBatchNorm` layer object will be returned
instead.

Example:

```
>>> # Network with nn.BatchNorm layer
>>> module = torch.nn.Sequential(
>>> torch.nn.Linear(20, 100),
>>> torch.nn.BatchNorm1d(100),
>>> ).cuda()
>>> # creating process group (optional)
>>> # ranks is a list of int identifying rank ids.
>>> ranks = list(range(8))
>>> r1, r2 = ranks[:4], ranks[4:]
>>> # Note: every rank calls into new_group for every
>>> # process group created, even if that rank is not
>>> # part of the group.
>>> process_groups = [torch.distributed.new_group(pids) for pids in [r1, r2]]
>>> process_group = process_groups[0 if dist.get_rank() <= 3 else 1]
>>> sync_bn_module = torch.nn.SyncBatchNorm.convert_sync_batchnorm(module, process_group)
```

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/3af07571b9d7402fd74352d079e6ff5fa307ec5f/torch/nn/modules/batchnorm.py#L790)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)