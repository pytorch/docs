# torch.is_complex

torch.is_complex(*input: [Tensor](../tensors.html#torch.Tensor)*) → [bool](https://docs.python.org/3/library/functions.html#bool)

Returns True if the data type of `input` is a complex data type i.e.,
one of `torch.complex64`, and `torch.complex128`.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Example:

```
>>> torch.is_complex(torch.tensor([1, 2, 3], dtype=torch.complex64))
True
>>> torch.is_complex(torch.tensor([1, 2, 3], dtype=torch.complex128))
True
>>> torch.is_complex(torch.tensor([1, 2, 3], dtype=torch.int32))
False
>>> torch.is_complex(torch.tensor([1.0, 2.0, 3.0], dtype=torch.float16))
False
```