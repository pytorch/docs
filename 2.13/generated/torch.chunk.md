# torch.chunk

torch.chunk(*input: [Tensor](../tensors.html#torch.Tensor)*, *chunks: [int](https://docs.python.org/3/library/functions.html#int)*, *dim: [int](https://docs.python.org/3/library/functions.html#int) = 0*) → Tuple[[Tensor](../tensors.html#torch.Tensor), ...]

Attempts to split a tensor into the specified number of chunks. Each chunk is a view of
the input tensor.

Note

This function may return fewer than the specified number of chunks!

See also

[`torch.tensor_split()`](torch.tensor_split.html#torch.tensor_split) a function that always returns exactly the specified number of chunks

If the tensor size along the given dimension `dim` is divisible by `chunks`,
all returned chunks will be the same size.
If the tensor size along the given dimension `dim` is not divisible by `chunks`,
all returned chunks will be the same size, except the last one.
If such division is not possible, this function may return fewer
than the specified number of chunks.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor to split
- **chunks** ([*int*](https://docs.python.org/3/library/functions.html#int)) - number of chunks to return
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - dimension along which to split the tensor

Example

```
>>> torch.arange(11).chunk(6)
(tensor([0, 1]),
 tensor([2, 3]),
 tensor([4, 5]),
 tensor([6, 7]),
 tensor([8, 9]),
 tensor([10]))
>>> torch.arange(12).chunk(6)
(tensor([0, 1]),
 tensor([2, 3]),
 tensor([4, 5]),
 tensor([6, 7]),
 tensor([8, 9]),
 tensor([10, 11]))
>>> torch.arange(13).chunk(6)
(tensor([0, 1, 2]),
 tensor([3, 4, 5]),
 tensor([6, 7, 8]),
 tensor([ 9, 10, 11]),
 tensor([12]))
```