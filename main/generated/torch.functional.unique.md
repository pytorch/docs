# torch.functional.unique

torch.functional.unique(*input*, *sorted=True*, *return_inverse=False*, *return_counts=False*, *dim=None*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), [Tensor](../tensors.html#torch.Tensor), [Tensor](../tensors.html#torch.Tensor)][[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/_jit_internal.py#L627)

Returns the unique elements of the input tensor.

Note

This function is different from [`torch.unique_consecutive()`](torch.unique_consecutive.html#torch.unique_consecutive) in the sense that
this function also eliminates non-consecutive duplicate values.

Note

Currently in the CUDA implementation and the CPU implementation,
torch.unique always sort the tensor at the beginning regardless of the sort argument.
Sorting could be slow, so if your input tensor is already sorted, it is recommended to use
[`torch.unique_consecutive()`](torch.unique_consecutive.html#torch.unique_consecutive) which avoids the sorting.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor
- **sorted** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to sort the unique elements in ascending order
before returning as output.
- **return_inverse** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to also return the indices for where
elements in the original input ended up in the returned unique list.
- **return_counts** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to also return the counts for each unique
element.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the dimension to operate upon. If `None`, the
unique of the flattened input is returned. Otherwise, each of the
tensors indexed by the given dimension is treated as one of the
elements to apply the unique operation upon. **Important:** when `dim`
is specified, the operation finds unique sub-tensors (e.g., unique rows
or columns), not unique scalar values. This means individual values may
appear multiple times in the output if they exist in different sub-tensors.
See examples for more details. Default: `None`

Returns:

A tensor or a tuple of tensors containing

> - **output** (*Tensor*): the output list of unique scalar elements if `dim`
> is `None`; otherwise, the unique sub-tensors along the specified dimension.
> Note that when `dim` is specified, scalar values may repeat in the output.
> - **inverse_indices** (*Tensor*): (optional) if
> `return_inverse` is True, there will be an additional
> returned tensor (same shape as input) representing the indices
> for where elements in the original input map to in the output;
> otherwise, this function will only return a single tensor.
> - **counts** (*Tensor*): (optional) if
> `return_counts` is True, there will be an additional
> returned tensor (same shape as output or output.size(dim),
> if dim was specified) representing the number of occurrences
> for each unique value or tensor.

Return type:

([Tensor](../tensors.html#torch.Tensor), [Tensor](../tensors.html#torch.Tensor) (optional), [Tensor](../tensors.html#torch.Tensor) (optional))

Example:

```
>>> output = torch.unique(torch.tensor([1, 3, 2, 3], dtype=torch.long))
>>> output
tensor([1, 2, 3])

>>> output, inverse_indices = torch.unique(
... torch.tensor([1, 3, 2, 3], dtype=torch.long), sorted=True, return_inverse=True)
>>> output
tensor([1, 2, 3])
>>> inverse_indices
tensor([0, 2, 1, 2])

>>> output, inverse_indices = torch.unique(
... torch.tensor([[1, 3], [2, 3]], dtype=torch.long), sorted=True, return_inverse=True)
>>> output
tensor([1, 2, 3])
>>> inverse_indices
tensor([[0, 2],
 [1, 2]])

>>> # When using dim, the operation finds unique sub-tensors, not unique values.
>>> # Notice how values can repeat in the output:
>>> x = torch.tensor([[1, 3, 2, 3], [1, 2, 1, 2]], dtype=torch.long)
>>> torch.unique(x, dim=0) # unique rows
tensor([[1, 2, 1, 2],
 [1, 3, 2, 3]])
>>> # Both rows are kept because they're different from each other,
>>> # even though values 1, 2, 3 appear multiple times in the output.
>>> torch.unique(x, dim=1) # unique columns
tensor([[1, 2, 3],
 [1, 1, 2]])
>>> # The value 1 appears twice because we're comparing columns, not values.
>>> # Compare with flattened (no dim):
>>> torch.unique(x)
tensor([1, 2, 3])

>>> a = torch.tensor([
... [
... [1, 1, 0, 0],
... [1, 1, 0, 0],
... [0, 0, 1, 1],
... ],
... [
... [0, 0, 1, 1],
... [0, 0, 1, 1],
... [1, 1, 1, 1],
... ],
... [
... [1, 1, 0, 0],
... [1, 1, 0, 0],
... [0, 0, 1, 1],
... ],
... ])

>>> # If we call `torch.unique(a, dim=0)`, each of the tensors `a[idx, :, :]`
>>> # will be compared. We can see that `a[0, :, :]` and `a[2, :, :]` match
>>> # each other, so one of them will be removed.
>>> (a[0, :, :] == a[2, :, :]).all()
tensor(True)
>>> a_unique_dim0 = torch.unique(a, dim=0)
>>> a_unique_dim0
tensor([[[0, 0, 1, 1],
 [0, 0, 1, 1],
 [1, 1, 1, 1]],
 [[1, 1, 0, 0],
 [1, 1, 0, 0],
 [0, 0, 1, 1]]])

>>> # Notice which sub-tensors from `a` match with the sub-tensors from
>>> # `a_unique_dim0`:
>>> (a_unique_dim0[0, :, :] == a[1, :, :]).all()
tensor(True)
>>> (a_unique_dim0[1, :, :] == a[0, :, :]).all()
tensor(True)

>>> # For `torch.unique(a, dim=1)`, each of the tensors `a[:, idx, :]` are
>>> # compared. `a[:, 0, :]` and `a[:, 1, :]` match each other, so one of
>>> # them will be removed.
>>> (a[:, 0, :] == a[:, 1, :]).all()
tensor(True)
>>> torch.unique(a, dim=1)
tensor([[[0, 0, 1, 1],
 [1, 1, 0, 0]],
 [[1, 1, 1, 1],
 [0, 0, 1, 1]],
 [[0, 0, 1, 1],
 [1, 1, 0, 0]]])

>>> # For `torch.unique(a, dim=2)`, the tensors `a[:, :, idx]` are compared.
>>> # `a[:, :, 0]` and `a[:, :, 1]` match each other. Also, `a[:, :, 2]` and
>>> # `a[:, :, 3]` match each other as well. So in this case, two of the
>>> # sub-tensors will be removed.
>>> (a[:, :, 0] == a[:, :, 1]).all()
tensor(True)
>>> (a[:, :, 2] == a[:, :, 3]).all()
tensor(True)
>>> torch.unique(a, dim=2)
tensor([[[0, 1],
 [0, 1],
 [1, 0]],
 [[1, 0],
 [1, 0],
 [1, 1]],
 [[0, 1],
 [0, 1],
 [1, 0]]])
```