# torch.Tensor.shape

Tensor.shape

Returns the size of the `self` tensor. Alias for [`size`](torch.Tensor.size.html#torch.Tensor.size).

See also [`Tensor.size()`](torch.Tensor.size.html#torch.Tensor.size).

Example:

```
>>> t = torch.empty(3, 4, 5)
>>> t.size()
torch.Size([3, 4, 5])
>>> t.shape
torch.Size([3, 4, 5])
```