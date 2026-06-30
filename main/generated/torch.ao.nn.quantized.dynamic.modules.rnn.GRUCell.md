# GRUCell

*class*torch.ao.nn.quantized.dynamic.modules.rnn.GRUCell(*input_size*, *hidden_size*, *bias=True*, *dtype=torch.qint8*)[[source]](https://github.com/pytorch/pytorch/blob/c8f2d26abd0de59995af555e80c82ca1221bc21b/torch/ao/nn/quantized/dynamic/modules/rnn.py#L1330)

A gated recurrent unit (GRU) cell

A dynamic quantized GRUCell module with floating point tensor as inputs and outputs.
Weights are quantized to 8 bits. We adopt the same interface as torch.nn.GRUCell,
please see [https://pytorch.org/docs/stable/nn.html#torch.nn.GRUCell](https://pytorch.org/docs/stable/nn.html#torch.nn.GRUCell) for documentation.

Examples:

```
>>> rnn = nn.GRUCell(10, 20)
>>> input = torch.randn(6, 3, 10)
>>> hx = torch.randn(3, 20)
>>> output = []
>>> for i in range(6):
... hx = rnn(input[i], hx)
... output.append(hx)
```