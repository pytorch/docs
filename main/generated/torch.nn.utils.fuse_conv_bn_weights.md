# torch.nn.utils.fuse_conv_bn_weights

torch.nn.utils.fuse_conv_bn_weights(*conv_w*, *conv_b*, *bn_rm*, *bn_rv*, *bn_eps*, *bn_w*, *bn_b*, *transpose=False*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/nn/utils/fusion.py#L58)

Fuse convolutional module parameters and BatchNorm module parameters into new convolutional module parameters.

Parameters:

- **conv_w** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - Convolutional weight.
- **conv_b** (*Optional**[*[*torch.Tensor*](../tensors.html#torch.Tensor)*]*) - Convolutional bias.
- **bn_rm** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - BatchNorm running mean.
- **bn_rv** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - BatchNorm running variance.
- **bn_eps** ([*float*](https://docs.python.org/3/library/functions.html#float)) - BatchNorm epsilon.
- **bn_w** (*Optional**[*[*torch.Tensor*](../tensors.html#torch.Tensor)*]*) - BatchNorm weight.
- **bn_b** (*Optional**[*[*torch.Tensor*](../tensors.html#torch.Tensor)*]*) - BatchNorm bias.
- **transpose** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If True, transpose the conv weight. Defaults to False.

Returns:

Fused convolutional weight and bias.

Return type:

Tuple[torch.nn.Parameter, torch.nn.Parameter]