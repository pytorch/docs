# torch.foreach.clamp_max

torch.foreach.clamp_max(*inputs: TensorList*, *max: Scalar*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...][[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/foreach/__init__.py#L1044)

torch.foreach.clamp_max(*inputs: TensorList*, *max: ScalarList*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...]

torch.foreach.clamp_max(*inputs: TensorList*, *max: TensorList*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...]

Applies [`torch.clamp()`](torch.clamp.html#torch.clamp) to every tensor in `inputs`.

This is semantically equivalent to applying [`torch.clamp()`](torch.clamp.html#torch.clamp) independently
at every list position. Does not mutate its arguments and returns a tuple of result tensors.

Tensor-list arguments must be non-empty.
Corresponding tensor or scalar lists must have the same length.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

Only the `max` bound is specified.

Parameters:

- **inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to transform.
- **max** (*Number**,*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**Number**, or*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - operand shared across positions or supplied per
position.

Returns:

a tuple containing one result tensor for each input tensor.