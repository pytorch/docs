# torch.nn.functional.dropout1d

torch.nn.functional.dropout1d(*input*, *p=0.5*, *training=True*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/69bbaeafe0b3f1e423be17b25ca11b149845b521/torch/nn/functional.py#L1476)

Randomly zero out entire channels (a channel is a 1D feature map).

For example, the jjj-th channel of the iii-th sample in the
batched input is a 1D tensor input[i,j]\text{input}[i, j]input[i,j] of the input tensor.
Each channel will be zeroed out independently on every forward call with
probability `p` using samples from a Bernoulli distribution.

See [`Dropout1d`](torch.nn.Dropout1d.html#torch.nn.Dropout1d) for details.

Parameters:

- **p** ([*float*](https://docs.python.org/3/library/functions.html#float)) - probability of a channel to be zeroed. Default: 0.5
- **training** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - apply dropout if is `True`. Default: `True`
- **inplace** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If set to `True`, will do this operation in-place. Default: `False`

Return type:

[*Tensor*](../tensors.html#torch.Tensor)