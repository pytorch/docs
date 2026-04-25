# torch.take_along_dim

torch.take_along_dim(*input*, *indices*, *dim=None*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Selects values from `input` at the 1-dimensional indices from `indices` along the given `dim`.

If `dim` is None, the input array is treated as if it has been flattened to 1d.

Functions that return indices along a dimension, like [`torch.argmax()`](torch.argmax.html#torch.argmax) and [`torch.argsort()`](torch.argsort.html#torch.argsort),
are designed to work with this function. See the examples below.

Note

This function is similar to NumPy's take_along_axis.
See also [`torch.gather()`](torch.gather.html#torch.gather).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **indices** (*LongTensor*) - the indices into `input`. Must have long dtype.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - dimension to select along. Default: None.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> t = torch.tensor([[10, 30, 20], [60, 40, 50]])
>>> max_idx = torch.argmax(t)
>>> torch.take_along_dim(t, max_idx)
tensor([60])
>>> sorted_idx = torch.argsort(t, dim=1)
>>> torch.take_along_dim(t, sorted_idx, dim=1)
tensor([[10, 20, 30],
 [40, 50, 60]])
```