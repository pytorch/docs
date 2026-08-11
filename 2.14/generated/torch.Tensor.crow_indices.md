# torch.Tensor.crow_indices

Tensor.crow_indices() → IntTensor

Returns the tensor containing the compressed row indices of the `self`
tensor when `self` is a sparse CSR tensor of layout `sparse_csr`.
The `crow_indices` tensor is strictly of shape (`self`.size(0) + 1)
and of type `int32` or `int64`. When using MKL routines such as sparse
matrix multiplication, it is necessary to use `int32` indexing in order
to avoid downcasting and potentially losing information.

Example:

```
>>> csr = torch.eye(5,5).to_sparse_csr()
>>> csr.crow_indices()
tensor([0, 1, 2, 3, 4, 5], dtype=torch.int32)
```