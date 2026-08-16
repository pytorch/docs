# torch.unravel_index

torch.unravel_index(*indices*, *shape*)[[source]](https://github.com/pytorch/pytorch/blob/8aac66fb022576e2d13144ab636372f686f23cfa/torch/functional.py#L1957)

Converts a tensor of flat indices into a tuple of coordinate tensors that
index into an arbitrary tensor of the specified shape.

Parameters:

- **indices** ([*Tensor*](../tensors.html#torch.Tensor)) - An integer tensor containing indices into the
flattened version of an arbitrary tensor of shape `shape`.
All elements must be in the range `[0, prod(shape) - 1]`.
- **shape** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**sequence**of**ints**, or*[*torch.Size*](../size.html#torch.Size)) - The shape of the arbitrary
tensor. All elements must be non-negative.

Returns:

Each `i`-th tensor in the output corresponds with
dimension `i` of `shape`. Each tensor has the same shape as
`indices` and contains one index into dimension `i` for each of the
flat indices given by `indices`.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple) of Tensors

Example:

```
>>> import torch
>>> torch.unravel_index(torch.tensor(4), (3, 2))
(tensor(2),
 tensor(0))

>>> torch.unravel_index(torch.tensor([4, 1]), (3, 2))
(tensor([2, 0]),
 tensor([0, 1]))

>>> torch.unravel_index(torch.tensor([0, 1, 2, 3, 4, 5]), (3, 2))
(tensor([0, 0, 1, 1, 2, 2]),
 tensor([0, 1, 0, 1, 0, 1]))

>>> torch.unravel_index(torch.tensor([1234, 5678]), (10, 10, 10, 10))
(tensor([1, 5]),
 tensor([2, 6]),
 tensor([3, 7]),
 tensor([4, 8]))

>>> torch.unravel_index(torch.tensor([[1234], [5678]]), (10, 10, 10, 10))
(tensor([[1], [5]]),
 tensor([[2], [6]]),
 tensor([[3], [7]]),
 tensor([[4], [8]]))

>>> torch.unravel_index(torch.tensor([[1234], [5678]]), (100, 100))
(tensor([[12], [56]]),
 tensor([[34], [78]]))
```