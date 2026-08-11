# torch.Tensor.put_

Tensor.put_(*index*, *source*, *accumulate=False*) → [Tensor](../tensors.html#torch.Tensor)

Copies the elements from `source` into the positions specified by
`index`. For the purpose of indexing, the `self` tensor is treated as if
it were a 1-D tensor.

`index` and `source` need to have the same number of elements, but not necessarily
the same shape.

If `accumulate` is `True`, the elements in `source` are added to
`self`. If accumulate is `False`, the behavior is undefined if `index`
contain duplicate elements.

Parameters:

- **index** (*LongTensor*) - the indices into self
- **source** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor containing values to copy from
- **accumulate** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether to accumulate into self. Default: `False`

Example:

```
>>> src = torch.tensor([[4, 3, 5],
... [6, 7, 8]])
>>> src.put_(torch.tensor([1, 3]), torch.tensor([9, 10]))
tensor([[ 4, 9, 5],
 [ 10, 7, 8]])
```