# LinearReLU

*class*torch.ao.nn.intrinsic.quantized.dynamic.LinearReLU(*in_features*, *out_features*, *bias=True*, *dtype=torch.qint8*)[[source]](https://github.com/pytorch/pytorch/blob/dea5f568512cef2ab009ee7858b1cfd9be8ba924/torch/ao/nn/intrinsic/quantized/dynamic/modules/linear_relu.py#L12)

A LinearReLU module fused from Linear and ReLU modules that can be used
for dynamic quantization.
Supports both, FP16 and INT8 quantization.

We adopt the same interface as [`torch.ao.nn.quantized.dynamic.Linear`](torch.ao.nn.quantized.dynamic.Linear.html#torch.ao.nn.quantized.dynamic.Linear).

Variables:

**torch.ao.nn.quantized.dynamic.Linear** (*Same as*) -

Examples:

```
>>> m = nn.intrinsic.quantized.dynamic.LinearReLU(20, 30)
>>> input = torch.randn(128, 20)
>>> output = m(input)
>>> print(output.size())
torch.Size([128, 30])
```