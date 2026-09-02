# torch.foreach.expm1_

torch.foreach.expm1_(*inputs: TensorList*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)][[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/foreach/__init__.py#L451)

Applies [`torch.expm1()`](torch.expm1.html#torch.expm1) to each tensor in `inputs` in-place.

This is semantically equivalent to applying [`torch.expm1()`](torch.expm1.html#torch.expm1) independently
at every list position. Mutates every tensor in `inputs` and returns the exact input container object.

Tensor-list arguments must be non-empty.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

Parameters:

**inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to transform.

Returns:

the exact input list or tuple.