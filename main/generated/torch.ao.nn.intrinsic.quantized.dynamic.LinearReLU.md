# LinearReLU

*class*torch.ao.nn.intrinsic.quantized.dynamic.LinearReLU(*in_features*, *out_features*, *bias=True*, *dtype=torch.qint8*)[[source]](https://github.com/pytorch/pytorch/blob/f744a6b99cda942b3dd232f56c0ebf413660c13f/torch/ao/nn/intrinsic/quantized/dynamic/modules/linear_relu.py#L12)

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