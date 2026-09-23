# torch.nn.utils.fusion.fuse_conv_bn_eval

torch.nn.utils.fusion.fuse_conv_bn_eval(*conv*, *bn*, *transpose=False*)[[source]](https://github.com/pytorch/pytorch/blob/8d6343a7cd80821d54ba546bc6f799aad9ccb79c/torch/nn/utils/fusion.py#L20)

Fuse a convolutional module and a BatchNorm module into a single, new convolutional module.

Parameters:

- **conv** (*torch.nn.modules.conv._ConvNd*) - A convolutional module.
- **bn** (*torch.nn.modules.batchnorm._BatchNorm*) - A BatchNorm module.
- **transpose** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*,**optional*) - If True, transpose the convolutional weight. Defaults to False.

Returns:

The fused convolutional module.

Return type:

torch.nn.modules.conv._ConvNd

Note

Both `conv` and `bn` must be in eval mode, and `bn` must have its running buffers computed.