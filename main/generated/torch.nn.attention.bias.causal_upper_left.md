# torch.nn.attention.bias.causal_upper_left

torch.nn.attention.bias.causal_upper_left(**size*)[[source]](https://github.com/pytorch/pytorch/blob/ca0571943b5289419bf52b30ee31769eb76a58c8/torch/nn/attention/bias.py#L308)

Creates an upper-left triangular causal bias.

This function generates an upper-left triangular matrix to represent causal attention bias with a
diagonal offset set so that the inclusive values are aligned to the upper left corner of the matrix.
This equivalent to the is_causal=True argument in scaled_dot_product_attention.

The equivalent pytorch code for constructing this bias is:

```
torch.tril(torch.ones(size, dtype=torch.bool))
```

For instance, with shape=(3,4), the materialized bias tensor will be:

```
[[1, 0, 0, 0],
 [1, 1, 0, 0],
 [1, 1, 1, 0]]
```

Parameters:

**size** - The size of the bias matrix.

Returns:

The UPPER_LEFT triangular causal bias variant.

Return type:

[CausalBias](torch.nn.attention.bias.CausalBias.html#torch.nn.attention.bias.CausalBias)