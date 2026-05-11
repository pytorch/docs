# torch.Tensor.storage_offset

Tensor.storage_offset() → [int](https://docs.python.org/3/library/functions.html#int)

Returns `self` tensor's offset in the underlying storage in terms of
number of storage elements (not bytes).

Example:

```
>>> x = torch.tensor([1, 2, 3, 4, 5])
>>> x.storage_offset()
0
>>> x[3:].storage_offset()
3
```