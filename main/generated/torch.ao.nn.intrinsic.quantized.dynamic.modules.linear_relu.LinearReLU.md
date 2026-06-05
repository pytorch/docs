# LinearReLU

*class*torch.ao.nn.intrinsic.quantized.dynamic.modules.linear_relu.LinearReLU(*in_features*, *out_features*, *bias=True*, *dtype=torch.qint8*)[[source]](https://github.com/pytorch/pytorch/blob/784e50bb03d4ff5f8fdc368da8449558a8fb4a43/torch/ao/nn/intrinsic/quantized/dynamic/modules/linear_relu.py#L12)

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