# torch.sparse.mm

torch.sparse.mm()[[source]](https://github.com/pytorch/pytorch/blob/24e9a3928e16bb875a0a4ae3d26677dd7ddc8e02/torch/sparse/__init__.py#L77)

> Performs a matrix multiplication of the sparse matrix `mat1`
> and the (sparse or strided) matrix `mat2`. Similar to [`torch.mm()`](torch.mm.html#torch.mm), if `mat1` is a
> (n×m)(n \times m)(n×m) tensor, `mat2` is a (m×p)(m \times p)(m×p) tensor, out will be a
> (n×p)(n \times p)(n×p) tensor.
> When `mat1` is a COO tensor it must have sparse_dim = 2.
> 
> 
> 
> 
> Supports both CSR and COO storage formats.

Note

**Gradient support:**

- **COO @ Dense**: Backward is supported for both inputs. The gradient for the
sparse input is returned as a sparse COO tensor.
- **CSR @ Dense**: Backward is supported for both inputs. The gradient for the
sparse input is returned as a sparse CSR tensor.
- **CSC/BSR/BSC @ Dense**: Not supported.
- **Sparse @ Sparse** (COO @ COO, CSR @ CSR): Forward works, but backward is
not supported.
- **Mixed formats** (COO @ CSR, CSR @ COO): Not supported.

This function also additionally accepts an optional `reduce` argument that allows
specification of an optional reduction operation, mathematically performs the following operation:

zij=⨁k=0K−1xikykjz_{ij} = \bigoplus_{k = 0}^{K - 1} x_{ik} y_{kj}zij​=k=0⨁K−1​xik​ykj​

where ⨁\bigoplus⨁ defines the reduce operator. `reduce` is implemented only for
CSR storage format on CPU device.

Parameters:

- **mat1** ([*Tensor*](../tensors.html#torch.Tensor)) - the first sparse matrix to be multiplied
- **mat2** ([*Tensor*](../tensors.html#torch.Tensor)) - the second matrix to be multiplied, which could be sparse or dense
- **reduce** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - the reduction operation to apply for non-unique indices
(`"sum"`, `"mean"`, `"amax"`, `"amin"`). Default `"sum"`.

Shape:

The format of the output tensor of this function follows:
- sparse x sparse -> sparse
- sparse x dense -> dense

Example:

```
>>> a = torch.tensor([[1., 0, 2], [0, 3, 0]]).to_sparse().requires_grad_()
>>> a
tensor(indices=tensor([[0, 0, 1],
 [0, 2, 1]]),
 values=tensor([1., 2., 3.]),
 size=(2, 3), nnz=3, layout=torch.sparse_coo, requires_grad=True)
>>> b = torch.tensor([[0, 1.], [2, 0], [0, 0]], requires_grad=True)
>>> b
tensor([[0., 1.],
 [2., 0.],
 [0., 0.]], requires_grad=True)
>>> y = torch.sparse.mm(a, b)
>>> y
tensor([[0., 1.],
 [6., 0.]], grad_fn=<SparseAddmmBackward0>)
>>> y.sum().backward()
>>> a.grad
tensor(indices=tensor([[0, 0, 1],
 [0, 2, 1]]),
 values=tensor([1., 0., 2.]),
 size=(2, 3), nnz=3, layout=torch.sparse_coo)
>>> c = a.detach().to_sparse_csr()
>>> c
tensor(crow_indices=tensor([0, 2, 3]),
 col_indices=tensor([0, 2, 1]),
 values=tensor([1., 2., 3.]), size=(2, 3), nnz=3,
 layout=torch.sparse_csr)
>>> y1 = torch.sparse.mm(c, b, 'sum')
>>> y1
tensor([[0., 1.],
 [6., 0.]], grad_fn=<SparseMmReduceImplBackward0>)
>>> y2 = torch.sparse.mm(c, b, 'max')
>>> y2
tensor([[0., 1.],
 [6., 0.]], grad_fn=<SparseMmReduceImplBackward0>)
```