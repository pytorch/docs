# torch.isin

torch.isin(*elements*, *test_elements*, ***, *assume_unique=False*, *invert=False*) → [Tensor](../tensors.html#torch.Tensor)

Tests if each element of `elements` is in `test_elements`. Returns
a boolean tensor of the same shape as `elements` that is True for elements
in `test_elements` and False otherwise.

Note

One of `elements` or `test_elements` can be a scalar, but not both.

Parameters:

- **elements** ([*Tensor*](../tensors.html#torch.Tensor)*or**Scalar*) - Input elements
- **test_elements** ([*Tensor*](../tensors.html#torch.Tensor)*or**Scalar*) - Values against which to test for each input element
- **assume_unique** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If True, assumes both `elements` and
`test_elements` contain unique elements, which can speed up the
calculation. Default: False
- **invert** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If True, inverts the boolean return tensor, resulting in True
values for elements *not* in `test_elements`. Default: False

Returns:

A boolean tensor of the same shape as `elements` that is True for elements in
`test_elements` and False otherwise

Example

```
>>> torch.isin(torch.tensor([[1, 2], [3, 4]]), torch.tensor([2, 3]))
tensor([[False, True],
 [ True, False]])
```