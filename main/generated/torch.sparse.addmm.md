# torch.sparse.addmm

torch.sparse.addmm(*mat*, *mat1*, *mat2*, ***, *beta=1.*, *alpha=1.*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/c8080db61856d74ad76795af1c6aa1fd41b7b862/torch/sparse/__init__.py#L45)

This function does exact same thing as [`torch.addmm()`](torch.addmm.html#torch.addmm) in the forward,
except that it supports backward for sparse COO and CSR matrix `mat1`.
When `mat1` is a COO tensor it must have sparse_dim = 2.

Supports both CSR and COO storage formats.

Note

**Gradient support:**

- **COO @ Dense**: Backward is supported for both inputs. The gradient for the
sparse input is returned as a sparse COO tensor.
- **CSR @ Dense**: Backward is supported for both inputs. The gradient for the
sparse input is returned as a sparse CSR tensor.
- **CSC/BSR/BSC @ Dense**: Not supported.
- **Sparse @ Sparse** (COO @ COO, CSR @ CSR): Forward works, but backward is
not supported.

Parameters:

- **mat** ([*Tensor*](../tensors.html#torch.Tensor)) - a dense matrix to be added
- **mat1** ([*Tensor*](../tensors.html#torch.Tensor)) - a sparse matrix to be multiplied
- **mat2** ([*Tensor*](../tensors.html#torch.Tensor)) - a dense matrix to be multiplied
- **beta** (*Number**,**optional*) - multiplier for `mat` (β\betaβ)
- **alpha** (*Number**,**optional*) - multiplier for mat1@mat2mat1 @ mat2mat1@mat2 (α\alphaα)