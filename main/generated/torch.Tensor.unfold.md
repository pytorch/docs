# torch.Tensor.unfold

Tensor.unfold(*dimension*, *size*, *step*) → [Tensor](../tensors.html#torch.Tensor)

Returns a view of the original tensor which contains all slices of size [`size`](torch.Tensor.size.html#torch.Tensor.size) from
`self` tensor in the dimension `dimension`.

Step between two slices is given by `step`.

If sizedim is the size of dimension `dimension` for `self`, the size of
dimension `dimension` in the returned tensor will be
(sizedim - size) / step + 1.

An additional dimension of size [`size`](torch.Tensor.size.html#torch.Tensor.size) is appended in the returned tensor.

Parameters:

- **dimension** ([*int*](https://docs.python.org/3/library/functions.html#int)) - dimension in which unfolding happens
- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the size of each slice that is unfolded
- **step** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the step between each slice

Example:

```
>>> x = torch.arange(1., 8)
>>> x
tensor([ 1., 2., 3., 4., 5., 6., 7.])
>>> x.unfold(0, 2, 1)
tensor([[ 1., 2.],
 [ 2., 3.],
 [ 3., 4.],
 [ 4., 5.],
 [ 5., 6.],
 [ 6., 7.]])
>>> x.unfold(0, 2, 2)
tensor([[ 1., 2.],
 [ 3., 4.],
 [ 5., 6.]])
```