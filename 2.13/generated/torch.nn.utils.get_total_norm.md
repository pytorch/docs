# torch.nn.utils.get_total_norm

torch.nn.utils.get_total_norm(*tensors*, *norm_type=2.0*, *error_if_nonfinite=False*, *foreach=None*)[[source]](https://github.com/pytorch/pytorch/blob/v2.13.0/torch/nn/utils/clip_grad.py#L48)

Compute the norm of an iterable of tensors.

The norm is computed over the norms of the individual tensors, as if the norms of
the individual tensors were concatenated into a single vector.

Parameters:

- **tensors** (*Iterable**[*[*Tensor*](../tensors.html#torch.Tensor)*] or*[*Tensor*](../tensors.html#torch.Tensor)) - an iterable of Tensors or a
single Tensor that will be normalized
- **norm_type** ([*float*](https://docs.python.org/3/library/functions.html#float)) - type of the used p-norm. Can be `'inf'` for
infinity norm.
- **error_if_nonfinite** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - if True, an error is thrown if the total
norm of `tensors` is `nan`, `inf`, or `-inf`.
Default: `False`
- **foreach** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - use the faster foreach-based implementation.
If `None`, use the foreach implementation for CUDA and CPU native tensors and silently
fall back to the slow implementation for other device types.
Default: `None`

Returns:

Total norm of the tensors (viewed as a single vector).

Return type:

[*Tensor*](../tensors.html#torch.Tensor)