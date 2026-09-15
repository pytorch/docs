# torch.nn.utils.clip_grads_with_norm_

torch.nn.utils.clip_grads_with_norm_(*parameters*, *max_norm*, *total_norm*, *foreach=None*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/nn/utils/clip_grad.py#L119)

Scale the gradients of an iterable of parameters given a pre-calculated total norm and desired max norm.

The gradients will be scaled by the following calculation

grad=grad∗min⁡(max_normtotal_norm+1e−6,1)grad = grad * \min(\frac{max\_norm}{total\_norm + 1e-6}, 1)

grad=grad∗min(total_norm+1e−6max_norm​,1)

Gradients are modified in-place.

Note: The scale coefficient is clamped to a maximum of 1.0 to prevent gradient amplification.
This ensures that gradients are only scaled down when the total norm exceeds max_norm.

This function is equivalent to [`torch.nn.utils.clip_grad_norm_()`](torch.nn.utils.clip_grad_norm_.html#torch.nn.utils.clip_grad_norm_) with a pre-calculated
total norm.

Parameters:

- **parameters** (*Iterable**[*[*Tensor*](../tensors.html#torch.Tensor)*] or*[*Tensor*](../tensors.html#torch.Tensor)) - an iterable of Tensors or a
single Tensor that will have gradients normalized
- **max_norm** ([*float*](https://docs.python.org/3/builtins/functions.html#float)) - max norm of the gradients
- **total_norm** ([*Tensor*](../tensors.html#torch.Tensor)) - total norm of the gradients to use for clipping
- **foreach** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - use the faster foreach-based implementation.
If `None`, use the foreach implementation for CUDA and CPU native tensors and silently
fall back to the slow implementation for other device types.
Default: `None`

Returns:

None

Return type:

None