# torch.nn.functional.adaptive_avg_pool1d

torch.nn.functional.adaptive_avg_pool1d(*input*, *output_size*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/nn/functional.py#L1376)

Applies a 1D adaptive average pooling over an input signal composed of
several input planes.

See [`AdaptiveAvgPool1d`](torch.nn.AdaptiveAvgPool1d.html#torch.nn.AdaptiveAvgPool1d) for details and output shape.

Parameters:

**output_size** - the target output size (single integer)