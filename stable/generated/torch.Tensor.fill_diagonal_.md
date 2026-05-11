# torch.Tensor.fill_diagonal_

Tensor.fill_diagonal_(*fill_value*, *wrap=False*) → [Tensor](../tensors.html#torch.Tensor)

Fill the main diagonal of a tensor that has at least 2-dimensions.
When dims>2, all dimensions of input must be of equal length.
This function modifies the input tensor in-place, and returns the input tensor.

Parameters:

- **fill_value** (*Scalar*) - the fill value
- **wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - the diagonal 'wrapped' after N columns for tall matrices. Default: `False`

Example:

```
>>> a = torch.zeros(3, 3)
>>> a.fill_diagonal_(5)
tensor([[5., 0., 0.],
 [0., 5., 0.],
 [0., 0., 5.]])
>>> b = torch.zeros(7, 3)
>>> b.fill_diagonal_(5)
tensor([[5., 0., 0.],
 [0., 5., 0.],
 [0., 0., 5.],
 [0., 0., 0.],
 [0., 0., 0.],
 [0., 0., 0.],
 [0., 0., 0.]])
>>> c = torch.zeros(7, 3)
>>> c.fill_diagonal_(5, wrap=True)
tensor([[5., 0., 0.],
 [0., 5., 0.],
 [0., 0., 5.],
 [0., 0., 0.],
 [5., 0., 0.],
 [0., 5., 0.],
 [0., 0., 5.]])
```