# torch.nn.functional.gumbel_softmax

torch.nn.functional.gumbel_softmax(*logits*, *tau=1*, *hard=False*, *eps=1e-10*, *dim=-1*)[[source]](https://github.com/pytorch/pytorch/blob/d7a82dcfcb838549a84f49516bc5c32ecf1eef90/torch/nn/functional.py#L2219)

Sample from the Gumbel-Softmax distribution ([Link 1](https://arxiv.org/abs/1611.00712) [Link 2](https://arxiv.org/abs/1611.01144)) and optionally discretize.

Parameters:

- **logits** ([*Tensor*](../tensors.html#torch.Tensor)) - [..., num_features] unnormalized log probabilities
- **tau** ([*float*](https://docs.python.org/3/library/functions.html#float)) - non-negative scalar temperature
- **hard** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - if `True`, the returned samples will be discretized as one-hot vectors,
but will be differentiated as if it is the soft sample in autograd
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - A dimension along which softmax will be computed. Default: -1.

Returns:

Sampled tensor of same shape as logits from the Gumbel-Softmax distribution.
If `hard=True`, the returned samples will be one-hot, otherwise they will
be probability distributions that sum to 1 across dim.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Note

This function is here for legacy reasons, may be removed from nn.Functional in the future.

Note

The main trick for hard is to do y_hard - y_soft.detach() + y_soft

It achieves two things:
- makes the output value exactly one-hot
(since we add then subtract y_soft value)
- makes the gradient equal to y_soft gradient
(since we strip all other gradients)

Examples::

```
>>> logits = torch.randn(20, 32)
>>> # Sample soft categorical using reparametrization trick:
>>> F.gumbel_softmax(logits, tau=1, hard=False)
>>> # Sample hard categorical using "Straight-through" trick:
>>> F.gumbel_softmax(logits, tau=1, hard=True)
```