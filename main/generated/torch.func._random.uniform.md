# torch.func._random.uniform

torch.func._random.uniform(*key*, **shape*, *low=0.0*, *high=1.0*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/func/_random.py#L294)

Generate uniformly distributed random values from a PRNG key.

Produces a tensor of the given shape filled with values drawn uniformly
from the interval `[low, high)`. The output is fully determined by the
key, so calling with the same key always returns the same result. The output
is placed on the same device as `key`.

Supports batched keys: if `key` has shape `(*batch, K)`, the leading
dimensions of `shape` must be broadcastable with `*batch` and each key
independently generates its slice of the output.

Gradients flow to tensor `low` / `high` as for a reparameterized sample
(like `torch.distributions.Distribution.rsample()`).

Parameters:

- **key** ([*Tensor*](../tensors.html#torch.Tensor)) - A PRNG key returned by [`key()`](torch.func._random.key.html#torch.func._random.key), [`split()`](torch.func._random.split.html#torch.func._random.split), or
[`fold_in()`](torch.func._random.fold_in.html#torch.func._random.fold_in).
- ***shape** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - The desired output shape.
- **low** ([*float*](https://docs.python.org/3/builtins/functions.html#float)*or*[*Tensor*](../tensors.html#torch.Tensor)) - Lower bound (inclusive) of the uniform
distribution. A floating-point tensor must broadcast to `shape`
and gives a bound per element. Default: `0.0`.
- **high** ([*float*](https://docs.python.org/3/builtins/functions.html#float)*or*[*Tensor*](../tensors.html#torch.Tensor)) - Upper bound (exclusive) of the uniform
distribution. A floating-point tensor must broadcast to `shape`
and gives a bound per element. Default: `1.0`.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - The desired dtype. Default: `torch.float32`.

Returns:

A tensor of the given shape filled with uniform random values.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Example:

```
>>> key = torch.func._random.key(42, device="cuda") 
>>> torch.func._random.uniform(key, (1000,))
```