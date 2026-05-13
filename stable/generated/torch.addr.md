# torch.addr

torch.addr(*input*, *vec1*, *vec2*, ***, *beta=1*, *alpha=1*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Performs the outer-product of vectors `vec1` and `vec2`
and adds it to the matrix `input`.

Optional values `beta` and `alpha` are scaling factors on the
outer product between `vec1` and `vec2` and the added matrix
`input` respectively.

out=β input+α (vec1⊗vec2)\text{out} = \beta\ \text{input} + \alpha\ (\text{vec1} \otimes \text{vec2})

out=β input+α (vec1⊗vec2)

If `beta` is 0, then the content of `input` will be ignored, and nan and inf in
it will not be propagated.

If `vec1` is a vector of size n and `vec2` is a vector
of size m, then `input` must be
[broadcastable](../notes/broadcasting.html#broadcasting-semantics) with a matrix of size
(n×m)(n \times m)(n×m) and `out` will be a matrix of size
(n×m)(n \times m)(n×m).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - matrix to be added
- **vec1** ([*Tensor*](../tensors.html#torch.Tensor)) - the first vector of the outer product
- **vec2** ([*Tensor*](../tensors.html#torch.Tensor)) - the second vector of the outer product

Keyword Arguments:

- **beta** (*Number**,**optional*) - multiplier for `input` (β\betaβ)
- **alpha** (*Number**,**optional*) - multiplier for vec1⊗vec2\text{vec1} \otimes \text{vec2}vec1⊗vec2 (α\alphaα)
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> vec1 = torch.arange(1., 4.)
>>> vec2 = torch.arange(1., 3.)
>>> M = torch.zeros(3, 2)
>>> torch.addr(M, vec1, vec2)
tensor([[ 1., 2.],
 [ 2., 4.],
 [ 3., 6.]])
```