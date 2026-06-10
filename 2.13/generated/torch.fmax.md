# torch.fmax

torch.fmax(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the element-wise maximum of `input` and `other`.

This is like [`torch.maximum()`](torch.maximum.html#torch.maximum) except it handles NaNs differently:
if exactly one of the two elements being compared is a NaN then the non-NaN element is taken as the maximum.
Only if both elements are NaN is NaN propagated.

This function is a wrapper around C++'s `std::fmax` and is similar to NumPy's `fmax` function.

Supports [broadcasting to a common shape](../notes/broadcasting.html#broadcasting-semantics),
[type promotion](../tensor_attributes.html#type-promotion-doc), and integer and floating-point inputs.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - the second input tensor

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.tensor([9.7, float('nan'), 3.1, float('nan')])
>>> b = torch.tensor([-2.2, 0.5, float('nan'), float('nan')])
>>> torch.fmax(a, b)
tensor([9.7000, 0.5000, 3.1000, nan])
```