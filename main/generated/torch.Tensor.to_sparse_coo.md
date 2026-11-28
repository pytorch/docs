# torch.Tensor.to_sparse_coo

Tensor.to_sparse_coo()[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/_tensor.py#L1406)

Convert a tensor to [coordinate format](../sparse.html#sparse-coo-docs).

Examples:

```
>>> dense = torch.randn(5, 5)
>>> sparse = dense.to_sparse_coo()
>>> sparse._nnz()
25
```