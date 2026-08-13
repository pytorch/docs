# torch.nn.functional.multilabel_soft_margin_loss

torch.nn.functional.multilabel_soft_margin_loss(*input*, *target*, *weight=None*, *size_average=None*, *reduce=None*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/nn/functional.py#L4526)

Compute the multilabel soft margin loss.

See [`MultiLabelSoftMarginLoss`](torch.nn.MultiLabelSoftMarginLoss.html#torch.nn.MultiLabelSoftMarginLoss) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Predicted values.
- **target** ([*Tensor*](../tensors.html#torch.Tensor)) - Ground truth values.
- **size_average** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduce** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
'none' | 'mean' | 'sum'. 'mean': the mean of the output is taken.
'sum': the output will be summed. 'none': no reduction will be applied.
Default: 'mean'.

Returns:

Mutilabel soft margin loss.

Return type:

[Tensor](../tensors.html#torch.Tensor)