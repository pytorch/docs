# torch.func._random.fold_in

torch.func._random.fold_in(*key*, *data*)[[source]](https://github.com/pytorch/pytorch/blob/e9565720ab4f59a0ed491b3f8440ae38c2455bab/torch/func/_random.py#L109)

Deterministically derive a new key by folding in an integer value.

`data` may be a Python `int` or a single-item `uint64` tensor on the
same device as `key`. Note that passing `data` as a tensor prevents it
from being baked into a captured CUDA graph, so the graph can be replayed
with a different value without recapture.

Equivalent to `split(key, data + 1)[data]`, but more efficient when
only a single derived key is needed. Useful for associating a key with
a loop iteration, layer index, or other integer identifier.

Supports batched keys: if `key` has shape `(*batch, K)`, `data` is
folded into each key independently.

Parameters:

- **key** ([*Tensor*](../tensors.html#torch.Tensor)) - A PRNG key returned by [`key()`](torch.func._random.key.html#torch.func._random.key), [`split()`](torch.func._random.split.html#torch.func._random.split), or
`fold_in()`.
- **data** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*Tensor*](../tensors.html#torch.Tensor)) - The value to fold into the key, interpreted as
uint64. An `int` must be within the inclusive range
`[-0x8000_0000_0000_0000, 0xffff_ffff_ffff_ffff]`. Negative inputs
are remapped to positive values with the formula
`0x1_0000_0000_0000_0000 + data`. A tensor must have dtype
`uint64`, contain a single value, and reside on the same device
as `key`.

Returns:

A new key tensor with the same shape as `key`.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Example:

```
>>> key = torch.func._random.key(42, device="cuda") 
>>> k0 = torch.func._random.fold_in(key, 0) 
>>> k1 = torch.func._random.fold_in(key, 1) 
>>> # Equivalent to split:
>>> keys = torch.func._random.split(key, 2) 
>>> assert torch.equal(k0, keys[0]) 
>>> assert torch.equal(k1, keys[1])
```