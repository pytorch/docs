# torch.nn.utils.clip_grad.clip_grad_norm

torch.nn.utils.clip_grad.clip_grad_norm(*parameters*, *max_norm*, *norm_type=2.0*, *error_if_nonfinite=False*, *foreach=None*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/nn/utils/clip_grad.py#L235)

Clip the gradient norm of an iterable of parameters.

Warning

This method is now deprecated in favor of
[`torch.nn.utils.clip_grad_norm_()`](torch.nn.utils.clip_grad_norm_.html#torch.nn.utils.clip_grad_norm_).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)