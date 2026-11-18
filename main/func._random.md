# torch.func._random

Warning

These APIs are a prototype and may change or be removed without notice. The module is private and not covered
by PyTorch's backward compatibility policy. Read more about feature classification at:
https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype

`torch.func._random` provides JAX-style stateless PRNG APIs: randomness is a pure function of an explicit key
tensor rather than of global generator state. The module is not imported by `import torch`; import it explicitly
with `import torch.func._random` before use.

These APIs do not yet support [`torch.func.vmap()`](generated/torch.func.vmap.html#torch.func.vmap). To generate a batch of independent samples, pass a batch of
keys with shape `(*batch, K)` (e.g. from [`split()`](generated/torch.func._random.split.html#torch.func._random.split)) instead.

| [`key`](generated/torch.func._random.key.html#torch.func._random.key) | Create a PRNG key from a seed. |
| --- | --- |
| [`split`](generated/torch.func._random.split.html#torch.func._random.split) | Split a PRNG key into `num` new independent keys. |
| [`fold_in`](generated/torch.func._random.fold_in.html#torch.func._random.fold_in) | Deterministically derive a new key by folding in an integer value. |
| [`uniform`](generated/torch.func._random.uniform.html#torch.func._random.uniform) | Generate uniformly distributed random values from a PRNG key. |
| [`uniform_`](generated/torch.func._random.uniform_.html#torch.func._random.uniform_) | Fill `result` in-place with uniform random values from a PRNG key. |
| [`normal`](generated/torch.func._random.normal.html#torch.func._random.normal) | Generate normally distributed random values from a PRNG key. |
| [`normal_`](generated/torch.func._random.normal_.html#torch.func._random.normal_) | Fill `result` in-place with normal random values from a PRNG key. |
| [`randint`](generated/torch.func._random.randint.html#torch.func._random.randint) | Generate uniform random integers in `[low, high)` from a PRNG key. |
| [`randint_`](generated/torch.func._random.randint_.html#torch.func._random.randint_) | Fill `result` in-place with uniform random integers in `[low, high)`. |
| [`bits`](generated/torch.func._random.bits.html#torch.func._random.bits) | Generate raw random bits from a PRNG key. |
| [`bits_`](generated/torch.func._random.bits_.html#torch.func._random.bits_) | Fill `result` in-place with raw random bits from a PRNG key. |