# torch.as_strided

torch.as_strided(*input*, *size*, *stride*, *storage_offset=None*) → [Tensor](../tensors.html#torch.Tensor)

Create a view of an existing torch.Tensor `input` with specified
`size`, `stride` and `storage_offset`.

Warning

Prefer using other view functions, like [`torch.Tensor.view()`](torch.Tensor.view.html#torch.Tensor.view) or
[`torch.Tensor.expand()`](torch.Tensor.expand.html#torch.Tensor.expand), to setting a view's strides manually with
as_strided, as this function will throw an error on non-standard Pytorch
backends (that do not have a concept of stride) and the result will depend
on the current layout in memory. The constructed view must only refer to
elements within the Tensor's storage or a runtime error will be thrown.
If the generated view is "overlapped" (with multiple indices referring to
the same element in memory), the behavior of inplace operations on this view
is undefined (and might not throw runtime errors).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **size** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*or**ints*) - the shape of the output tensor
- **stride** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*or**ints*) - the stride of the output tensor
- **storage_offset** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the offset in the underlying storage of the output tensor.
If `None`, the storage_offset of the output tensor will match the input tensor.

Example:

```
>>> x = torch.randn(3, 3)
>>> x
tensor([[ 0.9039, 0.6291, 1.0795],
 [ 0.1586, 2.1939, -0.4900],
 [-0.1909, -0.7503, 1.9355]])
>>> t = torch.as_strided(x, (2, 2), (1, 2))
>>> t
tensor([[0.9039, 1.0795],
 [0.6291, 0.1586]])
>>> t = torch.as_strided(x, (2, 2), (1, 2), 1)
tensor([[0.6291, 0.1586],
 [1.0795, 2.1939]])
```