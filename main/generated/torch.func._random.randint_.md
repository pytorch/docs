# torch.func._random.randint_

torch.func._random.randint_(*key*, *result*, ***, *low=0*, *high=None*)[[source]](https://github.com/pytorch/pytorch/blob/e9565720ab4f59a0ed491b3f8440ae38c2455bab/torch/func/_random.py#L345)

Fill `result` in-place with uniform random integers in `[low, high)`.

`low` defaults to `0` and `high` to the dtype's largest value plus one.
Passing `None` for either selects the corresponding limit of the dtype, so
`randint_(key, result, low=None, high=None)` draws from the dtype's full
range.

Warning

The two in-place analogues in core PyTorch both take bounds
positionally, while these are keyword-only. Versus
[`torch.randint()`](torch.randint.html#torch.randint) with `out=`, which needs the size even though
`out` already fixes it:

```
torch.randint(10, (2, 3), out=result) # -> [0, 10)
randint_(key, result, high=10) # size comes from result

torch.randint(1, 5, (2, 3), out=result) # -> [1, 5)
randint_(key, result, low=1, high=5)
```

Versus [`torch.Tensor.random_()`](torch.Tensor.random_.html#torch.Tensor.random_), which names the bounds `from` /
`to` and treats a lone bound as the upper one:

```
result.random_(10) # -> [0, 10)
randint_(key, result, high=10)

result.random_(1, 5) # -> [1, 5)
randint_(key, result, low=1, high=5)

result.random_() # -> [0, DTYPE_MAX]
randint_(key, result)

result.random_(DTYPE_MIN, None) # whole dtype range
randint_(key, result, low=None, high=None)
```

The bound defaults agree: both fill `[0, DTYPE_MAX]` when given no
bounds, and both need an explicit lower bound to reach negative values.
The spelling differs in that `None` here means the dtype's limit for
either bound, so `low=None` replaces `random_`'s `DTYPE_MIN`.

The output is fully determined by the key, so calling with the same key
always produces the same result.

Supports batched keys: if `key` has shape `(*batch, K)`, the leading
dimensions of `result` must be broadcastable with `*batch` and each key
independently generates its slice of the output.

Parameters:

- **key** ([*Tensor*](../tensors.html#torch.Tensor)) - A PRNG key returned by [`key()`](torch.func._random.key.html#torch.func._random.key), [`split()`](torch.func._random.split.html#torch.func._random.split), or
[`fold_in()`](torch.func._random.fold_in.html#torch.func._random.fold_in).
- **result** ([*Tensor*](../tensors.html#torch.Tensor)) - The output tensor to fill in-place. Must have an
integer dtype other than `torch.bool`.
- **low** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Lower bound (inclusive) of the range. `None` means
the dtype's smallest value. Default: `0`.
- **high** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Upper bound (exclusive) of the range. `None` means
the dtype's largest value plus one. For 32-bit dtypes,
`high - low` must be a power of two or less than `2 ** 28`;
see the note below.
Default: `None`.

Returns:

`result`, filled with random integers.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Note

Values are reduced into `[low, high)` with a modulo, which is exactly
uniform only when `high - low` is a power of two. Other ranges of
`2 ** 28` or more are rejected for 32-bit dtypes; use a 64-bit dtype if
you need a range that large. See [`randint()`](torch.func._random.randint.html#torch.func._random.randint) for the bias in detail.

Example:

```
>>> key = torch.func._random.key(42, device="cuda") 
>>> result = torch.empty(1000, dtype=torch.int64, device="cuda") 
>>> torch.func._random.randint_(key, result, high=10)
```