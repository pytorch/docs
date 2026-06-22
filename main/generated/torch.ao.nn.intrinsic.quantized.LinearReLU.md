# LinearReLU

*class*torch.ao.nn.intrinsic.quantized.LinearReLU(*in_features*, *out_features*, *bias=True*, *dtype=torch.qint8*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/ao/nn/intrinsic/quantized/modules/linear_relu.py#L15)

A LinearReLU module fused from Linear and ReLU modules

We adopt the same interface as [`torch.ao.nn.quantized.Linear`](torch.ao.nn.quantized.Linear.html#torch.ao.nn.quantized.Linear).

Variables:

**torch.ao.nn.quantized.Linear** (*Same as*) -

Examples:

```
>>> m = nn.intrinsic.LinearReLU(20, 30)
>>> input = torch.randn(128, 20)
>>> output = m(input)
>>> print(output.size())
torch.Size([128, 30])
```