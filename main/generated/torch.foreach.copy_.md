# torch.foreach.copy_

torch.foreach.copy_(*inputs: TensorList*, *src: TensorList*, */*, ***, *non_blocking: [bool](https://docs.python.org/3/library/functions.html#bool) = False*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)][[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/foreach/__init__.py#L1606)

Copies each tensor in `src` into the corresponding tensor in
`inputs`, following [`torch.Tensor.copy_()`](torch.Tensor.copy_.html#torch.Tensor.copy_).

This is semantically equivalent to applying [`torch.Tensor.copy_()`](torch.Tensor.copy_.html#torch.Tensor.copy_) independently
at every list position. Mutates every tensor in `inputs` and returns the exact input container object.

Tensor-list arguments must be non-empty.
Corresponding tensor or scalar lists must have the same length.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

There is no functional `torch.foreach.copy` operation.

Parameters:

- **inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - destination tensors.
- **src** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - source tensors.
- **non_blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - allows asynchronous host/device copies when
supported. Default: `False`.

Returns:

the exact `inputs` list or tuple.