# torch.func._random.key

torch.func._random.key(*seed*, ***, *device=None*, *impl='philox4x32-10'*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/func/_random.py#L31)

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

Each Philox call on a `(seed, offset)` pair produces 128 random bits,
which yield `E = 4` values for dtypes of 32 bits or fewer, or `E = 2`
for 64-bit dtypes. Each value of [`uniform()`](torch.func._random.uniform.html#torch.func._random.uniform), [`randint()`](torch.func._random.randint.html#torch.func._random.randint), and
[`bits()`](torch.func._random.bits.html#torch.func._random.bits) comes from its own `128 / E` bits, while [`normal()`](torch.func._random.normal.html#torch.func._random.normal)
derives each pair of values from each pair's worth of bits via the
Box-Muller transform. Element `i` (in row-major order) of a key's
output, or of each slice a batched key generates, is value `i % E` of
the call at `(offset + i // E) % 2**64`. Thus the key
`torch.tensor([seed, offset + k], dtype=torch.uint64)` skips the
first `k * E` elements, generating a contiguous range of the output
starting there (e.g. a row shard of a parameter) directly. Such keys
share counters with [`split()`](torch.func._random.split.html#torch.func._random.split) and [`fold_in()`](torch.func._random.fold_in.html#torch.func._random.fold_in) children of the
original key, so don't both shift and derive from the same key.

Example:

```
>>> key = torch.func._random.key(42, device="cuda")
```