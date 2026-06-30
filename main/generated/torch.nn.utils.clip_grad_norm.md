# torch.nn.utils.clip_grad_norm

torch.nn.utils.clip_grad_norm(*parameters*, *max_norm*, *norm_type=2.0*, *error_if_nonfinite=False*, *foreach=None*)[[source]](https://github.com/pytorch/pytorch/blob/c8f2d26abd0de59995af555e80c82ca1221bc21b/torch/nn/utils/clip_grad.py#L235)

Clip the gradient norm of an iterable of parameters.

Warning

This method is now deprecated in favor of
[`torch.nn.utils.clip_grad_norm_()`](torch.nn.utils.clip_grad_norm_.html#torch.nn.utils.clip_grad_norm_).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)