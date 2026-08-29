# torch.foreach.expm1

torch.foreach.expm1(*inputs: TensorList*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...][[source]](https://github.com/pytorch/pytorch/blob/fe3f518c806b6f1fb8acc283135e5414b8606887/torch/foreach/__init__.py#L446)

Applies [`torch.expm1()`](torch.expm1.html#torch.expm1) to each tensor in `inputs`.

This is semantically equivalent to applying [`torch.expm1()`](torch.expm1.html#torch.expm1) independently
at every list position. Does not mutate its arguments and returns a tuple of result tensors.

Tensor-list arguments must be non-empty.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

Parameters:

**inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to transform.

Returns:

a tuple containing one result tensor for each input tensor.