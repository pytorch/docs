# torch.foreach.norm

torch.foreach.norm(*inputs: TensorList*, */*, ***, *ord: Scalar = 2*, *dtype: [dtype](../tensor_attributes.html#torch.dtype) | [None](https://docs.python.org/3/library/constants.html#None) = None*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...][[source]](https://github.com/pytorch/pytorch/blob/c9fded8194d3b089ed610b586eb746a6e74c6616/torch/foreach/__init__.py#L1578)

Returns the vector norm of each tensor in `inputs`.

This is semantically equivalent to applying [`torch.linalg.vector_norm()`](torch.linalg.vector_norm.html#torch.linalg.vector_norm) independently
at every list position. Does not mutate its arguments and returns a tuple of result tensors.

Tensor-list arguments must be non-empty.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

Every input tensor is reduced over all dimensions. The `dim` and
`keepdim` options of [`torch.linalg.vector_norm()`](torch.linalg.vector_norm.html#torch.linalg.vector_norm) are not supported.

Parameters:

- **inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to reduce.
- **ord** (*Number**,**optional*) - norm order. Default: `2`.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - dtype used for the computation.

Returns:

a tuple containing one norm tensor per input tensor.