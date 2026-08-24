# torch.foreach.reciprocal_

torch.foreach.reciprocal_(*inputs: TensorList*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)][[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/foreach/__init__.py#L550)

Applies [`torch.reciprocal()`](torch.reciprocal.html#torch.reciprocal) to each tensor in `inputs` in-place.

This is semantically equivalent to applying [`torch.reciprocal()`](torch.reciprocal.html#torch.reciprocal) independently
at every list position. Mutates every tensor in `inputs` and returns the exact input container object.

Tensor-list arguments must be non-empty.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

Parameters:

**inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to transform.

Returns:

the exact input list or tuple.