# LSTMCell

*class*torch.ao.nn.quantized.dynamic.LSTMCell(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/2a8ba15825312e681c7dc6b12b79dec216aecd30/torch/ao/nn/quantized/dynamic/modules/rnn.py#L1277)

A long short-term memory (LSTM) cell.

A dynamic quantized LSTMCell module with floating point tensor as inputs and outputs.
Weights are quantized to 8 bits. We adopt the same interface as torch.nn.LSTMCell,
please see [https://pytorch.org/docs/stable/nn.html#torch.nn.LSTMCell](https://pytorch.org/docs/stable/nn.html#torch.nn.LSTMCell) for documentation.

Examples:

```
>>> rnn = nn.LSTMCell(10, 20)
>>> input = torch.randn(6, 3, 10)
>>> hx = torch.randn(3, 20)
>>> cx = torch.randn(3, 20)
>>> output = []
>>> for i in range(6):
... hx, cx = rnn(input[i], (hx, cx))
... output.append(hx)
```