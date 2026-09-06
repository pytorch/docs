# torch.foreach.div

torch.foreach.div(*inputs: TensorList*, *other: ScalarList*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...][[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/foreach/__init__.py#L942)

torch.foreach.div(*inputs: TensorList*, *other: [Tensor](../tensors.html#torch.Tensor)*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...]

torch.foreach.div(*inputs: TensorList*, *other: TensorList*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...]

torch.foreach.div(*inputs: TensorList*, *other: Scalar*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...]

Applies [`torch.div()`](torch.div.html#torch.div) to every tensor in `inputs`.

This is semantically equivalent to applying [`torch.div()`](torch.div.html#torch.div) independently
at every list position. Does not mutate its arguments and returns a tuple of result tensors.

Tensor-list arguments must be non-empty.
Corresponding tensor or scalar lists must have the same length.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

A shared `Tensor` operand must be a 0-D scalar tensor.

The `rounding_mode` argument is not supported.

Parameters:

- **inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to transform.
- **other** (*Number**,*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**Number**, or*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)*, or*[*Tensor*](../tensors.html#torch.Tensor)) - operand shared across positions or supplied per
position.

Returns:

a tuple containing one result tensor for each input tensor.