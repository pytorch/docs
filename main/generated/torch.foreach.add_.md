# torch.foreach.add_

torch.foreach.add_(*inputs: TensorList*, *other: Scalar*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)][[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/foreach/__init__.py#L765)

torch.foreach.add_(*inputs: TensorList*, *other: ScalarList*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)]

torch.foreach.add_(*inputs: TensorList*, *other: [Tensor](../tensors.html#torch.Tensor)*, */*, ***, *alpha: Scalar*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)]

torch.foreach.add_(*inputs: TensorList*, *other: TensorList*, */*, ***, *alpha: Scalar = 1*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)]

Applies [`torch.add()`](torch.add.html#torch.add) to every tensor in `inputs`.

This is semantically equivalent to applying [`torch.add()`](torch.add.html#torch.add) independently
at every list position. Mutates every tensor in `inputs` and returns the exact input container object.

Tensor-list arguments must be non-empty.
Corresponding tensor or scalar lists must have the same length.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

A shared `Tensor` operand must be a 0-D scalar tensor.

For a shared 0-D tensor, pass `alpha` explicitly, including when its value is `1`, to select the Tensor overload. Omitting `alpha` may convert the tensor to a host scalar.

Parameters:

- **inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to transform.
- **other** (*Number**,*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**Number**, or*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)*, or*[*Tensor*](../tensors.html#torch.Tensor)) - operand shared across positions or supplied per
position.
- **alpha** (*Number**,**optional*) - supported only when `other` is a tensor list or a shared 0-D scalar tensor. Default: `1`.

Returns:

the exact input list or tuple.