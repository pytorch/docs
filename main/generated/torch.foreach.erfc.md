# torch.foreach.erfc

torch.foreach.erfc(*inputs: TensorList*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...][[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/foreach/__init__.py#L424)

Applies [`torch.erfc()`](torch.erfc.html#torch.erfc) to each tensor in `inputs`.

This is semantically equivalent to applying [`torch.erfc()`](torch.erfc.html#torch.erfc) independently
at every list position. Does not mutate its arguments and returns a tuple of result tensors.

Tensor-list arguments must be non-empty.
An accelerated multi-tensor implementation is used only when supported by the
inputs; otherwise the operation falls back to per-tensor execution.

Parameters:

**inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - tensors to transform.

Returns:

a tuple containing one result tensor for each input tensor.