# torch.nn.functional.gaussian_nll_loss

torch.nn.functional.gaussian_nll_loss(*input*, *target*, *var*, *full=False*, *eps=1e-06*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/3f8cf8d55cb309421fc5433c518b11b5f9c7a0a0/torch/nn/functional.py#L3259)

Compute the Gaussian negative log likelihood loss.

See [`GaussianNLLLoss`](torch.nn.GaussianNLLLoss.html#torch.nn.GaussianNLLLoss) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Expectation of the Gaussian distribution.
- **target** ([*Tensor*](../tensors.html#torch.Tensor)) - Sample from the Gaussian distribution.
- **var** ([*Tensor*](../tensors.html#torch.Tensor)*|*[*float*](https://docs.python.org/3/library/functions.html#float)) - Tensor of positive variance(s), one for each of the expectations
in the input (heteroscedastic), or a single one (homoscedastic),
or a positive scalar value to be used for all expectations.
- **full** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether to include the constant term in the loss calculation. Default: `False`.
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - Value added to var, for stability. Default: 1e-6.
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. `'none'`: no reduction will be applied,
`'mean'`: the output is the average of all batch member losses,
`'sum'`: the output is the sum of all batch member losses.
Default: `'mean'`.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)