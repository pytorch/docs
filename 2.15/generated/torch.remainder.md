# torch.remainder

torch.remainder(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes
[Python's modulus operation](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations)
entrywise. The result has the same sign as the divisor `other` and its absolute value
is less than that of `other`.

It may also be defined in terms of [`torch.div()`](torch.div.html#torch.div) as

```
torch.remainder(a, b) == a - a.div(b, rounding_mode="floor") * b
```

Supports [broadcasting to a common shape](../notes/broadcasting.html#broadcasting-semantics),
[type promotion](../tensor_attributes.html#type-promotion-doc), and integer and float inputs.

Note

Complex inputs are not supported. In some cases, it is not mathematically
possible to satisfy the definition of a modulo operation with complex numbers.
See [`torch.fmod()`](torch.fmod.html#torch.fmod) for how division by zero is handled.

See also

[`torch.fmod()`](torch.fmod.html#torch.fmod) which implements C++'s [std::fmod](https://en.cppreference.com/w/cpp/numeric/math/fmod).
This one is defined in terms of division rounding towards zero.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)*or**Scalar*) - the dividend
- **other** ([*Tensor*](../tensors.html#torch.Tensor)*or**Scalar*) - the divisor

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.remainder(torch.tensor([-3., -2, -1, 1, 2, 3]), 2)
tensor([ 1., 0., 1., 1., 0., 1.])
>>> torch.remainder(torch.tensor([1, 2, 3, 4, 5]), -1.5)
tensor([ -0.5000, -1.0000, 0.0000, -0.5000, -1.0000 ])
```