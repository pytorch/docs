# torch.Tensor.item

Tensor.item() → number

Returns the value of this tensor as a standard Python number. This only works
for tensors with one element. For other cases, see [`tolist()`](torch.Tensor.tolist.html#torch.Tensor.tolist).

This operation is not differentiable.

Example:

```
>>> x = torch.tensor([1.0])
>>> x.item()
1.0
```