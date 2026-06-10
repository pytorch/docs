# torch.outer

torch.outer(*input*, *vec2*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Outer product of `input` and `vec2`.
If `input` is a vector of size nnn and `vec2` is a vector of
size mmm, then `out` must be a matrix of size (n×m)(n \times m)(n×m).

Note

This function does not [broadcast](../notes/broadcasting.html#broadcasting-semantics).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - 1-D input vector
- **vec2** ([*Tensor*](../tensors.html#torch.Tensor)) - 1-D input vector

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - optional output matrix

Example:

```
>>> v1 = torch.arange(1., 5.)
>>> v2 = torch.arange(1., 4.)
>>> torch.outer(v1, v2)
tensor([[ 1., 2., 3.],
 [ 2., 4., 6.],
 [ 3., 6., 9.],
 [ 4., 8., 12.]])
```