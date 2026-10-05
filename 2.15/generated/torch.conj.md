# torch.conj

torch.conj(*input*) → [Tensor](../tensors.html#torch.Tensor)

Returns a view of `input` with a flipped conjugate bit. If `input` has a non-complex dtype,
this function just returns `input`.

Note

`torch.conj()` performs a lazy conjugation, but the actual conjugated tensor can be materialized
at any time using [`torch.resolve_conj()`](torch.resolve_conj.html#torch.resolve_conj).

Warning

In the future, `torch.conj()` may return a non-writeable view for an `input` of
non-complex dtype. It's recommended that programs not modify the tensor returned by [`torch.conj_physical()`](torch.conj_physical.html#torch.conj_physical)
when `input` is of non-complex dtype to be compatible with this change.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Example:

```
>>> x = torch.tensor([-1 + 1j, -2 + 2j, 3 - 3j])
>>> x.is_conj()
False
>>> y = torch.conj(x)
>>> y.is_conj()
True
```