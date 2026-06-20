# torch.nn.functional.mse_loss

torch.nn.functional.mse_loss(*input*, *target*, *size_average=None*, *reduce=None*, *reduction='mean'*, *weight=None*)[[source]](https://github.com/pytorch/pytorch/blob/27b52de22e4e5fa572c07a4065423083a41b8756/torch/nn/functional.py#L4245)

Compute the element-wise mean squared error, with optional weighting.

See [`MSELoss`](torch.nn.MSELoss.html#torch.nn.MSELoss) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Predicted values.
- **target** ([*Tensor*](../tensors.html#torch.Tensor)) - Ground truth values.
- **size_average** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduce** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
'none' | 'mean' | 'sum'. 'mean': the mean of the output is taken.
'sum': the output will be summed. 'none': no reduction will be applied.
Default: 'mean'.
- **weight** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - Weights for each sample. Default: None.

Returns:

Mean Squared Error loss (optionally weighted).

Return type:

[Tensor](../tensors.html#torch.Tensor)