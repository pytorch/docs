# LSTM

*class*torch.ao.nn.quantizable.LSTM(*input_size*, *hidden_size*, *num_layers=1*, *bias=True*, *batch_first=False*, *dropout=0.0*, *bidirectional=False*, *device=None*, *dtype=None*, ***, *split_gates=False*)[[source]](https://github.com/pytorch/pytorch/blob/3af07571b9d7402fd74352d079e6ff5fa307ec5f/torch/ao/nn/quantizable/modules/rnn.py#L411)

A quantizable long short-term memory (LSTM).

For the description and the argument types, please, refer to [`LSTM`](torch.nn.LSTM.html#torch.nn.LSTM)

Variables:

**layers** - instances of the _LSTMLayer

Note

To access the weights and biases, you need to access them per layer.
See examples below.

Examples:

```
>>> import torch.ao.nn.quantizable as nnqa
>>> rnn = nnqa.LSTM(10, 20, 2)
>>> input = torch.randn(5, 3, 10)
>>> h0 = torch.randn(2, 3, 20)
>>> c0 = torch.randn(2, 3, 20)
>>> output, (hn, cn) = rnn(input, (h0, c0))
>>> # To get the weights:
>>> print(rnn.layers[0].weight_ih)
tensor([[...]])
>>> print(rnn.layers[0].weight_hh)
AssertionError: There is no reverse path in the non-bidirectional layer
```