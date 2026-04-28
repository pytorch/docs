# torch.mv

torch.mv(*input*, *vec*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Performs a matrix-vector product of the matrix `input` and the vector
`vec`.

If `input` is a (n×m)(n \times m)(n×m) tensor, `vec` is a 1-D tensor of
size mmm, `out` will be 1-D of size nnn.

Note

This function does not [broadcast](../notes/broadcasting.html#broadcasting-semantics).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - matrix to be multiplied
- **vec** ([*Tensor*](../tensors.html#torch.Tensor)) - vector to be multiplied

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> mat = torch.randn(2, 3)
>>> vec = torch.randn(3)
>>> torch.mv(mat, vec)
tensor([ 1.0404, -0.6361])
```