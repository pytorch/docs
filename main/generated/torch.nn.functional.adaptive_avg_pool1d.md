# torch.nn.functional.adaptive_avg_pool1d

torch.nn.functional.adaptive_avg_pool1d(*input*, *output_size*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/ab645165510131aa973a5b8880aa56f565e59c7b/torch/nn/functional.py#L1424)

Applies a 1D adaptive average pooling over an input signal composed of
several input planes.

See [`AdaptiveAvgPool1d`](torch.nn.AdaptiveAvgPool1d.html#torch.nn.AdaptiveAvgPool1d) for details and output shape.

Parameters:

**output_size** - the target output size (single integer)