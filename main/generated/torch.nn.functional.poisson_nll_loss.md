# torch.nn.functional.poisson_nll_loss

torch.nn.functional.poisson_nll_loss(*input*, *target*, *log_input=True*, *full=False*, *size_average=None*, *eps=1e-08*, *reduce=None*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/40e21dcd4b92d59842b3e3b7f542f855dedddb91/torch/nn/functional.py#L3241)

Compute the Poisson negative log likelihood loss.

See [`PoissonNLLLoss`](torch.nn.PoissonNLLLoss.html#torch.nn.PoissonNLLLoss) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Expectation of underlying Poisson distribution.
- **target** ([*Tensor*](../tensors.html#torch.Tensor)) - Random sample target∼Poisson(input)target \sim \text{Poisson}(input)target∼Poisson(input).
- **log_input** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True` the loss is computed as
exp⁡(input)−target∗input\exp(\text{input}) - \text{target} * \text{input}exp(input)−target∗input, if `False` then loss is
input−target∗log⁡(input+eps)\text{input} - \text{target} * \log(\text{input}+\text{eps})input−target∗log(input+eps). Default: `True`
- **full** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to compute full loss, i. e. to add the Stirling
approximation term. Default: `False`
target∗log⁡(target)−target+0.5∗log⁡(2∗π∗target)\text{target} * \log(\text{target}) - \text{target} + 0.5 * \log(2 * \pi * \text{target})target∗log(target)−target+0.5∗log(2∗π∗target).
- **size_average** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - Small value to avoid evaluation of log⁡(0)\log(0)log(0) when
`log_input`=`False`. Default: 1e-8
- **reduce** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. `'none'`: no reduction will be applied,
`'mean'`: the sum of the output will be divided by the number of
elements in the output, `'sum'`: the output will be summed. Note: `size_average`
and `reduce` are in the process of being deprecated, and in the meantime,
specifying either of those two args will override `reduction`. Default: `'mean'`

Return type:

[*Tensor*](../tensors.html#torch.Tensor)