# LSTMCell

*class*torch.nn.modules.rnn.LSTMCell(*input_size*, *hidden_size*, *bias=True*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/2f696474dc8fe614670ddb889f4ae1c75d1a11e6/torch/nn/modules/rnn.py#L1661)

A long short-term memory (LSTM) cell.

i=σ(Wiix+bii+Whih+bhi)f=σ(Wifx+bif+Whfh+bhf)g=tanh⁡(Wigx+big+Whgh+bhg)o=σ(Wiox+bio+Whoh+bho)c′=f⊙c+i⊙gh′=o⊙tanh⁡(c′)\begin{array}{ll}
i = \sigma(W_{ii} x + b_{ii} + W_{hi} h + b_{hi}) \\
f = \sigma(W_{if} x + b_{if} + W_{hf} h + b_{hf}) \\
g = \tanh(W_{ig} x + b_{ig} + W_{hg} h + b_{hg}) \\
o = \sigma(W_{io} x + b_{io} + W_{ho} h + b_{ho}) \\
c' = f \odot c + i \odot g \\
h' = o \odot \tanh(c') \\
\end{array}i=σ(Wii​x+bii​+Whi​h+bhi​)f=σ(Wif​x+bif​+Whf​h+bhf​)g=tanh(Wig​x+big​+Whg​h+bhg​)o=σ(Wio​x+bio​+Who​h+bho​)c′=f⊙c+i⊙gh′=o⊙tanh(c′)​

where σ\sigmaσ is the sigmoid function, and ⊙\odot⊙ is the Hadamard product.

Parameters:

- **input_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The number of expected features in the input x
- **hidden_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The number of features in the hidden state h
- **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `False`, then the layer does not use bias weights b_ih and
b_hh. Default: `True`

Inputs: input, (h_0, c_0)

- **input** of shape (batch, input_size) or (input_size): tensor containing input features
- **h_0** of shape (batch, hidden_size) or (hidden_size): tensor containing the initial hidden state
- **c_0** of shape (batch, hidden_size) or (hidden_size): tensor containing the initial cell state

If (h_0, c_0) is not provided, both **h_0** and **c_0** default to zero.

Outputs: (h_1, c_1)

- **h_1** of shape (batch, hidden_size) or (hidden_size): tensor containing the next hidden state
- **c_1** of shape (batch, hidden_size) or (hidden_size): tensor containing the next cell state

Variables:

- **weight_ih** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - the learnable input-hidden weights, of shape
(4*hidden_size, input_size)
- **weight_hh** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - the learnable hidden-hidden weights, of shape
(4*hidden_size, hidden_size)
- **bias_ih** - the learnable input-hidden bias, of shape (4*hidden_size)
- **bias_hh** - the learnable hidden-hidden bias, of shape (4*hidden_size)

Note

All the weights and biases are initialized from U(−k,k)\mathcal{U}(-\sqrt{k}, \sqrt{k})U(−k​,k​)
where k=1hidden_sizek = \frac{1}{\text{hidden\_size}}k=hidden_size1​

On certain ROCm devices, when using float16 inputs this module will use [different precision](../notes/numerical_accuracy.html#fp16-on-mi200) for backward.

Examples:

```
>>> rnn = nn.LSTMCell(10, 20) # (input_size, hidden_size)
>>> input = torch.randn(2, 3, 10) # (time_steps, batch, input_size)
>>> hx = torch.randn(3, 20) # (batch, hidden_size)
>>> cx = torch.randn(3, 20)
>>> output = []
>>> for i in range(input.size()[0]):
... hx, cx = rnn(input[i], (hx, cx))
... output.append(hx)
>>> output = torch.stack(output, dim=0)
```