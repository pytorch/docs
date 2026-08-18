# GRUCell

*class*torch.ao.nn.quantized.dynamic.GRUCell(*input_size*, *hidden_size*, *bias=True*, *dtype=torch.qint8*)[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/ao/nn/quantized/dynamic/modules/rnn.py#L1330)

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