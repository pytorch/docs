# torch.isnan

torch.isnan(*input*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with boolean elements representing if each element of `input`
is NaN or not. Complex values are considered NaN when either their real
and/or imaginary part is NaN.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Returns:

A boolean tensor that is True where `input` is NaN and False elsewhere

Example:

```
>>> torch.isnan(torch.tensor([1, float('nan'), 2]))
tensor([False, True, False])
```