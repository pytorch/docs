# torch.Tensor.random_

Tensor.random_(*from=0*, *to=None*, ***, *generator=None*) → [Tensor](../tensors.html#torch.Tensor)

Fills `self` tensor with numbers sampled from the discrete uniform
distribution over `[from, to - 1]`. If not specified, the values are usually
only bounded by `self` tensor's data type. However, for floating point
types, if unspecified, range will be `[0, 2^mantissa]` to ensure that every
value is representable. For example, torch.tensor(1, dtype=torch.double).random_()
will be uniform in `[0, 2^53]`.