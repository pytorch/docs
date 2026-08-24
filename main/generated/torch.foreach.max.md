# torch.foreach.max

torch.foreach.max(*inputs: TensorList*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...][[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/foreach/__init__.py#L1558)

Returns the maximum value of each tensor in `inputs`.

This is semantically equivalent to applying [`torch.max()`](torch.max.html#torch.max) independently
at every list position. Does not mutate its arguments and returns a tuple of result tensors.

Tensor-list arguments must be non-empty.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

This operation reduces every input tensor over all dimensions. It does not
accept a dimension or return indices.

Parameters:

**inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to reduce.

Returns:

a tuple of scalar tensors.