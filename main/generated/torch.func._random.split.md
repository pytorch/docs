# torch.func._random.split

torch.func._random.split(*key*, *num=2*)[[source]](https://github.com/pytorch/pytorch/blob/f8a8dd25ad84298ffbd713e8dbdb5bba38ef907d/torch/func/_random.py#L83)

Split a PRNG key into `num` new independent keys.

Each returned key produces a different, deterministic random sequence.
This is the primary mechanism for deriving multiple independent keys from
a single parent key without mutating any state.

Supports batched keys: if `key` has shape `(*batch, K)`, each key in the
batch is split independently and the result has shape `(num, *batch, K)`.

Parameters:

- **key** ([*Tensor*](../tensors.html#torch.Tensor)) - A PRNG key returned by [`key()`](torch.func._random.key.html#torch.func._random.key), `split()`, or
[`fold_in()`](torch.func._random.fold_in.html#torch.func._random.fold_in).
- **num** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Number of keys to produce. Default: `2`.

Returns:

A tensor of shape `(num, *key.shape)` containing the derived keys.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Example:

```
>>> key = torch.func._random.key(42, device="cuda") 
>>> k1, k2 = torch.func._random.split(key)
```