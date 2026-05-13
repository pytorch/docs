# CausalVariant

*class*torch.nn.attention.bias.CausalVariant(*value*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/nn/attention/bias.py#L33)

Enum for causal variants used in attention mechanisms.

Defines two types of causal biases:

`UPPER_LEFT`: Represents upper-left triangular bias for standard causal attention.
The equivalent pytorch code for constructing this bias is:

```
torch.tril(torch.ones(size, dtype=torch.bool))
```

For instance, with `shape=(3,4)`, the materialized bias tensor will be:

```
[[1, 0, 0, 0],
 [1, 1, 0, 0],
 [1, 1, 1, 0]]
```

`LOWER_RIGHT`: Represents lower-right triangular bias, the include values are aligned to the lower
right corner of the matrix.

The equivalent pytorch code for constructing this bias is:

```
diagonal_offset = size[1] - size[0]
torch.tril(
 torch.ones(size, dtype=torch.bool),
 diagonal=diagonal_offset,
)
```

For instance, with `shape=(3,4)`, the materialized bias tensor will be:

```
[[1, 1, 0, 0],
 [1, 1, 1, 0],
 [1, 1, 1, 1]]
```

Note that these variants are equivalent to each other when the sequence lengths of the query and key/value
tensors are equal since the triangular matrix is square.

Warning

This enum is a prototype and subject to change.