# RNNBase

*class*torch.nn.modules.rnn.RNNBase(*mode*, *input_size*, *hidden_size*, *num_layers=1*, *bias=True*, *batch_first=False*, *dropout=0.0*, *bidirectional=False*, *proj_size=0*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/nn/modules/rnn.py#L48)

Base class for RNN modules (RNN, LSTM, GRU).

Implements aspects of RNNs shared by the RNN, LSTM, and GRU classes, such as module initialization
and utility methods for parameter storage management.

Note

The forward method is not implemented by the RNNBase class.

Note

LSTM and GRU classes override some methods implemented by RNNBase.

flatten_parameters()[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/nn/modules/rnn.py#L237)

Reset parameter data pointer so that they can use faster code paths.

Right now, this works only if the module is on the GPU and cuDNN is enabled.
Otherwise, it's a no-op.