# torch.Tensor.to_sparse_coo

Tensor.to_sparse_coo()[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/_tensor.py#L1517)

Convert a tensor to [coordinate format](../sparse.html#sparse-coo-docs).

Examples:

```
>>> dense = torch.randn(5, 5)
>>> sparse = dense.to_sparse_coo()
>>> sparse._nnz()
25
```