# torch.Tensor.dim_order

Tensor.dim_order(*ambiguity_check=False*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[source]](https://github.com/pytorch/pytorch/blob/051c786d044a8aa490884192d549c8057aa4d2e7/torch/_tensor.py#L1381)

Returns the uniquely determined tuple of int describing the dim order or
physical layout of `self`.

The dim order represents how dimensions are laid out in memory of dense tensors,
starting from the outermost to the innermost dimension.

Note that the dim order may not always be uniquely determined.
If ambiguity_check is True, this function raises a RuntimeError when the dim order cannot be uniquely determined;
If ambiguity_check is a list of memory formats, this function raises a RuntimeError when tensor can not be interpreted
into exactly one of the given memory formats, or it cannot be uniquely determined.
If ambiguity_check is False, it will return one of legal dim order(s) without checking its uniqueness.
Otherwise, it will raise TypeError.

Parameters:

**ambiguity_check** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*or**List**[*[*torch.memory_format*](../tensor_attributes.html#torch.memory_format)*]*) - The check method for ambiguity of dim order.

Examples:

```
>>> torch.empty((2, 3, 5, 7)).dim_order()
(0, 1, 2, 3)
>>> torch.empty((2, 3, 5, 7)).transpose(1, 2).dim_order()
(0, 2, 1, 3)
>>> torch.empty((2, 3, 5, 7), memory_format=torch.channels_last).dim_order()
(0, 2, 3, 1)
>>> torch.empty((1, 2, 3, 4)).dim_order()
(0, 1, 2, 3)
>>> try:
... torch.empty((1, 2, 3, 4)).dim_order(ambiguity_check=True)
... except RuntimeError as e:
... print(e)
The tensor does not have unique dim order, or cannot map to exact one of the given memory formats.
>>> torch.empty((1, 2, 3, 4)).dim_order(
... ambiguity_check=[torch.contiguous_format, torch.channels_last]
... ) # It can be mapped to contiguous format
(0, 1, 2, 3)
>>> try:
... torch.empty((1, 2, 3, 4)).dim_order(ambiguity_check="ILLEGAL") # type: ignore[arg-type]
... except TypeError as e:
... print(e)
The ambiguity_check argument must be a bool or a list of memory formats.
```

Warning

The dim_order tensor API is experimental and subject to change.