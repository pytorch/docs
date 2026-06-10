# torch.select

torch.select(*input*, *dim*, *index*) → [Tensor](../tensors.html#torch.Tensor)

Slices the `input` tensor along the selected dimension at the given index.
This function returns a view of the original tensor with the given dimension removed.

Note

If `input` is a sparse tensor and returning a view of
the tensor is not possible, a RuntimeError exception is
raised. In this is the case, consider using
[`torch.select_copy()`](torch.select_copy.html#torch.select_copy) function.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the dimension to slice
- **index** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the index to select with

Note

`select()` is equivalent to slicing. For example,
`tensor.select(0, index)` is equivalent to `tensor[index]` and
`tensor.select(2, index)` is equivalent to `tensor[:,:,index]`.