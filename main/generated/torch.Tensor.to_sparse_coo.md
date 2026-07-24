# torch.Tensor.to_sparse_coo

Tensor.to_sparse_coo()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/_tensor.py#L1368)

Convert a tensor to [coordinate format](../sparse.html#sparse-coo-docs).

Examples:

```
>>> dense = torch.randn(5, 5)
>>> sparse = dense.to_sparse_coo()
>>> sparse._nnz()
25
```