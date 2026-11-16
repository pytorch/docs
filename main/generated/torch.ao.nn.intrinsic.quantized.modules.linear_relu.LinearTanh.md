# LinearTanh

*class*torch.ao.nn.intrinsic.quantized.modules.linear_relu.LinearTanh(*in_features*, *out_features*, *bias=True*, *dtype=torch.qint8*)[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/ao/nn/intrinsic/quantized/modules/linear_relu.py#L135)

A LinearTanh module fused from Linear and Tanh modules

We adopt the same interface as [`torch.ao.nn.quantized.Linear`](torch.ao.nn.quantized.Linear.html#torch.ao.nn.quantized.Linear).

Variables:

**torch.ao.nn.quantized.Linear** (*Same as*) -

Examples:

```
>>> m = nn.intrinsic.LinearTanh(20, 30)
>>> input = torch.randn(128, 20)
>>> output = m(input)
>>> print(output.size())
torch.Size([128, 30])
```