# torch.Tensor.to_sparse_coo

Tensor.to_sparse_coo()[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/_tensor.py#L1370)

Convert a tensor to [coordinate format](../sparse.html#sparse-coo-docs).

Examples:

```
>>> dense = torch.randn(5, 5)
>>> sparse = dense.to_sparse_coo()
>>> sparse._nnz()
25
```