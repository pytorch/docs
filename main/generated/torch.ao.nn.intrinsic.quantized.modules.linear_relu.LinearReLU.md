# LinearReLU

*class*torch.ao.nn.intrinsic.quantized.modules.linear_relu.LinearReLU(*in_features*, *out_features*, *bias=True*, *dtype=torch.qint8*)[[source]](https://github.com/pytorch/pytorch/blob/ab02f71479d3b0fb41d5b722bbe1943340f2022b/torch/ao/nn/intrinsic/quantized/modules/linear_relu.py#L15)

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