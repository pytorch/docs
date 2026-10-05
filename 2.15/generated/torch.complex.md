# torch.complex

torch.complex(*real*, *imag*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Constructs a complex tensor with its real part equal to [`real`](torch.real.html#torch.real) and its
imaginary part equal to [`imag`](torch.imag.html#torch.imag).

Parameters:

- **real** ([*Tensor*](../tensors.html#torch.Tensor)) - The real part of the complex tensor. Must be half, float or double.
- **imag** ([*Tensor*](../tensors.html#torch.Tensor)) - The imaginary part of the complex tensor. Must be same dtype
as [`real`](torch.real.html#torch.real).

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)) - If the inputs are `torch.float32`, must be
`torch.complex64`. If the inputs are `torch.float64`, must be
`torch.complex128`.

Example:

```
>>> real = torch.tensor([1, 2], dtype=torch.float32)
>>> imag = torch.tensor([3, 4], dtype=torch.float32)
>>> z = torch.complex(real, imag)
>>> z
tensor([(1.+3.j), (2.+4.j)])
>>> z.dtype
torch.complex64
```