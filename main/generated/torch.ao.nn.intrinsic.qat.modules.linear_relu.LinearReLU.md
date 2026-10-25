# LinearReLU

*class*torch.ao.nn.intrinsic.qat.modules.linear_relu.LinearReLU(*in_features*, *out_features*, *bias=True*, *qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/c9b5004c45376c912422325d032b2d74b4828d5c/torch/ao/nn/intrinsic/qat/modules/linear_relu.py#L19)

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