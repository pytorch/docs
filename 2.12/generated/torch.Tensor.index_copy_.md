# torch.Tensor.index_copy_

Tensor.index_copy_(*dim*, *index*, *tensor*) → [Tensor](../tensors.html#torch.Tensor)

Copies the elements of [`tensor`](torch.tensor.html#torch.tensor) into the `self` tensor by selecting
the indices in the order given in `index`. For example, if `dim == 0`
and `index[i] == j`, then the `i`th row of [`tensor`](torch.tensor.html#torch.tensor) is copied to the
`j`th row of `self`.

The [`dim`](torch.Tensor.dim.html#torch.Tensor.dim)th dimension of [`tensor`](torch.tensor.html#torch.tensor) must have the same size as the
length of `index` (which must be a vector), and all other dimensions must
match `self`, or an error will be raised.

Note

If `index` contains duplicate entries, multiple elements from
[`tensor`](torch.tensor.html#torch.tensor) will be copied to the same index of `self`. The result
is nondeterministic since it depends on which copy occurs last.

Parameters:

- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - dimension along which to index
- **index** (*LongTensor*) - indices of [`tensor`](torch.tensor.html#torch.tensor) to select from
- **tensor** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor containing values to copy

Example:

```
>>> x = torch.zeros(5, 3)
>>> t = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
>>> index = torch.tensor([0, 4, 2])
>>> x.index_copy_(0, index, t)
tensor([[ 1., 2., 3.],
 [ 0., 0., 0.],
 [ 7., 8., 9.],
 [ 0., 0., 0.],
 [ 4., 5., 6.]])
```