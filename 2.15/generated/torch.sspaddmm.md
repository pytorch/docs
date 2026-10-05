# torch.sspaddmm

torch.sspaddmm(*input*, *mat1*, *mat2*, ***, *beta=1*, *alpha=1*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Matrix multiplies a sparse tensor `mat1` with a dense tensor
`mat2`, then adds the sparse tensor `input` to the result.

Note: This function is equivalent to [`torch.addmm()`](torch.addmm.html#torch.addmm), except
`input` and `mat1` are sparse.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - a sparse matrix to be added
- **mat1** ([*Tensor*](../tensors.html#torch.Tensor)) - a sparse matrix to be matrix multiplied
- **mat2** ([*Tensor*](../tensors.html#torch.Tensor)) - a dense matrix to be matrix multiplied

Keyword Arguments:

- **beta** (*Number**,**optional*) - multiplier for `mat` (β\betaβ)
- **alpha** (*Number**,**optional*) - multiplier for mat1@mat2mat1 @ mat2mat1@mat2 (α\alphaα)
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.