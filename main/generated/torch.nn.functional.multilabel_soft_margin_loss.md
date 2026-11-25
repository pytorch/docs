# torch.nn.functional.multilabel_soft_margin_loss

torch.nn.functional.multilabel_soft_margin_loss(*input*, *target*, *weight=None*, *size_average=None*, *reduce=None*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/7e752fbd7bf384857985d3e556423eaca714bbfe/torch/nn/functional.py#L4607)

Compute the multilabel soft margin loss.

See [`MultiLabelSoftMarginLoss`](torch.nn.MultiLabelSoftMarginLoss.html#torch.nn.MultiLabelSoftMarginLoss) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Predicted values.
- **target** ([*Tensor*](../tensors.html#torch.Tensor)) - Ground truth values.
- **weight** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - a manual rescaling weight given to each
class. If given, it has to be a Tensor of size C. Otherwise, it is
treated as if having all ones.
- **size_average** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduce** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduction** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
'none' | 'mean' | 'sum'. 'mean': the mean of the output is taken.
'sum': the output will be summed. 'none': no reduction will be applied.
Default: 'mean'.

Returns:

Multilabel soft margin loss.

Return type:

[Tensor](../tensors.html#torch.Tensor)