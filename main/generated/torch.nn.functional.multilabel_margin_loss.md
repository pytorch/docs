# torch.nn.functional.multilabel_margin_loss

torch.nn.functional.multilabel_margin_loss(*input*, *target*, *size_average=None*, *reduce=None*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/e1994aea9ce307fb82feeb7524ab2c5d36771e4f/torch/nn/functional.py#L4466)

Compute the multilabel margin loss.

See [`MultiLabelMarginLoss`](torch.nn.MultiLabelMarginLoss.html#torch.nn.MultiLabelMarginLoss) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Predicted values.
- **target** ([*Tensor*](../tensors.html#torch.Tensor)) - Ground truth values.
- **size_average** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduce** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduction** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
'none' | 'mean' | 'sum'. 'mean': the mean of the output is taken.
'sum': the output will be summed. 'none': no reduction will be applied.
Default: 'mean'.

Returns:

Mutilabel margin loss.

Return type:

[Tensor](../tensors.html#torch.Tensor)