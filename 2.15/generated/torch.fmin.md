# torch.fmin

torch.fmin(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the element-wise minimum of `input` and `other`.

This is like [`torch.minimum()`](torch.minimum.html#torch.minimum) except it handles NaNs differently:
if exactly one of the two elements being compared is a NaN then the non-NaN element is taken as the minimum.
Only if both elements are NaN is NaN propagated.

This function is a wrapper around C++'s `std::fmin` and is similar to NumPy's `fmin` function.

Supports [broadcasting to a common shape](../notes/broadcasting.html#broadcasting-semantics),
[type promotion](../tensor_attributes.html#type-promotion-doc), and integer and floating-point inputs.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - the second input tensor

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.tensor([2.2, float('nan'), 2.1, float('nan')])
>>> b = torch.tensor([-9.3, 0.1, float('nan'), float('nan')])
>>> torch.fmin(a, b)
tensor([-9.3000, 0.1000, 2.1000, nan])
```