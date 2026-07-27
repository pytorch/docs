# torch.nn.functional.binary_cross_entropy_with_logits

torch.nn.functional.binary_cross_entropy_with_logits(*input*, *target*, *weight=None*, *size_average=None*, *reduce=None*, *reduction='mean'*, *pos_weight=None*)[[source]](https://github.com/pytorch/pytorch/blob/94de2113ebf2891e498dd58ed1a16fedac39b5c6/torch/nn/functional.py#L3634)

Compute Binary Cross Entropy between target and input logits.

See [`BCEWithLogitsLoss`](torch.nn.BCEWithLogitsLoss.html#torch.nn.BCEWithLogitsLoss) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Tensor of arbitrary shape as unnormalized scores (often referred to as logits).
- **target** ([*Tensor*](../tensors.html#torch.Tensor)) - Tensor of the same shape as input with values between 0 and 1
- **weight** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - a manual rescaling weight. If provided, the dimension
of weight supports [broadcasting to a common shape](../notes/broadcasting.html#broadcasting-semantics)
with respect to the input (and target) shape.
- **size_average** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduce** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. `'none'`: no reduction will be applied,
`'mean'`: the sum of the output will be divided by the number of
elements in the output, `'sum'`: the output will be summed. Note: `size_average`
and `reduce` are in the process of being deprecated, and in the meantime,
specifying either of those two args will override `reduction`. Default: `'mean'`
- **pos_weight** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - a weight of positive examples to be broadcasted with target.
Must be a tensor with equal size along the class dimension to the number of classes.
Pay close attention to PyTorch's broadcasting semantics in order to achieve the desired
operations. For a target of size [B, C, H, W] (where B is batch size) pos_weight of
size [B, C, H, W] will apply different pos_weights to each element of the batch or
[C, H, W] the same pos_weights across the batch. To apply the same positive weight
along all spatial dimensions for a 2D multi-class target [C, H, W] use: [C, 1, 1].
Default: `None`

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Examples:

```
>>> input = torch.randn(3, requires_grad=True)
>>> target = torch.empty(3).random_(2)
>>> loss = F.binary_cross_entropy_with_logits(input, target)
>>> loss.backward()
```