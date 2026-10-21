# torch.sparse.log_softmax

torch.sparse.log_softmax(*input*, *dim*, ***, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/7ffd47d270087d6dbafb876c0549d949aabf0a5a/torch/sparse/__init__.py#L338)

Applies a softmax function followed by logarithm.

See [`softmax`](torch.sparse.softmax.html#torch.sparse.softmax) for more details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - input
- **dim** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - A dimension along which softmax will be computed.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type
of returned tensor. If specified, the input tensor is
casted to `dtype` before the operation is
performed. This is useful for preventing data type
overflows. Default: None