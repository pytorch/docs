# torch.repeat_interleave

torch.repeat_interleave(*input*, *repeats*, *dim=None*, ***, *output_size=None*) → [Tensor](../tensors.html#torch.Tensor)

Repeat elements of a tensor.

Warning

This is different from [`torch.Tensor.repeat()`](torch.Tensor.repeat.html#torch.Tensor.repeat) but similar to `numpy.repeat`.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **repeats** ([*Tensor*](../tensors.html#torch.Tensor)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - The number of repetitions for each element.
repeats is broadcasted to fit the shape of the given axis.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The dimension along which to repeat values.
By default, use the flattened input array, and return a flat output
array.

Keyword Arguments:

**output_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Total output size for the given axis
( e.g. sum of repeats). If given, it will avoid stream synchronization
needed to calculate output shape of the tensor.

Returns:

Repeated tensor which has the same shape as input, except along the given axis.

Return type:

[Tensor](../tensors.html#torch.Tensor)

Example:

```
>>> x = torch.tensor([1, 2, 3])
>>> x.repeat_interleave(2)
tensor([1, 1, 2, 2, 3, 3])
>>> y = torch.tensor([[1, 2], [3, 4]])
>>> torch.repeat_interleave(y, 2)
tensor([1, 1, 2, 2, 3, 3, 4, 4])
>>> torch.repeat_interleave(y, 3, dim=1)
tensor([[1, 1, 1, 2, 2, 2],
 [3, 3, 3, 4, 4, 4]])
>>> torch.repeat_interleave(y, torch.tensor([1, 2]), dim=0)
tensor([[1, 2],
 [3, 4],
 [3, 4]])
>>> torch.repeat_interleave(y, torch.tensor([1, 2]), dim=0, output_size=3)
tensor([[1, 2],
 [3, 4],
 [3, 4]])
```

If the repeats is tensor([n1, n2, n3, ...]), then the output will be
tensor([0, 0, ..., 1, 1, ..., 2, 2, ..., ...]) where 0 appears n1 times,
1 appears n2 times, 2 appears n3 times, etc.

torch.repeat_interleave(*repeats*, ***) → [Tensor](../tensors.html#torch.Tensor)

Repeats 0 repeats[0] times, 1 repeats[1] times, 2 repeats[2] times, etc.

Parameters:

**repeats** ([*Tensor*](../tensors.html#torch.Tensor)) - The number of repetitions for each element.

Returns:

Repeated tensor of size sum(repeats).

Return type:

[Tensor](../tensors.html#torch.Tensor)

Example:

```
>>> torch.repeat_interleave(torch.tensor([1, 2, 3]))
tensor([0, 1, 1, 2, 2, 2])
```