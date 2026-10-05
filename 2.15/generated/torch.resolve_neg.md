# torch.resolve_neg

torch.resolve_neg(*input*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with materialized negation if `input`'s negative bit is set to True,
else returns `input`. The output tensor will always have its negative bit set to False.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Example:

```
>>> x = torch.tensor([-1 + 1j, -2 + 2j, 3 - 3j])
>>> y = x.conj()
>>> z = y.imag
>>> z.is_neg()
True
>>> out = z.resolve_neg()
>>> out
tensor([-1., -2., 3.])
>>> out.is_neg()
False
```