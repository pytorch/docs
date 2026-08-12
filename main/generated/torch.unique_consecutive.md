# torch.unique_consecutive

torch.unique_consecutive(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/_jit_internal.py#L627)

Eliminates all but the first element from every consecutive group of equivalent elements.

Note

This function is different from [`torch.unique()`](torch.unique.html#torch.unique) in the sense that this function
only eliminates consecutive duplicate values. This semantics is similar to std::unique
in C++.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor
- **return_inverse** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to also return the indices for where
elements in the original input ended up in the returned unique list.
- **return_counts** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to also return the counts for each unique
element.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the dimension to apply unique. If `None`, the unique of the
flattened input is returned. default: `None`

Returns:

A tensor or a tuple of tensors containing

> - **output** (*Tensor*): the output list of unique scalar elements.
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
>>> x = torch.tensor([1, 1, 2, 2, 3, 1, 1, 2])
>>> output = torch.unique_consecutive(x)
>>> output
tensor([1, 2, 3, 1, 2])

>>> output, inverse_indices = torch.unique_consecutive(x, return_inverse=True)
>>> output
tensor([1, 2, 3, 1, 2])
>>> inverse_indices
tensor([0, 0, 1, 1, 2, 3, 3, 4])

>>> output, counts = torch.unique_consecutive(x, return_counts=True)
>>> output
tensor([1, 2, 3, 1, 2])
>>> counts
tensor([2, 2, 1, 2, 1])
```