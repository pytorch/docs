# torch.Tensor.stride

Tensor.stride(*dim*) → tuple or int

Returns the stride of `self` tensor.

Stride is the jump necessary to go from one element to the next one in the
specified dimension [`dim`](torch.Tensor.dim.html#torch.Tensor.dim). A tuple of all strides is returned when no
argument is passed in. Otherwise, an integer value is returned as the stride in
the particular dimension [`dim`](torch.Tensor.dim.html#torch.Tensor.dim).

Parameters:

**dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the desired dimension in which stride is required

Example:

```
>>> x = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
>>> x.stride()
(5, 1)
>>> x.stride(0)
5
>>> x.stride(-1)
1
```