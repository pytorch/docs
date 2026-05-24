# torch.sparse.as_sparse_gradcheck

torch.sparse.as_sparse_gradcheck(*gradcheck*)[[source]](https://github.com/pytorch/pytorch/blob/15e96b281415c58d3acf5d63d86df9d68744ee16/torch/sparse/__init__.py#L566)

Decorate function, to extend gradcheck for sparse tensors.

Decorator for torch.autograd.gradcheck or its functools.partial
variants that extends the gradcheck function with support to input
functions that operate on or/and return sparse tensors.

The specified gradcheck function itself is guaranteed to operate
on strided tensors only.

For example:

```
>>> gradcheck = torch.sparse.as_sparse_gradcheck(torch.autograd.gradcheck)
>>> x = (
... torch.tensor([[0, 1], [2, 3]], dtype=torch.float64)
... .to_sparse_coo()
... .requires_grad_(True)
... )
>>> gradcheck(lambda x: x.to_sparse_csr(), x)
True
```