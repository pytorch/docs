# torch.func._random.normal

torch.func._random.normal(*key*, **shape*, *mean=0.0*, *std=1.0*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/efbc87071fdf61bd50d5dc3b315b65bd452c401d/torch/func/_random.py#L197)

Generate normally distributed random values from a PRNG key.

Produces a tensor of the given shape filled with values drawn from a normal
distribution with the specified `mean` and `std`. The output is fully
determined by the key, so calling with the same key always returns the same
result. The output is placed on the same device as `key`.

Supports batched keys: if `key` has shape `(*batch, K)`, the leading
dimensions of `shape` must be broadcastable with `*batch` and each key
independently generates its slice of the output.

Parameters:

- **key** ([*Tensor*](../tensors.html#torch.Tensor)) - A PRNG key returned by [`key()`](torch.func._random.key.html#torch.func._random.key), [`split()`](torch.func._random.split.html#torch.func._random.split), or
[`fold_in()`](torch.func._random.fold_in.html#torch.func._random.fold_in).
- ***shape** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - The desired output shape.
- **mean** ([*float*](https://docs.python.org/3/builtins/functions.html#float)) - Mean of the normal distribution. Default: `0.0`.
- **std** ([*float*](https://docs.python.org/3/builtins/functions.html#float)) - Standard deviation of the normal distribution. Default: `1.0`.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - The desired dtype. Default: `torch.float32`.

Returns:

A tensor of the given shape filled with normal random values.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Example:

```
>>> key = torch.func._random.key(42, device="cuda") 
>>> torch.func._random.normal(key, (1000,))
```