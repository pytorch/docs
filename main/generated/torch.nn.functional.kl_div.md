# torch.nn.functional.kl_div

torch.nn.functional.kl_div(*input*, *target*, *size_average=None*, *reduce=None*, *reduction='mean'*, *log_target=False*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/nn/functional.py#L3401)

Compute the KL Divergence loss.

Refer - The [Kullback-Leibler divergence Loss](https://en.wikipedia.org/wiki/Kullback-Leibler_divergence)

See [`KLDivLoss`](torch.nn.KLDivLoss.html#torch.nn.KLDivLoss) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Tensor of arbitrary shape in log-probabilities.
- **target** ([*Tensor*](../tensors.html#torch.Tensor)) - Tensor of the same shape as input. See `log_target` for
the target's interpretation.
- **size_average** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduce** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
`'none'` | `'batchmean'` | `'sum'` | `'mean'`.
`'none'`: no reduction will be applied
`'batchmean'`: the sum of the output will be divided by the batchsize
`'sum'`: the output will be summed
`'mean'`: the output will be divided by the number of elements in the output
Default: `'mean'`
- **log_target** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - A flag indicating whether `target` is passed in the log space.
It is recommended to pass certain distributions (like `softmax`)
in the log space to avoid numerical issues caused by explicit `log`.
Default: `False`

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Note

`size_average` and `reduce` are in the process of being deprecated,
and in the meantime, specifying either of those two args will override `reduction`.

Warning

`reduction` = `'mean'` doesn't return the true kl divergence value, please use
`reduction` = `'batchmean'` which aligns with KL math definition.