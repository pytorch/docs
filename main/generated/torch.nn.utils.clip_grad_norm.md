# torch.nn.utils.clip_grad_norm

torch.nn.utils.clip_grad_norm(*parameters*, *max_norm*, *norm_type=2.0*, *error_if_nonfinite=False*, *foreach=None*)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/nn/utils/clip_grad.py#L235)

Clip the gradient norm of an iterable of parameters.

Warning

This method is now deprecated in favor of
[`torch.nn.utils.clip_grad_norm_()`](torch.nn.utils.clip_grad_norm_.html#torch.nn.utils.clip_grad_norm_).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)