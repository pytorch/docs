# torch.func._random.randint

torch.func._random.randint(*key*, **shape*, *low=0*, *high=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/7e752fbd7bf384857985d3e556423eaca714bbfe/torch/func/_random.py#L450)

Generate uniform random integers in `[low, high)` from a PRNG key.

Produces a tensor of the given shape filled with integers drawn uniformly
from `[low, high)`. The output is fully determined by the key, so calling
with the same key always returns the same result. The output is placed on the
same device as `key`.

`low` defaults to `0` and `high` to the dtype's largest value plus
one. Passing `None` for either selects the corresponding limit of
`dtype`, so `low=None` with no `high` draws from the full range.

Warning

The signature differs from [`torch.randint()`](torch.randint.html#torch.randint). Bounds are
keyword-only and follow the shape, matching [`uniform()`](torch.func._random.uniform.html#torch.func._random.uniform) and
[`normal()`](torch.func._random.normal.html#torch.func._random.normal) in this module, whereas [`torch.randint()`](torch.randint.html#torch.randint) takes them
positionally before the size:

```
torch.randint(10, (2, 3)) # -> [0, 10)
randint(key, (2, 3), high=10)

torch.randint(1, 5, (2, 3)) # -> [1, 5)
randint(key, (2, 3), low=1, high=5)
```

Note that a positional integer is a shape dimension here, not a bound,
so `randint(key, 10, high=5)` produces ten values in `[0, 5)` rather
than the `[0, 10)` that [`torch.randint()`](torch.randint.html#torch.randint) would give.

This function also accepts `None` bounds for the dtype's limits, which
[`torch.randint()`](torch.randint.html#torch.randint) does not.

Supports batched keys: if `key` has shape `(*batch, K)`, the leading
dimensions of `shape` must be broadcastable with `*batch` and each key
independently generates its slice of the output.

Parameters:

- **key** ([*Tensor*](../tensors.html#torch.Tensor)) - A PRNG key returned by [`key()`](torch.func._random.key.html#torch.func._random.key), [`split()`](torch.func._random.split.html#torch.func._random.split), or
[`fold_in()`](torch.func._random.fold_in.html#torch.func._random.fold_in).
- ***shape** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - The desired output shape.
- **low** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Lower bound (inclusive) of the range. `None` means
the dtype's smallest value. Default: `0`.
- **high** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Upper bound (exclusive) of the range. `None` means
the dtype's largest value plus one. For 32-bit dtypes,
`high - low` must be a power of two or less than `2 ** 28`;
see the note below.
Default: `None`.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - The desired dtype: any integer
dtype other than `torch.bool`. Default: `torch.int32`.

Returns:

A tensor of the given shape filled with random integers.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Note

**Sampling width.** Each element draws a fixed `nbits` of randomness:
64 for the 8-byte dtypes (`torch.int64` / `torch.uint64`) and 32 for
every narrower one. Dtypes smaller than 32 bits are *not* packed several
to a word; each element still consumes a full 32-bit sample, the range
reduction is done at 32 bits, and only the final store narrows to the
output dtype (keeping the low bits). Sampling `torch.int8` therefore
matches sampling `torch.int32` and casting down with
[`to()`](torch.Tensor.to.html#torch.Tensor.to), and its bias is measured against `2 ** 32`
rather than `2 ** 8`.

**Sampling bias.** The `nbits` sample is reduced into `[low, high)`
with a modulo. That is exactly uniform only when `high - low` divides `2 ** nbits`,
i.e. when the range is a power of two; otherwise the lowest
`2 ** nbits % (high - low)` values of the range are returned slightly
more often than the rest.

With `q = 2 ** nbits // (high - low)`, the most frequent value occurs
`1 + 1 / q` times as often as the least frequent, so the worst case
grows with the range:

```
q = 2**nbits // (high - low)
bias = 0.0 if 2**nbits % (high - low) == 0 else 1.0 / q
```

Away from the exact cases this is close to `(high - low) / 2 ** nbits`.
It is a step function of the range, changing only where `q` does.
Exact powers of two are unbiased, so the figures below bound every range
up to the listed size, for a 32-bit dtype:

| Range up to | Max relative bias |
| --- | --- |
| `2 ** 8` | 0.000006% |
| `2 ** 16` | 0.0015% |
| `2 ** 20` | 0.024% |
| `2 ** 24` | 0.39% |
| `2 ** 26` | 1.6% |
| `2 ** 27` | 3.1% |
| `2 ** 28` | 6.25% |

Ranges of `2 ** 28` or more are rejected for dtypes sampled at 32 bits,
to keep the bias under roughly 6%; use a 64-bit dtype if you need a range
that large. Ranges that divide `2 ** 32` evenly (powers of two) are
exact at any size and are always allowed. Dtypes narrower than 32 bits can never reach that limit, since
their ranges cap at `2 ** 16`, so their bias stays below 0.0015%.
64-bit dtypes are not restricted, since the same formula over
`2 ** 64` keeps the bias near `2e-10` even at a range of `2 ** 32`.

Using the dtype's full range (omitting both bounds) is always exactly
uniform, since that range is a power of two and no reduction is applied.

Example:

```
>>> r = torch.func._random
>>> key = r.key(42, device="cuda")
>>> r.randint(key, (1000,), high=10) # [0, 10)
>>> r.randint(key, (1000,), low=-5, high=5) # [-5, 5)
>>> r.randint(key, 2, 3, high=10, dtype=torch.int64) # shape (2, 3)
>>> r.randint(key, (1000,), low=None) # the dtype's full range
```