# torch.foreach.minimum_

torch.foreach.minimum_(*inputs: TensorList*, *other: Scalar*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)][[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/foreach/__init__.py#L1119)

torch.foreach.minimum_(*inputs: TensorList*, *other: ScalarList*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)]

torch.foreach.minimum_(*inputs: TensorList*, *other: TensorList*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)]

Applies [`torch.minimum()`](torch.minimum.html#torch.minimum) to every tensor in `inputs`.

This is semantically equivalent to applying [`torch.minimum()`](torch.minimum.html#torch.minimum) independently
at every list position. Mutates every tensor in `inputs` and returns the exact input container object.

Tensor-list arguments must be non-empty.
Corresponding tensor or scalar lists must have the same length.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

Scalar and `ScalarList` forms are semantically equivalent to [`torch.clamp()`](torch.clamp.html#torch.clamp) with only `max` specified.

Parameters:

- **inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to transform.
- **other** (*Number**,*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**Number**, or*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - operand shared across positions or supplied per
position.

Returns:

the exact input list or tuple.