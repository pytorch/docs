# torch.nn.functional.adaptive_avg_pool1d

torch.nn.functional.adaptive_avg_pool1d(*input*, *output_size*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/56964c25c21235cf3a06679d2e400195087f64fb/torch/nn/functional.py#L1396)

Applies a 1D adaptive average pooling over an input signal composed of
several input planes.

See [`AdaptiveAvgPool1d`](torch.nn.AdaptiveAvgPool1d.html#torch.nn.AdaptiveAvgPool1d) for details and output shape.

Parameters:

**output_size** - the target output size (single integer)