# torch.foreach.log_

torch.foreach.log_(*inputs: TensorList*, */*) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...] | [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](../tensors.html#torch.Tensor)][[source]](https://github.com/pytorch/pytorch/blob/0c8b4a78ffbbce776adc0823e790158b26435f40/torch/foreach/__init__.py#L495)

Applies [`torch.log()`](torch.log.html#torch.log) to each tensor in `inputs` in-place.

This is semantically equivalent to applying [`torch.log()`](torch.log.html#torch.log) independently
at every list position. Mutates every tensor in `inputs` and returns the exact input container object.

Tensor-list arguments must be non-empty.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

Parameters:

**inputs** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to transform.

Returns:

the exact input list or tuple.