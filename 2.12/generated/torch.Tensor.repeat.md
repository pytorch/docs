# torch.Tensor.repeat

Tensor.repeat(**repeats*) → [Tensor](../tensors.html#torch.Tensor)

Repeats this tensor along the specified dimensions.

Unlike [`expand()`](torch.Tensor.expand.html#torch.Tensor.expand), this function copies the tensor's data.

Warning

`repeat()` behaves differently from
[numpy.repeat](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html),
but is more similar to
[numpy.tile](https://numpy.org/doc/stable/reference/generated/numpy.tile.html).
For the operator similar to numpy.repeat, see [`torch.repeat_interleave()`](torch.repeat_interleave.html#torch.repeat_interleave).

Parameters:

**repeat** ([*torch.Size*](../size.html#torch.Size)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*...**,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*of*[*int*](https://docs.python.org/3/library/functions.html#int)) - The number of times to repeat this tensor along each dimension

Example:

```
>>> x = torch.tensor([1, 2, 3])
>>> x.repeat(4, 2)
tensor([[ 1, 2, 3, 1, 2, 3],
 [ 1, 2, 3, 1, 2, 3],
 [ 1, 2, 3, 1, 2, 3],
 [ 1, 2, 3, 1, 2, 3]])
>>> x.repeat(4, 2, 1).size()
torch.Size([4, 2, 3])
```