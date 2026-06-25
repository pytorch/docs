# torch.nn.attention.bias.causal_lower_right

torch.nn.attention.bias.causal_lower_right(**size*)[[source]](https://github.com/pytorch/pytorch/blob/847b7df02b84551445eda7d44d08f15bda4c6159/torch/nn/attention/bias.py#L342)

Creates a lower-right triangular causal bias.

This function generates a lower-right triangular matrix to represent causal attention bias with a
diagonal offset set so that the inclusive values are aligned to the lower right corner of the matrix.

The equivalent pytorch code for constructing this bias is:

```
diagonal_offset = size[1] - size[0]
torch.tril(
 torch.ones(size, dtype=torch.bool),
 diagonal=diagonal_offset,
)
```

For instance, with shape=(3,4), the materialized bias tensor will be:

```
[[1, 1, 0, 0],
 [1, 1, 1, 0],
 [1, 1, 1, 1]]
```

Parameters:

**size** - The size of the bias matrix.

Returns:

The LOWER_RIGHT triangular causal bias variant.

Return type:

[CausalBias](torch.nn.attention.bias.CausalBias.html#torch.nn.attention.bias.CausalBias)