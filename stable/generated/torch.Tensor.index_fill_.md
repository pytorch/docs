# torch.Tensor.index_fill_

Tensor.index_fill_(*dim*, *index*, *value*) → [Tensor](../tensors.html#torch.Tensor)

Fills the elements of the `self` tensor with value `value` by
selecting the indices in the order given in `index`.

Parameters:

- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - dimension along which to index
- **index** (*LongTensor*) - indices of `self` tensor to fill in
- **value** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the value to fill with

Example:

```
>>> x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
>>> index = torch.tensor([0, 2])
>>> x.index_fill_(1, index, -1)
tensor([[-1., 2., -1.],
 [-1., 5., -1.],
 [-1., 8., -1.]])
```