# torch.foreach.clone

torch.foreach.clone(*inputs: TensorList*, */*, ***, *memory_format: [memory_format](../tensor_attributes.html#torch.memory_format) | [None](https://docs.python.org/3/library/constants.html#None) = None*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...][[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/foreach/__init__.py#L1534)

Clones every tensor in `inputs`.

This is semantically equivalent to applying [`torch.clone()`](torch.clone.html#torch.clone) independently
at every list position. Does not mutate its arguments and returns a tuple of result tensors.

Tensor-list arguments must be non-empty.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

Parameters:

- **inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to clone.
- **memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - desired memory
format. If `None`, the input memory format is preserved. Default: `None`.

Returns:

a tuple containing the cloned tensors.