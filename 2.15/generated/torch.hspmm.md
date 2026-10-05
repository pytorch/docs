# torch.hspmm

torch.hspmm(*mat1*, *mat2*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Performs a matrix multiplication of a [sparse COO matrix](../sparse.html#sparse-coo-docs) `mat1` and a strided matrix `mat2`. The
result is a (1 + 1)-dimensional [hybrid COO matrix](../sparse.html#sparse-hybrid-coo-docs).

Parameters:

- **mat1** ([*Tensor*](../tensors.html#torch.Tensor)) - the first sparse matrix to be matrix multiplied
- **mat2** ([*Tensor*](../tensors.html#torch.Tensor)) - the second strided matrix to be matrix multiplied

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.