# torch.func._random.normal_

torch.func._random.normal_(*key*, *result*, ***, *mean=0.0*, *std=1.0*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/func/_random.py#L161)

Fill `result` in-place with normal random values from a PRNG key.

The values are drawn from a normal distribution with the specified `mean`
and `std`. The output is fully determined by the key, so calling with the
same key always produces the same result.

Supports batched keys: if `key` has shape `(*batch, K)`, the leading
dimensions of `result` must be broadcastable with `*batch` and each key
independently generates its slice of the output.

Parameters:

- **key** ([*Tensor*](../tensors.html#torch.Tensor)) - A PRNG key returned by [`key()`](torch.func._random.key.html#torch.func._random.key), [`split()`](torch.func._random.split.html#torch.func._random.split), or
[`fold_in()`](torch.func._random.fold_in.html#torch.func._random.fold_in).
- **result** ([*Tensor*](../tensors.html#torch.Tensor)) - The output tensor to fill in-place.
- **mean** ([*float*](https://docs.python.org/3/builtins/functions.html#float)) - Mean of the normal distribution. Default: `0.0`.
- **std** ([*float*](https://docs.python.org/3/builtins/functions.html#float)) - Standard deviation of the normal distribution. Default: `1.0`.

Returns:

`result`, filled with normal random values.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Example:

```
>>> key = torch.func._random.key(42, device="cuda") 
>>> result = torch.empty(1000, device="cuda") 
>>> torch.func._random.normal_(key, result)
```