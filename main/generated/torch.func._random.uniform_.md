# torch.func._random.uniform_

torch.func._random.uniform_(*key*, *result*, ***, *low=0.0*, *high=1.0*)[[source]](https://github.com/pytorch/pytorch/blob/f8a8dd25ad84298ffbd713e8dbdb5bba38ef907d/torch/func/_random.py#L241)

Fill `result` in-place with uniform random values from a PRNG key.

The values are drawn uniformly from the interval `[low, high)`. The output
is fully determined by the key, so calling with the same key always produces
the same result.

Supports batched keys: if `key` has shape `(*batch, K)`, the leading
dimensions of `result` must be broadcastable with `*batch` and each key
independently generates its slice of the output.

Gradients flow to tensor `low` / `high` as for a reparameterized sample
(like `torch.distributions.Distribution.rsample()`).

Parameters:

- **key** ([*Tensor*](../tensors.html#torch.Tensor)) - A PRNG key returned by [`key()`](torch.func._random.key.html#torch.func._random.key), [`split()`](torch.func._random.split.html#torch.func._random.split), or
[`fold_in()`](torch.func._random.fold_in.html#torch.func._random.fold_in).
- **result** ([*Tensor*](../tensors.html#torch.Tensor)) - The output tensor to fill in-place.
- **low** ([*float*](https://docs.python.org/3/builtins/functions.html#float)*or*[*Tensor*](../tensors.html#torch.Tensor)) - Lower bound (inclusive) of the uniform
distribution. A floating-point tensor must broadcast to `result`
and gives a bound per element. Default: `0.0`.
- **high** ([*float*](https://docs.python.org/3/builtins/functions.html#float)*or*[*Tensor*](../tensors.html#torch.Tensor)) - Upper bound (exclusive) of the uniform
distribution. A floating-point tensor must broadcast to `result`
and gives a bound per element. Default: `1.0`.

Returns:

`result`, filled with uniform random values.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Example:

```
>>> key = torch.func._random.key(42, device="cuda") 
>>> result = torch.empty(1000, device="cuda") 
>>> torch.func._random.uniform_(key, result)
```