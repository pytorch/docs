# torch.fmod

torch.fmod(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Applies C++'s [std::fmod](https://en.cppreference.com/w/cpp/numeric/math/fmod) entrywise.
The result has the same sign as the dividend `input` and its absolute value
is less than that of `other`.

This function may be defined in terms of [`torch.div()`](torch.div.html#torch.div) as

```
torch.fmod(a, b) == a - a.div(b, rounding_mode="trunc") * b
```

Supports [broadcasting to a common shape](../notes/broadcasting.html#broadcasting-semantics),
[type promotion](../tensor_attributes.html#type-promotion-doc), and integer and float inputs.

Note

When the divisor is zero, returns `NaN` for floating point dtypes
on both CPU and GPU; raises `RuntimeError` for integer division by
zero on CPU; Integer division by zero on GPU may return any value.

Note

Complex inputs are not supported. In some cases, it is not mathematically
possible to satisfy the definition of a modulo operation with complex numbers.

See also

[`torch.remainder()`](torch.remainder.html#torch.remainder) which implements Python's modulus operator.
This one is defined using division rounding down the result.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the dividend
- **other** ([*Tensor*](../tensors.html#torch.Tensor)*or**Scalar*) - the divisor

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.fmod(torch.tensor([-3., -2, -1, 1, 2, 3]), 2)
tensor([-1., -0., -1., 1., 0., 1.])
>>> torch.fmod(torch.tensor([1, 2, 3, 4, 5]), -1.5)
tensor([1.0000, 0.5000, 0.0000, 1.0000, 0.5000])
```