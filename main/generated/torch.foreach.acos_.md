# torch.foreach.acos_

torch.foreach.acos_(*inputs: TensorList*, */*) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)][[source]](https://github.com/pytorch/pytorch/blob/8d6343a7cd80821d54ba546bc6f799aad9ccb79c/torch/foreach/__init__.py#L352)

Applies [`torch.acos()`](torch.acos.html#torch.acos) to each tensor in `inputs` in-place.

This is semantically equivalent to applying [`torch.acos()`](torch.acos.html#torch.acos) independently
at every list position. Mutates every tensor in `inputs` and returns the exact input container object.

Tensor-list arguments must be non-empty.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

Parameters:

**inputs** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to transform.

Returns:

the exact input list or tuple.