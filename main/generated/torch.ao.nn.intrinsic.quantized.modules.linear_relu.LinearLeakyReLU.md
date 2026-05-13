# LinearLeakyReLU

*class*torch.ao.nn.intrinsic.quantized.modules.linear_relu.LinearLeakyReLU(*in_features*, *out_features*, *negative_slope*, *bias=True*, *dtype=torch.qint8*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/ao/nn/intrinsic/quantized/modules/linear_relu.py#L58)

For onednn backend only
A LinearLeakyReLU module fused from Linear and LeakyReLU modules
We adopt the same interface as [`torch.ao.nn.quantized.Linear`](torch.ao.nn.quantized.Linear.html#torch.ao.nn.quantized.Linear).
:ivar Same as torch.ao.nn.quantized.Linear:
:ivar + negative_slope:

Examples::

```
>>> m = nn.intrinsic.LinearLeakyReLU(20, 30, 0.01)
>>> input = torch.randn(128, 20)
>>> output = m(input)
>>> print(output.size())
torch.Size([128, 30])
```