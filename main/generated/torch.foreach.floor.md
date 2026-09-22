# torch.foreach.floor

torch.foreach.floor(*inputs: TensorList*, */*) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...][[source]](https://github.com/pytorch/pytorch/blob/9d784735eb70fb8b0335b0ad7cad9db3ea4babbd/torch/foreach/__init__.py#L457)

Applies [`torch.floor()`](torch.floor.html#torch.floor) to each tensor in `inputs`.

This is semantically equivalent to applying [`torch.floor()`](torch.floor.html#torch.floor) independently
at every list position. Does not mutate its arguments and returns a tuple of result tensors.

Tensor-list arguments must be non-empty.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

Parameters:

**inputs** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to transform.

Returns:

a tuple containing one result tensor for each input tensor.