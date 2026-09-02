# Linear

*class*torch.ao.nn.qat.dynamic.Linear(*in_features*, *out_features*, *bias=True*, *qconfig=None*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/ao/nn/qat/dynamic/modules/linear.py#L13)

A linear module attached with FakeQuantize modules for weight,
used for dynamic quantization aware training.

We adopt the same interface as torch.nn.Linear, please see
[https://pytorch.org/docs/stable/nn.html#torch.nn.Linear](https://pytorch.org/docs/stable/nn.html#torch.nn.Linear)
for documentation.

Similar to torch.nn.Linear, with FakeQuantize modules initialized to
default.