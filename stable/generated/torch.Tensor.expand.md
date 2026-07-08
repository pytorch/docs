# torch.Tensor.expand

Tensor.expand(**size*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new view of the `self` tensor with singleton dimensions expanded
to a larger size.

Passing -1 as the size for a dimension means not changing the size of
that dimension.

Tensor can be also expanded to a larger number of dimensions, and the
new ones will be appended at the front. For the new dimensions, the
size cannot be set to -1.

Expanding a tensor does not allocate new memory, but only creates a
new view on the existing tensor where a dimension of size one is
expanded to a larger size by setting the `stride` to 0. Any dimension
of size 1 can be expanded to an arbitrary value without allocating new
memory.

Note

Operations on an expanded view may still allocate memory if they need to
materialize the expanded values. For example, changing dtype after
`expand()` can allocate memory for the full expanded shape.

Parameters:

***size** ([*torch.Size*](../size.html#torch.Size)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*...*) - the desired expanded size

Warning

More than one element of an expanded tensor may refer to a single
memory location. As a result, in-place operations (especially ones that
are vectorized) may result in incorrect behavior. If you need to write
to the tensors, please clone them first.

Example:

```
>>> x = torch.tensor([[1], [2], [3]])
>>> x.size()
torch.Size([3, 1])
>>> x.expand(3, 4)
tensor([[ 1, 1, 1, 1],
 [ 2, 2, 2, 2],
 [ 3, 3, 3, 3]])
>>> x.expand(-1, 4) # -1 means not changing the size of that dimension
tensor([[ 1, 1, 1, 1],
 [ 2, 2, 2, 2],
 [ 3, 3, 3, 3]])
```