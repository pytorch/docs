# torch.nn.functional.cosine_embedding_loss

torch.nn.functional.cosine_embedding_loss(*input1*, *input2*, *target*, *margin=0*, *size_average=None*, *reduce=None*, *reduction='mean'*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/nn/functional.py#L4562)

Compute the cosine embedding loss.

See [`CosineEmbeddingLoss`](torch.nn.CosineEmbeddingLoss.html#torch.nn.CosineEmbeddingLoss) for details.

Parameters:

- **input1** ([*Tensor*](../tensors.html#torch.Tensor)) - Predicted values.
- **input2** ([*Tensor*](../tensors.html#torch.Tensor)) - Predicted values.
- **target** ([*Tensor*](../tensors.html#torch.Tensor)) - Ground truth values.
- **margin** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - Margin for cosine embedding. Has a default value of 0.
- **size_average** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduce** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Deprecated (see `reduction`).
- **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Specifies the reduction to apply to the output:
'none' | 'mean' | 'sum'. 'mean': the mean of the output is taken.
'sum': the output will be summed. 'none': no reduction will be applied.
Default: 'mean'.

Returns:

Cosine embedding loss.

Return type:

[Tensor](../tensors.html#torch.Tensor)