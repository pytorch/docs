# torch.argwhere

torch.argwhere(*input*) → [Tensor](../tensors.html#torch.Tensor)

Returns a tensor containing the indices of all non-zero elements of
`input`. Each row in the result contains the indices of a non-zero
element in `input`. The result is sorted lexicographically, with
the last index changing the fastest (C-style).

If `input` has nnn dimensions, then the resulting indices tensor
`out` is of size (z×n)(z \times n)(z×n), where zzz is the total number of
non-zero elements in the `input` tensor.

Note

This function is similar to NumPy's argwhere.

When `input` is on CUDA, this function causes host-device synchronization.

Parameters:

**{input}** -

Example:

```
>>> t = torch.tensor([1, 0, 1])
>>> torch.argwhere(t)
tensor([[0],
 [2]])
>>> t = torch.tensor([[1, 0, 1], [0, 1, 1]])
>>> torch.argwhere(t)
tensor([[0, 0],
 [0, 2],
 [1, 1],
 [1, 2]])
```