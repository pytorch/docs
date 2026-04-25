# torch.gcd

torch.gcd(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the element-wise greatest common divisor (GCD) of `input` and `other`.

Both `input` and `other` must have integer types.

Note

This defines gcd(0,0)=0gcd(0, 0) = 0gcd(0,0)=0.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - the second input tensor

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.tensor([5, 10, 15])
>>> b = torch.tensor([3, 4, 5])
>>> torch.gcd(a, b)
tensor([1, 2, 5])
>>> c = torch.tensor([3])
>>> torch.gcd(a, c)
tensor([1, 1, 3])
```