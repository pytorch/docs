# torch.vdot

torch.vdot(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the dot product of two 1D vectors along a dimension.

In symbols, this function computes

∑i=1nxi‾yi.\sum_{i=1}^n \overline{x_i}y_i.i=1∑n​xi​​yi​.

where xi‾\overline{x_i}xi​​ denotes the conjugate for complex
vectors, and it is the identity for real vectors.

Note

Unlike NumPy's vdot, torch.vdot intentionally only supports computing the dot product
of two 1D tensors with the same number of elements.

See also

[`torch.linalg.vecdot()`](torch.linalg.vecdot.html#torch.linalg.vecdot) computes the dot product of two batches of vectors along a dimension.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - first tensor in the dot product, must be 1D. Its conjugate is used if it's complex.
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - second tensor in the dot product, must be 1D.

Keyword args:

Note

out (Tensor, optional): the output tensor.

Example:

```
>>> torch.vdot(torch.tensor([2, 3]), torch.tensor([2, 1]))
tensor(7)
>>> a = torch.tensor((1 +2j, 3 - 1j))
>>> b = torch.tensor((2 +1j, 4 - 0j))
>>> torch.vdot(a, b)
tensor([16.+1.j])
>>> torch.vdot(b, a)
tensor([16.-1.j])
```