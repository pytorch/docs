# torch.func._random.key

torch.func._random.key(*seed*, ***, *device=None*, *impl='philox4x32-10'*)[[source]](https://github.com/pytorch/pytorch/blob/5b1433112eb30368cb8f63b3bf0145b391ec72a5/torch/func/_random.py#L31)

Create a PRNG key from a seed.

A key is a tensor that encodes the state needed to deterministically
produce random values. Keys are consumed by generation functions to produce
reproducible random tensors without any global state. The internal
representation of the key depends on the chosen PRNG algorithm.

Parameters:

- **seed** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - The seed value for the PRNG.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - The desired device for the
returned key. Default: the current default device (see
[`torch.set_default_device()`](torch.set_default_device.html#torch.set_default_device)).
- **impl** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - PRNG algorithm. Currently only `"philox4x32-10"` is
supported.

Returns:

A tensor representing the PRNG key.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Note

For the `"philox4x32-10"` algorithm, the key is a uint64 tensor of
shape `(2,)` encoding a `(seed, offset)` pair. The offset determines
the starting position in the Philox output stream.

Example:

```
>>> key = torch.func._random.key(42, device="cuda")
```