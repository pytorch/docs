# torch.nn.functional.local_response_norm

torch.nn.functional.local_response_norm(*input*, *size*, *alpha=0.0001*, *beta=0.75*, *k=1.0*)[[source]](https://github.com/pytorch/pytorch/blob/a62499b17156f49891b06593215215c6df2f94b4/torch/nn/functional.py#L3053)

Apply local response normalization over an input signal.

The input signal is composed of several input planes, where channels occupy the second dimension.
Normalization is applied across channels.

See [`LocalResponseNorm`](torch.nn.LocalResponseNorm.html#torch.nn.LocalResponseNorm) for details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)