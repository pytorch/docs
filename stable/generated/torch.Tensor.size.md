# torch.Tensor.size

Tensor.size(*dim=None*) → torch.Size or int

Returns the size of the `self` tensor. If `dim` is not specified,
the returned value is a [`torch.Size`](../size.html#torch.Size), a subclass of [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple).
If `dim` is specified, returns an int holding the size of that dimension.

Parameters:

**dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The dimension for which to retrieve the size.

Example:

```
>>> t = torch.empty(3, 4, 5)
>>> t.size()
torch.Size([3, 4, 5])
>>> t.size(dim=1)
4
```