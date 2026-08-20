# torch.Tensor.to_sparse_coo

Tensor.to_sparse_coo()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/_tensor.py#L1368)

Convert a tensor to [coordinate format](../sparse.html#sparse-coo-docs).

Examples:

```
>>> dense = torch.randn(5, 5)
>>> sparse = dense.to_sparse_coo()
>>> sparse._nnz()
25
```