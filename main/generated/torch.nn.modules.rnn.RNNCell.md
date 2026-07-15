# RNNCell

*class*torch.nn.modules.rnn.RNNCell(*input_size*, *hidden_size*, *bias=True*, *nonlinearity='tanh'*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/0f5932e5e82c3a4da21331c6cf7cddf6bce55cff/torch/nn/modules/rnn.py#L1542)

An Elman RNN cell with tanh or ReLU non-linearity.

h′=tanh⁡(Wihx+bih+Whhh+bhh)h' = \tanh(W_{ih} x + b_{ih} + W_{hh} h + b_{hh})h′=tanh(Wih​x+bih​+Whh​h+bhh​)

If `nonlinearity` is 'relu', then ReLU is used in place of tanh.

Parameters:

- **input_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The number of expected features in the input x
- **hidden_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The number of features in the hidden state h
- **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `False`, then the layer does not use bias weights b_ih and b_hh.
Default: `True`
- **nonlinearity** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The non-linearity to use. Can be either `'tanh'` or `'relu'`. Default: `'tanh'`

Inputs: input, hidden

- **input**: tensor containing input features
- **hidden**: tensor containing the initial hidden state
Defaults to zero if not provided.

Outputs: h'

- **h'** of shape (batch, hidden_size): tensor containing the next hidden state
for each element in the batch

Shape:

- input: (N,Hin)(N, H_{in})(N,Hin​) or (Hin)(H_{in})(Hin​) tensor containing input features where
HinH_{in}Hin​ = input_size.
- hidden: (N,Hout)(N, H_{out})(N,Hout​) or (Hout)(H_{out})(Hout​) tensor containing the initial hidden
state where HoutH_{out}Hout​ = hidden_size. Defaults to zero if not provided.
- output: (N,Hout)(N, H_{out})(N,Hout​) or (Hout)(H_{out})(Hout​) tensor containing the next hidden state.

Variables:

- **weight_ih** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - the learnable input-hidden weights, of shape
(hidden_size, input_size)
- **weight_hh** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - the learnable hidden-hidden weights, of shape
(hidden_size, hidden_size)
- **bias_ih** - the learnable input-hidden bias, of shape (hidden_size)
- **bias_hh** - the learnable hidden-hidden bias, of shape (hidden_size)

Note

All the weights and biases are initialized from U(−k,k)\mathcal{U}(-\sqrt{k}, \sqrt{k})U(−k​,k​)
where k=1hidden_sizek = \frac{1}{\text{hidden\_size}}k=hidden_size1​

Examples:

```
>>> rnn = nn.RNNCell(10, 20)
>>> input = torch.randn(6, 3, 10)
>>> hx = torch.randn(3, 20)
>>> output = []
>>> for i in range(6):
... hx = rnn(input[i], hx)
... output.append(hx)
```