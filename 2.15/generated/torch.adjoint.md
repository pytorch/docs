# torch.adjoint

torch.adjoint(*input: [Tensor](../tensors.html#torch.Tensor)*) → [Tensor](../tensors.html#torch.Tensor)

Returns a view of the tensor conjugated and with the last two dimensions transposed.

`x.adjoint()` is equivalent to `x.transpose(-2, -1).conj()` for complex tensors and
to `x.transpose(-2, -1)` for real tensors.

Parameters:

**{input}** -

Example:

```
>>> x = torch.arange(4, dtype=torch.float)
>>> A = torch.complex(x, x).reshape(2, 2)
>>> A
tensor([[0.+0.j, 1.+1.j],
 [2.+2.j, 3.+3.j]])
>>> A.adjoint()
tensor([[0.-0.j, 2.-2.j],
 [1.-1.j, 3.-3.j]])
>>> (A.adjoint() == A.mH).all()
tensor(True)
```