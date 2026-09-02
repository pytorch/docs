# torch.foreach.zero_

torch.foreach.zero_(*inputs: TensorList*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)][[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/foreach/__init__.py#L1636)

Fills every tensor in `inputs` with zero.

This is semantically equivalent to applying [`torch.Tensor.zero_()`](torch.Tensor.zero_.html#torch.Tensor.zero_) independently
at every list position. Mutates every tensor in `inputs` and returns the exact input container object.

Tensor-list arguments must be non-empty.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

There is no functional `torch.foreach.zero` operation.

Parameters:

**inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to zero.

Returns:

the exact `inputs` list or tuple.