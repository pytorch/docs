# torch.func._random.bits_

torch.func._random.bits_(*key*, *result*)[[source]](https://github.com/pytorch/pytorch/blob/e9565720ab4f59a0ed491b3f8440ae38c2455bab/torch/func/_random.py#L582)

Fill `result` in-place with raw random bits from a PRNG key.

Equivalent to [`randint_()`](torch.func._random.randint_.html#torch.func._random.randint_) over the full range of `result`'s dtype.
That range is a power of two, so unlike a bounded draw this is exactly
uniform. Signed dtypes receive negative values as well.

Supports batched keys: if `key` has shape `(*batch, K)`, the leading
dimensions of `result` must be broadcastable with `*batch` and each key
independently generates its slice of the output.

Parameters:

- **key** ([*Tensor*](../tensors.html#torch.Tensor)) - A PRNG key returned by [`key()`](torch.func._random.key.html#torch.func._random.key), [`split()`](torch.func._random.split.html#torch.func._random.split), or
[`fold_in()`](torch.func._random.fold_in.html#torch.func._random.fold_in).
- **result** ([*Tensor*](../tensors.html#torch.Tensor)) - The output tensor to fill in-place. Must have an
integer dtype other than `torch.bool`.

Returns:

`result`, filled with raw random bits.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Example:

```
>>> key = torch.func._random.key(42, device="cuda") 
>>> result = torch.empty(1000, dtype=torch.uint32, device="cuda") 
>>> torch.func._random.bits_(key, result)
```