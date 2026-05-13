# torch.isinf

torch.isinf(*input*) → [Tensor](../tensors.html#torch.Tensor)

Tests if each element of `input` is infinite
(positive or negative infinity) or not.

Note

Complex values are infinite when their real or imaginary part is
infinite.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Returns:

A boolean tensor that is True where `input` is infinite and False elsewhere

Example:

```
>>> torch.isinf(torch.tensor([1, float('inf'), 2, float('-inf'), float('nan')]))
tensor([False, True, False, True, False])
```