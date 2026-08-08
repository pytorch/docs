# LazyInstanceNorm3d

*class*torch.nn.LazyInstanceNorm3d(*eps=1e-05*, *momentum=0.1*, *affine=True*, *track_running_stats=True*, *device=None*, *dtype=None*, ***, *bias=True*)[[source]](https://github.com/pytorch/pytorch/blob/ab645165510131aa973a5b8880aa56f565e59c7b/torch/nn/modules/instancenorm.py#L455)

A [`torch.nn.InstanceNorm3d`](torch.nn.InstanceNorm3d.html#torch.nn.InstanceNorm3d) module with lazy initialization of the `num_features` argument.

The `num_features` argument of the [`InstanceNorm3d`](torch.nn.InstanceNorm3d.html#torch.nn.InstanceNorm3d) is inferred from the `input.size(1)`.
The attributes that will be lazily initialized are weight, bias,
running_mean and running_var.

Check the [`torch.nn.modules.lazy.LazyModuleMixin`](torch.nn.modules.lazy.LazyModuleMixin.html#torch.nn.modules.lazy.LazyModuleMixin) for further documentation
on lazy modules and their limitations.

Parameters:

- **num_features** - CCC from an expected input of size
(N,C,D,H,W)(N, C, D, H, W)(N,C,D,H,W) or (C,D,H,W)(C, D, H, W)(C,D,H,W)
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

- Input: (N,C,D,H,W)(N, C, D, H, W)(N,C,D,H,W) or (C,D,H,W)(C, D, H, W)(C,D,H,W)
- Output: (N,C,D,H,W)(N, C, D, H, W)(N,C,D,H,W) or (C,D,H,W)(C, D, H, W)(C,D,H,W) (same shape as input)

cls_to_become[[source]](https://github.com/pytorch/pytorch/blob/ab645165510131aa973a5b8880aa56f565e59c7b/torch/nn/modules/instancenorm.py#L375)

alias of [`InstanceNorm3d`](torch.nn.modules.instancenorm.InstanceNorm3d.html#torch.nn.modules.instancenorm.InstanceNorm3d)