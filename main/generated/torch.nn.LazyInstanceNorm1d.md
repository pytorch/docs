# LazyInstanceNorm1d

*class*torch.nn.LazyInstanceNorm1d(*eps=1e-05*, *momentum=0.1*, *affine=True*, *track_running_stats=True*, *device=None*, *dtype=None*, ***, *bias=True*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/nn/modules/instancenorm.py#L215)

A [`torch.nn.InstanceNorm1d`](torch.nn.InstanceNorm1d.html#torch.nn.InstanceNorm1d) module with lazy initialization of the `num_features` argument.

The `num_features` argument of the [`InstanceNorm1d`](torch.nn.InstanceNorm1d.html#torch.nn.InstanceNorm1d) is inferred from the `input.size(1)`.
The attributes that will be lazily initialized are weight, bias, running_mean and running_var.

Check the [`torch.nn.modules.lazy.LazyModuleMixin`](torch.nn.modules.lazy.LazyModuleMixin.html#torch.nn.modules.lazy.LazyModuleMixin) for further documentation
on lazy modules and their limitations.

Parameters:

- **num_features** - CCC from an expected input of size
(N,C,L)(N, C, L)(N,C,L) or (C,L)(C, L)(C,L)
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)) - a value added to the denominator for numerical stability. Default: 1e-5
- **momentum** ([*float*](https://docs.python.org/3/library/functions.html#float)*|**None*) - the value used for the running_mean and running_var computation. Default: 0.1
- **affine** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - a boolean value that when set to `True`, this module has
learnable affine parameters, initialized the same way as done for batch normalization.
Default: `False`
- **track_running_stats** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - a boolean value that when set to `True`, this
module tracks the running mean and variance, and when set to `False`,
this module does not track such statistics and always uses batch
statistics in both training and eval modes. Default: `False`
- **bias** ([*UninitializedParameter*](torch.nn.parameter.UninitializedParameter.html#torch.nn.parameter.UninitializedParameter)) - If set to `False`, the layer will not learn an additive bias (only relevant if
`affine` is `True`). Default: `True`

Shape:

- Input: (N,C,L)(N, C, L)(N,C,L) or (C,L)(C, L)(C,L)
- Output: (N,C,L)(N, C, L)(N,C,L) or (C,L)(C, L)(C,L) (same shape as input)

cls_to_become[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/nn/modules/instancenorm.py#L136)

alias of [`InstanceNorm1d`](torch.nn.modules.instancenorm.InstanceNorm1d.html#torch.nn.modules.instancenorm.InstanceNorm1d)