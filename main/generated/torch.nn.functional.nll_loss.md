# torch.nn.functional.nll_loss

torch.nn.functional.nll_loss(*input*, *target*, *weight=None*, *size_average=None*, *ignore_index=-100*, *reduce=None*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/0e9f4621713322cc25850b6b032d13bc31696736/torch/nn/functional.py#L3180)

Compute the negative log likelihood loss.

See [`NLLLoss`](torch.nn.NLLLoss.html#torch.nn.NLLLoss) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - (N,C)(N, C)(N,C) where C = number of classes or (N,C,H,W)(N, C, H, W)(N,C,H,W)
in case of 2D Loss, or (N,C,d1,d2,...,dK)(N, C, d_1, d_2, ..., d_K)(N,C,d1​,d2​,...,dK​) where K≥1K \geq 1K≥1
in the case of K-dimensional loss. input is expected to be log-probabilities.
- **target** ([*Tensor*](../tensors.html#torch.Tensor)) - (N)(N)(N) where each value is 0≤targets[i]≤C−10 \leq \text{targets}[i] \leq C-10≤targets[i]≤C−1,
or (N,d1,d2,...,dK)(N, d_1, d_2, ..., d_K)(N,d1​,d2​,...,dK​) where K≥1K \geq 1K≥1 for
K-dimensional loss.
- **weight** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - A manual rescaling weight given to each
class. If given, has to be a Tensor of size C
- **size_average** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **ignore_index** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Specifies a target value that is ignored
and does not contribute to the input gradient. When `size_average` is
`True`, the loss is averaged over non-ignored targets. Default: -100
- **reduce** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. `'none'`: no reduction will be applied,
`'mean'`: the sum of the output will be divided by the number of
elements in the output, `'sum'`: the output will be summed. Note: `size_average`
and `reduce` are in the process of being deprecated, and in the meantime,
specifying either of those two args will override `reduction`. Default: `'mean'`

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Example:

```
>>> # input is of size N x C = 3 x 5
>>> input = torch.randn(3, 5, requires_grad=True)
>>> # each element in target has to have 0 <= value < C
>>> target = torch.tensor([1, 0, 4])
>>> output = F.nll_loss(F.log_softmax(input, dim=1), target)
>>> output.backward()
```