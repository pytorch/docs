# torch.nn.functional.multi_margin_loss

torch.nn.functional.multi_margin_loss(*input*, *target*, *p=1*, *margin=1.0*, *weight=None*, *size_average=None*, *reduce=None*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/nn/functional.py#L4633)

Compute the multi margin loss, with optional weighting.

See [`MultiMarginLoss`](torch.nn.MultiMarginLoss.html#torch.nn.MultiMarginLoss) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Predicted values.
- **target** ([*Tensor*](../tensors.html#torch.Tensor)) - Ground truth values.
- **p** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Has a default value of 1. 1 and 2 are the only supported values.
- **margin** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - Margin for multi margin loss. Has a default value of 1.
- **weight** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - Weights for each sample. Default: None.
- **size_average** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduce** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
'none' | 'mean' | 'sum'. 'mean': the mean of the output is taken.
'sum': the output will be summed. 'none': no reduction will be applied.
Default: 'mean'.

Returns:

Multi margin loss (optionally weighted).

Return type:

[Tensor](../tensors.html#torch.Tensor)