# torch.foreach.clamp_min_

torch.foreach.clamp_min_(*inputs: TensorList*, *min: Scalar*, */*) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)][[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/foreach/__init__.py#L1019)

torch.foreach.clamp_min_(*inputs: TensorList*, *min: ScalarList*, */*) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)]

torch.foreach.clamp_min_(*inputs: TensorList*, *min: TensorList*, */*) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)]

Applies [`torch.clamp()`](torch.clamp.html#torch.clamp) to every tensor in `inputs`.

This is semantically equivalent to applying [`torch.clamp()`](torch.clamp.html#torch.clamp) independently
at every list position. Mutates every tensor in `inputs` and returns the exact input container object.

Tensor-list arguments must be non-empty.
Corresponding tensor or scalar lists must have the same length.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

Only the `min` bound is specified.

Parameters:

- **inputs** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to transform.
- **min** (*Number**,*[*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*of**Number**, or*[*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - operand shared across positions or supplied per
position.

Returns:

the exact input list or tuple.