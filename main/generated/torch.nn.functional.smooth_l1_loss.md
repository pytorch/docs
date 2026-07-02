# torch.nn.functional.smooth_l1_loss

torch.nn.functional.smooth_l1_loss(*input*, *target*, *size_average=None*, *reduce=None*, *reduction='mean'*, *beta=1.0*)[[source]](https://github.com/pytorch/pytorch/blob/613fb8c0f7fc1641d104e1ba45491d522964094c/torch/nn/functional.py#L4036)

Compute the Smooth L1 loss.

Function uses a squared term if the absolute
element-wise error falls below beta and an L1 term otherwise.

See [`SmoothL1Loss`](torch.nn.SmoothL1Loss.html#torch.nn.SmoothL1Loss) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Predicted values.
- **target** ([*Tensor*](../tensors.html#torch.Tensor)) - Ground truth values.
- **size_average** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduce** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
'none' | 'mean' | 'sum'. 'mean': the mean of the output is taken.
'sum': the output will be summed. 'none': no reduction will be applied.
Default: 'mean'.
- **beta** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - Specifies the threshold at which to change from the squared
term to the L1 term in the loss calculation. This value must be positive.
Default: 1.0.

Returns:

L1 loss (optionally weighted).

Return type:

[Tensor](../tensors.html#torch.Tensor)