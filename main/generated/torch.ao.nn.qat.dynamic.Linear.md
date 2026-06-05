# Linear

*class*torch.ao.nn.qat.dynamic.Linear(*in_features*, *out_features*, *bias=True*, *qconfig=None*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/784e50bb03d4ff5f8fdc368da8449558a8fb4a43/torch/ao/nn/qat/dynamic/modules/linear.py#L13)

A linear module attached with FakeQuantize modules for weight,
used for dynamic quantization aware training.

We adopt the same interface as torch.nn.Linear, please see
[https://pytorch.org/docs/stable/nn.html#torch.nn.Linear](https://pytorch.org/docs/stable/nn.html#torch.nn.Linear)
for documentation.

Similar to torch.nn.Linear, with FakeQuantize modules initialized to
default.