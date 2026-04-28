# torch.tile

torch.tile(*input*, *dims*) → [Tensor](../tensors.html#torch.Tensor)

Constructs a tensor by repeating the elements of `input`.
The `dims` argument specifies the number of repetitions
in each dimension.

If `dims` specifies fewer dimensions than `input` has, then
ones are prepended to `dims` until all dimensions are specified.
For example, if `input` has shape (8, 6, 4, 2) and `dims`
is (2, 2), then `dims` is treated as (1, 1, 2, 2).

Analogously, if `input` has fewer dimensions than `dims`
specifies, then `input` is treated as if it were unsqueezed at
dimension zero until it has as many dimensions as `dims` specifies.
For example, if `input` has shape (4, 2) and `dims`
is (3, 3, 2, 2), then `input` is treated as if it had the
shape (1, 1, 4, 2).

Note

This function is similar to NumPy's tile function.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor whose elements to repeat.
- **dims** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - the number of repetitions per dimension.

Example:

```
>>> x = torch.tensor([1, 2, 3])
>>> x.tile((2,))
tensor([1, 2, 3, 1, 2, 3])
>>> y = torch.tensor([[1, 2], [3, 4]])
>>> torch.tile(y, (2, 2))
tensor([[1, 2, 1, 2],
 [3, 4, 3, 4],
 [1, 2, 1, 2],
 [3, 4, 3, 4]])
```