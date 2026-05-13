# torch.frexp

torch.frexp(*input*, ***, *out=None) -> (Tensor mantissa*, *Tensor exponent*)

Decomposes `input` into mantissa and exponent tensors
such that input=mantissa×2exponent\text{input} = \text{mantissa} \times 2^{\text{exponent}}input=mantissa×2exponent.

The range of mantissa is the open interval (-1, 1).

Supports float inputs.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor

Keyword Arguments:

**out** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - the output tensors

Example:

```
>>> x = torch.arange(9.)
>>> mantissa, exponent = torch.frexp(x)
>>> mantissa
tensor([0.0000, 0.5000, 0.5000, 0.7500, 0.5000, 0.6250, 0.7500, 0.8750, 0.5000])
>>> exponent
tensor([0, 1, 2, 2, 3, 3, 3, 3, 4], dtype=torch.int32)
>>> torch.ldexp(mantissa, exponent)
tensor([0., 1., 2., 3., 4., 5., 6., 7., 8.])
```