# torch.unflatten

torch.unflatten(*input*, *dim*, *sizes*) → [Tensor](../tensors.html#torch.Tensor)

Expands a dimension of the input tensor over multiple dimensions.

See also

[`torch.flatten()`](torch.flatten.html#torch.flatten) the inverse of this function. It coalesces several dimensions into one.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Dimension to be unflattened, specified as an index into
`input.shape`.
- **sizes** (*Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - New shape of the unflattened dimension.
One of its elements can be -1 in which case the corresponding output
dimension is inferred. Otherwise, the product of `sizes` *must*
equal `input.shape[dim]`.

Returns:

A View of input with the specified dimension unflattened.

Examples::

```
>>> torch.unflatten(torch.randn(3, 4, 1), 1, (2, 2)).shape
torch.Size([3, 2, 2, 1])
>>> torch.unflatten(torch.randn(3, 4, 1), 1, (-1, 2)).shape
torch.Size([3, 2, 2, 1])
>>> torch.unflatten(torch.randn(5, 12, 3), -2, (2, 2, 3, 1, 1)).shape
torch.Size([5, 2, 2, 3, 1, 1, 3])
```