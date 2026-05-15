# torch.sparse.sampled_addmm

torch.sparse.sampled_addmm(*input*, *mat1*, *mat2*, ***, *beta=1.*, *alpha=1.*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/sparse/__init__.py#L162)

Performs a matrix multiplication of the dense matrices `mat1` and `mat2` at the locations
specified by the sparsity pattern of `input`. The matrix `input` is added to the final result.

Mathematically this performs the following operation:

out=α (mat1@mat2)∗spy(input)+β input\text{out} = \alpha\ (\text{mat1} \mathbin{@} \text{mat2})*\text{spy}(\text{input}) + \beta\ \text{input}out=α (mat1@mat2)∗spy(input)+β input

where spy(input)\text{spy}(\text{input})spy(input) is the sparsity pattern matrix of `input`, `alpha`
and `beta` are the scaling factors.
spy(input)\text{spy}(\text{input})spy(input) has value 1 at the positions where `input` has non-zero values, and 0 elsewhere.

Note

`input` must be a sparse CSR tensor. `mat1` and `mat2` must be dense tensors.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - a sparse CSR matrix of shape (m, n) to be added and used to compute
the sampled matrix multiplication
- **mat1** ([*Tensor*](../tensors.html#torch.Tensor)) - a dense matrix of shape (m, k) to be multiplied
- **mat2** ([*Tensor*](../tensors.html#torch.Tensor)) - a dense matrix of shape (k, n) to be multiplied

Keyword Arguments:

- **beta** (*Number**,**optional*) - multiplier for `input` (β\betaβ)
- **alpha** (*Number**,**optional*) - multiplier for mat1@mat2mat1 @ mat2mat1@mat2 (α\alphaα)
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - output tensor. Ignored if None. Default: None.

Examples:

```
>>> input = torch.eye(3, device='cuda').to_sparse_csr()
>>> mat1 = torch.randn(3, 5, device='cuda')
>>> mat2 = torch.randn(5, 3, device='cuda')
>>> torch.sparse.sampled_addmm(input, mat1, mat2)
tensor(crow_indices=tensor([0, 1, 2, 3]),
 col_indices=tensor([0, 1, 2]),
 values=tensor([ 0.2847, -0.7805, -0.1900]), device='cuda:0',
 size=(3, 3), nnz=3, layout=torch.sparse_csr)
>>> torch.sparse.sampled_addmm(input, mat1, mat2).to_dense()
tensor([[ 0.2847, 0.0000, 0.0000],
 [ 0.0000, -0.7805, 0.0000],
 [ 0.0000, 0.0000, -0.1900]], device='cuda:0')
>>> torch.sparse.sampled_addmm(input, mat1, mat2, beta=0.5, alpha=0.5)
tensor(crow_indices=tensor([0, 1, 2, 3]),
 col_indices=tensor([0, 1, 2]),
 values=tensor([ 0.1423, -0.3903, -0.0950]), device='cuda:0',
 size=(3, 3), nnz=3, layout=torch.sparse_csr)
```