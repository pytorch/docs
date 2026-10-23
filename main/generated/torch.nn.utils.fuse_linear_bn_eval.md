# torch.nn.utils.fuse_linear_bn_eval

torch.nn.utils.fuse_linear_bn_eval(*linear*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/8fdc6530233b7482bb73269b47190767c3cfb0b3/torch/nn/utils/fusion.py#L111)

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