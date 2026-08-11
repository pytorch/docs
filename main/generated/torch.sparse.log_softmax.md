# torch.sparse.log_softmax

torch.sparse.log_softmax(*input*, *dim*, ***, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/ab02f71479d3b0fb41d5b722bbe1943340f2022b/torch/sparse/__init__.py#L338)

Applies a softmax function followed by logarithm.

See [`softmax`](torch.sparse.softmax.html#torch.sparse.softmax) for more details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - input
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - A dimension along which softmax will be computed.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type
of returned tensor. If specified, the input tensor is
casted to `dtype` before the operation is
performed. This is useful for preventing data type
overflows. Default: None