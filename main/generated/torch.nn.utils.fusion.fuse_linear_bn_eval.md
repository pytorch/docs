# torch.nn.utils.fusion.fuse_linear_bn_eval

torch.nn.utils.fusion.fuse_linear_bn_eval(*linear*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/5b1433112eb30368cb8f63b3bf0145b391ec72a5/torch/nn/utils/fusion.py#L111)

Fuse a linear module and a BatchNorm module into a single, new linear module.

Parameters:

- **linear** ([*torch.nn.Linear*](torch.nn.Linear.html#torch.nn.Linear)) - A Linear module.
- **bn** (*torch.nn.modules.batchnorm._BatchNorm*) - A BatchNorm module.

Returns:

The fused linear module.

Return type:

[torch.nn.Linear](torch.nn.Linear.html#torch.nn.Linear)

Note

Both `linear` and `bn` must be in eval mode, and `bn` must have its running buffers computed.