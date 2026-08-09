# LazyBatchNorm2d

*class*torch.nn.LazyBatchNorm2d(*eps=1e-05*, *momentum=0.1*, *affine=True*, *track_running_stats=True*, *device=None*, *dtype=None*, ***, *bias=True*)[[source]](https://github.com/pytorch/pytorch/blob/a471a58d241b08025dcb4ec69c2d30e5a49a757a/torch/nn/modules/batchnorm.py#L499)

A [`torch.nn.BatchNorm2d`](torch.nn.BatchNorm2d.html#torch.nn.BatchNorm2d) module with lazy initialization.

Lazy initialization is done for the `num_features` argument of the [`BatchNorm2d`](torch.nn.BatchNorm2d.html#torch.nn.BatchNorm2d) that is inferred
from the `input.size(1)`.
The attributes that will be lazily initialized are weight, bias,
running_mean and running_var.

Check the [`torch.nn.modules.lazy.LazyModuleMixin`](torch.nn.modules.lazy.LazyModuleMixin.html#torch.nn.modules.lazy.LazyModuleMixin) for further documentation
on lazy modules and their limitations.

Parameters:

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
- **bias** ([*UninitializedParameter*](torch.nn.parameter.UninitializedParameter.html#torch.nn.parameter.UninitializedParameter)) - If set to `False`, the layer will not learn an additive bias (only relevant if
`affine` is `True`). Default: `True`

cls_to_become[[source]](https://github.com/pytorch/pytorch/blob/a471a58d241b08025dcb4ec69c2d30e5a49a757a/torch/nn/modules/batchnorm.py#L420)

alias of [`BatchNorm2d`](torch.nn.modules.batchnorm.BatchNorm2d.html#torch.nn.modules.batchnorm.BatchNorm2d)