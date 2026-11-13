# torch.nn.functional.adaptive_avg_pool1d

torch.nn.functional.adaptive_avg_pool1d(*input*, *output_size*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/b896199bee9ca0e125f6ec366a265418a8f3290e/torch/nn/functional.py#L1471)

Applies a 1D adaptive average pooling over an input signal composed of
several input planes.

See [`AdaptiveAvgPool1d`](torch.nn.AdaptiveAvgPool1d.html#torch.nn.AdaptiveAvgPool1d) for details and output shape.

Parameters:

**output_size** - the target output size (single integer)