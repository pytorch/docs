# torch.Tensor.tolist

Tensor.tolist() → list or number

Returns the tensor as a (nested) list. For scalars, a standard
Python number is returned, just like with [`item()`](torch.Tensor.item.html#torch.Tensor.item).
Tensors are automatically moved to the CPU first if necessary.

This operation is not differentiable.

Examples:

```
>>> a = torch.randn(2, 2)
>>> a.tolist()
[[0.012766935862600803, 0.5415473580360413],
 [-0.08909505605697632, 0.7729271650314331]]
>>> a[0,0].tolist()
0.012766935862600803
```