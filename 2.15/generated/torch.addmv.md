# torch.addmv

torch.addmv(*input*, *mat*, *vec*, ***, *beta=1*, *alpha=1*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Performs a matrix-vector product of the matrix `mat` and
the vector `vec`.
The vector `input` is added to the final result.

If `mat` is a (n×m)(n \times m)(n×m) tensor, `vec` is a 1-D tensor of
size m, then `input` must be
[broadcastable](../notes/broadcasting.html#broadcasting-semantics) with a 1-D tensor of size n and
`out` will be 1-D tensor of size n.

`alpha` and `beta` are scaling factors on matrix-vector product between
`mat` and `vec` and the added tensor `input` respectively.

out=β input+α (mat@vec)\text{out} = \beta\ \text{input} + \alpha\ (\text{mat} \mathbin{@} \text{vec})

out=β input+α (mat@vec)

If `beta` is 0, then the content of `input` will be ignored, and nan and inf in
it will not be propagated.

For inputs of type FloatTensor or DoubleTensor, arguments `beta` and
`alpha` must be real numbers, otherwise they should be integers.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - vector to be added
- **mat** ([*Tensor*](../tensors.html#torch.Tensor)) - matrix to be matrix multiplied
- **vec** ([*Tensor*](../tensors.html#torch.Tensor)) - vector to be matrix multiplied

Keyword Arguments:

- **beta** (*Number**,**optional*) - multiplier for `input` (β\betaβ)
- **alpha** (*Number**,**optional*) - multiplier for mat@vecmat @ vecmat@vec (α\alphaα)
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> M = torch.randn(2)
>>> mat = torch.randn(2, 3)
>>> vec = torch.randn(3)
>>> torch.addmv(M, mat, vec)
tensor([-0.3768, -5.5565])
```