# LSTM

*class*torch.ao.nn.quantized.dynamic.modules.rnn.LSTM(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/b5cf35aa75e0d5087ede9131ab2f970aa2de6509/torch/ao/nn/quantized/dynamic/modules/rnn.py#L512)

A dynamic quantized LSTM module with floating point tensor as inputs and outputs.
We adopt the same interface as torch.nn.LSTM, please see
[https://pytorch.org/docs/stable/nn.html#torch.nn.LSTM](https://pytorch.org/docs/stable/nn.html#torch.nn.LSTM) for documentation.

Examples:

```
>>> rnn = nn.LSTM(10, 20, 2)
>>> input = torch.randn(5, 3, 10)
>>> h0 = torch.randn(2, 3, 20)
>>> c0 = torch.randn(2, 3, 20)
>>> output, (hn, cn) = rnn(input, (h0, c0))
```