# torch.foreach.mm

torch.foreach.mm(*inputs: TensorList*, *mat2: TensorList*, */*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), ...][[source]](https://github.com/pytorch/pytorch/blob/c9fded8194d3b089ed610b586eb746a6e74c6616/torch/foreach/__init__.py#L1656)

Multiplies corresponding matrices from `inputs` and `mat2` using
[`torch.mm()`](torch.mm.html#torch.mm). This is semantically equivalent to applying
[`torch.mm()`](torch.mm.html#torch.mm) independently at every list position. It does not mutate its
arguments and returns a tuple of result tensors.

On supported CUDA inputs, an accelerated grouped matrix multiplication
implementation may be used. Other inputs fall back to per-position execution.

Both tensor-list arguments must be non-empty and have the same length.
There is no in-place `torch.foreach.mm_` operation.

Parameters:

- **inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - first matrices.
- **mat2** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*Tensor*](../tensors.html#torch.Tensor)) - second matrices.

Returns:

a tuple containing one matrix product per list position.