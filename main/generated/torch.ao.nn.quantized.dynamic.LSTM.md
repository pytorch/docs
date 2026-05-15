# LSTM

*class*torch.ao.nn.quantized.dynamic.LSTM(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/ao/nn/quantized/dynamic/modules/rnn.py#L512)

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