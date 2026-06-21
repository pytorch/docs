# torch.nn.utils.clip_grad.clip_grad_norm_

torch.nn.utils.clip_grad.clip_grad_norm_(*parameters*, *max_norm*, *norm_type=2.0*, *error_if_nonfinite=False*, *foreach=None*)[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/nn/utils/clip_grad.py#L184)

Clip the gradient norm of an iterable of parameters.

The norm is computed over the norms of the individual gradients of all parameters,
as if the norms of the individual gradients were concatenated into a single vector.
Gradients are modified in-place.

This function is equivalent to [`torch.nn.utils.get_total_norm()`](torch.nn.utils.get_total_norm.html#torch.nn.utils.get_total_norm) followed by
[`torch.nn.utils.clip_grads_with_norm_()`](torch.nn.utils.clip_grads_with_norm_.html#torch.nn.utils.clip_grads_with_norm_) with the `total_norm` returned by `get_total_norm`.

Parameters:

- **parameters** (*Iterable**[*[*Tensor*](../tensors.html#torch.Tensor)*] or*[*Tensor*](../tensors.html#torch.Tensor)) - an iterable of Tensors or a
single Tensor that will have gradients normalized
- **max_norm** ([*float*](https://docs.python.org/3/library/functions.html#float)) - max norm of the gradients
- **norm_type** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - type of the used p-norm. Can be `'inf'` for
infinity norm. Default: 2.0
- **error_if_nonfinite** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - if True, an error is thrown if the total
norm of the gradients from `parameters` is `nan`,
`inf`, or `-inf`. Default: False
- **foreach** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - use the faster foreach-based implementation.
If `None`, use the foreach implementation for CUDA and CPU native tensors and silently
fall back to the slow implementation for other device types.
Default: `None`

Returns:

Total norm of the parameter gradients (viewed as a single vector).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)