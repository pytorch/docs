# torch.nn.utils.fuse_linear_bn_weights

torch.nn.utils.fuse_linear_bn_weights(*linear_w*, *linear_b*, *bn_rm*, *bn_rv*, *bn_eps*, *bn_w*, *bn_b*)[[source]](https://github.com/pytorch/pytorch/blob/fd6d216e3e8bf07c470716dfbf022d82fadd521d/torch/nn/utils/fusion.py#L162)

Fuse linear module parameters and BatchNorm module parameters into new linear module parameters.

Parameters:

- **linear_w** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - Linear weight.
- **linear_b** (*Optional**[*[*torch.Tensor*](../tensors.html#torch.Tensor)*]*) - Linear bias.
- **bn_rm** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - BatchNorm running mean.
- **bn_rv** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - BatchNorm running variance.
- **bn_eps** ([*float*](https://docs.python.org/3/library/functions.html#float)) - BatchNorm epsilon.
- **bn_w** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - BatchNorm weight.
- **bn_b** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - BatchNorm bias.

Returns:

Fused linear weight and bias.

Return type:

Tuple[torch.nn.Parameter, torch.nn.Parameter]