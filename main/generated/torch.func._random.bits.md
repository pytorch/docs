# torch.func._random.bits

torch.func._random.bits(*key*, **shape*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/func/_random.py#L611)

Generate raw random bits from a PRNG key.

Equivalent to [`randint()`](torch.func._random.randint.html#torch.func._random.randint) over the full range of `dtype`. That range
is a power of two, so unlike a bounded draw this is exactly uniform. Signed
dtypes receive negative values as well.

Dtypes narrower than 32 bits take the low bits of a full 32-bit sample, so
`bits(key, shape, dtype=torch.int8)` matches `bits(key, shape,
dtype=torch.int32).to(torch.int8)`.

Supports batched keys: if `key` has shape `(*batch, K)`, the leading
dimensions of `shape` must be broadcastable with `*batch` and each key
independently generates its slice of the output.

Parameters:

- **key** ([*Tensor*](../tensors.html#torch.Tensor)) - A PRNG key returned by [`key()`](torch.func._random.key.html#torch.func._random.key), [`split()`](torch.func._random.split.html#torch.func._random.split), or
[`fold_in()`](torch.func._random.fold_in.html#torch.func._random.fold_in).
- ***shape** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - The desired output shape.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - The desired dtype: any integer
dtype other than `torch.bool`. Default: `torch.int32`.

Returns:

A tensor of the given shape filled with raw random bits.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Example:

```
>>> key = torch.func._random.key(42, device="cuda") 
>>> torch.func._random.bits(key, (1000,), dtype=torch.uint64)
```