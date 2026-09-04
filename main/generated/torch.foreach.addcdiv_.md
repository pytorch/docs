# torch.foreach.addcdiv_

torch.foreach.addcdiv_(*inputs: TensorList*, *tensor1: TensorList*, *tensor2: TensorList*, */*, ***, *value: ScalarList*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)][[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/foreach/__init__.py#L1359)

torch.foreach.addcdiv_(*inputs: TensorList*, *tensor1: TensorList*, *tensor2: TensorList*, */*, ***, *value: [Tensor](../tensors.html#torch.Tensor)*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)]

torch.foreach.addcdiv_(*inputs: TensorList*, *tensor1: TensorList*, *tensor2: TensorList*, */*, ***, *value: Scalar = 1*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)]

Applies [`torch.addcdiv()`](torch.addcdiv.html#torch.addcdiv) to corresponding tensors from the three input
lists.

This is semantically equivalent to applying [`torch.addcdiv()`](torch.addcdiv.html#torch.addcdiv) independently
at every list position. Mutates every tensor in `inputs` and returns the exact input container object.

Tensor-list arguments must be non-empty.
Corresponding tensor or scalar lists must have the same length.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

`value` may be one shared scalar, a scalar list or tuple, or a packed 1-D
CPU tensor containing one scalar per list position.

Parameters:

- **inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to transform.
- **tensor1** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - first multiplicative or divisive operands.
- **tensor2** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - second multiplicative or divisive operands.
- **value** (*Number**,*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**Number**, or*[*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - scale values.
Default: `1`.

Returns:

the exact input list or tuple.