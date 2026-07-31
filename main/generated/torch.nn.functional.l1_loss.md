# torch.nn.functional.l1_loss

torch.nn.functional.l1_loss(*input*, *target*, *size_average=None*, *reduce=None*, *reduction='mean'*, *weight=None*)[[source]](https://github.com/pytorch/pytorch/blob/f613b2a0a05cebc8f0b0095458f6f2219008b0dd/torch/nn/functional.py#L4195)

Compute the L1 loss, with optional weighting.

Function that takes the mean element-wise absolute value difference.

See [`L1Loss`](torch.nn.L1Loss.html#torch.nn.L1Loss) for details.

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

L1 loss (optionally weighted).

Return type:

[Tensor](../tensors.html#torch.Tensor)