# LinearReLU

*class*torch.ao.nn.intrinsic.qat.LinearReLU(*in_features*, *out_features*, *bias=True*, *qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/3f8cf8d55cb309421fc5433c518b11b5f9c7a0a0/torch/ao/nn/intrinsic/qat/modules/linear_relu.py#L19)

A LinearReLU module fused from Linear and ReLU modules, attached with
FakeQuantize modules for weight, used in
quantization aware training.

We adopt the same interface as [`torch.nn.Linear`](torch.nn.Linear.html#torch.nn.Linear).

Similar to torch.ao.nn.intrinsic.LinearReLU, with FakeQuantize modules initialized to
default.

Variables:

**weight** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - fake quant module for weight

Examples:

```
>>> m = nn.qat.LinearReLU(20, 30)
>>> input = torch.randn(128, 20)
>>> output = m(input)
>>> print(output.size())
torch.Size([128, 30])
```