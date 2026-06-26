# LazyLinear

*class*torch.nn.modules.linear.LazyLinear(*out_features*, *bias=True*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/6468763e46fe7b5527a52dfbb151d63938d7288a/torch/nn/modules/linear.py#L259)

A [`torch.nn.Linear`](torch.nn.Linear.html#torch.nn.Linear) module where in_features is inferred.

In this module, the weight and bias are of `torch.nn.UninitializedParameter`
class. They will be initialized after the first call to `forward` is done and the
module will become a regular [`torch.nn.Linear`](torch.nn.Linear.html#torch.nn.Linear) module. The `in_features` argument
of the [`Linear`](torch.nn.modules.linear.Linear.html#torch.nn.modules.linear.Linear) is inferred from the `input.shape[-1]`.

Check the [`torch.nn.modules.lazy.LazyModuleMixin`](torch.nn.modules.lazy.LazyModuleMixin.html#torch.nn.modules.lazy.LazyModuleMixin) for further documentation
on lazy modules and their limitations.

Parameters:

- **out_features** ([*int*](https://docs.python.org/3/library/functions.html#int)) - size of each output sample
- **bias** ([*UninitializedParameter*](torch.nn.parameter.UninitializedParameter.html#torch.nn.parameter.UninitializedParameter)) - If set to `False`, the layer will not learn an additive bias.
Default: `True`

Variables:

- **weight** ([*torch.nn.parameter.UninitializedParameter*](torch.nn.parameter.UninitializedParameter.html#torch.nn.parameter.UninitializedParameter)) - the learnable weights of the module of shape
(out_features,in_features)(\text{out\_features}, \text{in\_features})(out_features,in_features). The values are
initialized from U(−k,k)\mathcal{U}(-\sqrt{k}, \sqrt{k})U(−k​,k​), where
k=1in_featuresk = \frac{1}{\text{in\_features}}k=in_features1​
- **bias** ([*torch.nn.parameter.UninitializedParameter*](torch.nn.parameter.UninitializedParameter.html#torch.nn.parameter.UninitializedParameter)) - the learnable bias of the module of shape (out_features)(\text{out\_features})(out_features).
If `bias` is `True`, the values are initialized from
U(−k,k)\mathcal{U}(-\sqrt{k}, \sqrt{k})U(−k​,k​) where
k=1in_featuresk = \frac{1}{\text{in\_features}}k=in_features1​

cls_to_become[[source]](https://github.com/pytorch/pytorch/blob/6468763e46fe7b5527a52dfbb151d63938d7288a/torch/nn/modules/linear.py#L53)

alias of [`Linear`](torch.nn.modules.linear.Linear.html#torch.nn.modules.linear.Linear)

initialize_parameters(*input*)[[source]](https://github.com/pytorch/pytorch/blob/6468763e46fe7b5527a52dfbb151d63938d7288a/torch/nn/modules/linear.py#L316)

Infers `in_features` based on `input` and initializes parameters.

reset_parameters()[[source]](https://github.com/pytorch/pytorch/blob/6468763e46fe7b5527a52dfbb151d63938d7288a/torch/nn/modules/linear.py#L308)

Resets parameters based on their initialization used in `__init__`.