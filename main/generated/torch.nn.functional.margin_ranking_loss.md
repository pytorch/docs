# torch.nn.functional.margin_ranking_loss

torch.nn.functional.margin_ranking_loss(*input1*, *input2*, *target*, *margin=0*, *size_average=None*, *reduce=None*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/nn/functional.py#L4347)

Compute the margin ranking loss.

See [`MarginRankingLoss`](torch.nn.MarginRankingLoss.html#torch.nn.MarginRankingLoss) for details.

Parameters:

- **input1** ([*Tensor*](../tensors.html#torch.Tensor)) - Predicted values.
- **input2** ([*Tensor*](../tensors.html#torch.Tensor)) - Predicted values.
- **target** ([*Tensor*](../tensors.html#torch.Tensor)) - Ground truth values.
- **size_average** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduce** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
'none' | 'mean' | 'sum'. 'mean': the mean of the output is taken.
'sum': the output will be summed. 'none': no reduction will be applied.
Default: 'mean'.

Returns:

Margin ranking loss.

Return type:

[Tensor](../tensors.html#torch.Tensor)