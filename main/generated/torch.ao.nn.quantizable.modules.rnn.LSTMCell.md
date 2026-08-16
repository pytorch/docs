# LSTMCell

*class*torch.ao.nn.quantizable.modules.rnn.LSTMCell(*input_dim*, *hidden_dim*, *bias=True*, *device=None*, *dtype=None*, ***, *split_gates=False*)[[source]](https://github.com/pytorch/pytorch/blob/8aac66fb022576e2d13144ab636372f686f23cfa/torch/ao/nn/quantizable/modules/rnn.py#L18)

A quantizable long short-term memory (LSTM) cell.

For the description and the argument types, please, refer to [`LSTMCell`](torch.nn.LSTMCell.html#torch.nn.LSTMCell)

split_gates: specify True to compute the input/forget/cell/output gates separately
to avoid an intermediate tensor which is subsequently chunk'd. This optimization can
be beneficial for on-device inference latency. This flag is cascaded down from the
parent classes.

Examples:

```
>>> import torch.ao.nn.quantizable as nnqa
>>> rnn = nnqa.LSTMCell(10, 20)
>>> input = torch.randn(6, 10)
>>> hx = torch.randn(3, 20)
>>> cx = torch.randn(3, 20)
>>> output = []
>>> for i in range(6):
... hx, cx = rnn(input[i], (hx, cx))
... output.append(hx)
```

*classmethod*from_params(*wi*, *wh*, *bi=None*, *bh=None*, *split_gates=False*)[[source]](https://github.com/pytorch/pytorch/blob/8aac66fb022576e2d13144ab636372f686f23cfa/torch/ao/nn/quantizable/modules/rnn.py#L166)

Uses the weights and biases to create a new LSTM cell.

Parameters:

- **wi** - Weights for the input and hidden layers
- **wh** - Weights for the input and hidden layers
- **bi** - Biases for the input and hidden layers
- **bh** - Biases for the input and hidden layers