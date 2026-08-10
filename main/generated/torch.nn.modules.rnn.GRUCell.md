# GRUCell

*class*torch.nn.modules.rnn.GRUCell(*input_size*, *hidden_size*, *bias=True*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/2ba6a0a1865e48bce91c6a36d4d11218b52baee7/torch/nn/modules/rnn.py#L1771)

A gated recurrent unit (GRU) cell.

r=σ(Wirx+bir+Whrh+bhr)z=σ(Wizx+biz+Whzh+bhz)n=tanh⁡(Winx+bin+r⊙(Whnh+bhn))h′=(1−z)⊙n+z⊙h\begin{array}{ll}
r = \sigma(W_{ir} x + b_{ir} + W_{hr} h + b_{hr}) \\
z = \sigma(W_{iz} x + b_{iz} + W_{hz} h + b_{hz}) \\
n = \tanh(W_{in} x + b_{in} + r \odot (W_{hn} h + b_{hn})) \\
h' = (1 - z) \odot n + z \odot h
\end{array}r=σ(Wir​x+bir​+Whr​h+bhr​)z=σ(Wiz​x+biz​+Whz​h+bhz​)n=tanh(Win​x+bin​+r⊙(Whn​h+bhn​))h′=(1−z)⊙n+z⊙h​

where σ\sigmaσ is the sigmoid function, and ⊙\odot⊙ is the Hadamard product.

Parameters:

- **input_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The number of expected features in the input x
- **hidden_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The number of features in the hidden state h
- **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `False`, then the layer does not use bias weights b_ih and
b_hh. Default: `True`

Inputs: input, hidden

- **input** : tensor containing input features
- **hidden** : tensor containing the initial hidden
state for each element in the batch.
Defaults to zero if not provided.

Outputs: h'

- **h'** : tensor containing the next hidden state
for each element in the batch

Shape:

- input: (N,Hin)(N, H_{in})(N,Hin​) or (Hin)(H_{in})(Hin​) tensor containing input features where
HinH_{in}Hin​ = input_size.
- hidden: (N,Hout)(N, H_{out})(N,Hout​) or (Hout)(H_{out})(Hout​) tensor containing the initial hidden
state where HoutH_{out}Hout​ = hidden_size. Defaults to zero if not provided.
- output: (N,Hout)(N, H_{out})(N,Hout​) or (Hout)(H_{out})(Hout​) tensor containing the next hidden state.

Variables:

- **weight_ih** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - the learnable input-hidden weights, of shape
(3*hidden_size, input_size)
- **weight_hh** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - the learnable hidden-hidden weights, of shape
(3*hidden_size, hidden_size)
- **bias_ih** - the learnable input-hidden bias, of shape (3*hidden_size)
- **bias_hh** - the learnable hidden-hidden bias, of shape (3*hidden_size)

Note

All the weights and biases are initialized from U(−k,k)\mathcal{U}(-\sqrt{k}, \sqrt{k})U(−k​,k​)
where k=1hidden_sizek = \frac{1}{\text{hidden\_size}}k=hidden_size1​

On certain ROCm devices, when using float16 inputs this module will use [different precision](../notes/numerical_accuracy.html#fp16-on-mi200) for backward.

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