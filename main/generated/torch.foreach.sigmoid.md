# torch.foreach.sigmoid

torch.foreach.sigmoid(*inputs: TensorList*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...][[source]](https://github.com/pytorch/pytorch/blob/c9fded8194d3b089ed610b586eb746a6e74c6616/torch/foreach/__init__.py#L590)

Applies [`torch.sigmoid()`](torch.sigmoid.html#torch.sigmoid) to each tensor in `inputs`.

This is semantically equivalent to applying [`torch.sigmoid()`](torch.sigmoid.html#torch.sigmoid) independently
at every list position. Does not mutate its arguments and returns a tuple of result tensors.

Tensor-list arguments must be non-empty.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

Parameters:

**inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to transform.

Returns:

a tuple containing one result tensor for each input tensor.