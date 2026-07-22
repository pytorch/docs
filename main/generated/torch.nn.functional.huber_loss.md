# torch.nn.functional.huber_loss

torch.nn.functional.huber_loss(*input*, *target*, *reduction='mean'*, *delta=1.0*, *weight=None*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/nn/functional.py#L4107)

Compute the Huber loss, with optional weighting.

Function uses a squared term if the absolute
element-wise error falls below delta and a delta-scaled L1 term otherwise.

When delta equals 1, this loss is equivalent to SmoothL1Loss.
In general, Huber loss differs from SmoothL1Loss by a factor of delta (AKA beta in Smooth L1).

See [`HuberLoss`](torch.nn.HuberLoss.html#torch.nn.HuberLoss) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Predicted values.
- **target** ([*Tensor*](../tensors.html#torch.Tensor)) - Ground truth values.
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
'none' | 'mean' | 'sum'. 'mean': the mean of the output is taken.
'sum': the output will be summed. 'none': no reduction will be applied.
Default: 'mean'.
- **delta** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - The threshold at which to change between delta-scaled L1 and L2 loss. Default: 1.0.
- **weight** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - Weights for each sample. Default: None.

Returns:

Huber loss (optionally weighted).

Return type:

[Tensor](../tensors.html#torch.Tensor)