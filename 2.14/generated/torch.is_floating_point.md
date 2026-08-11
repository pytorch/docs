# torch.is_floating_point

torch.is_floating_point(*input: [Tensor](../tensors.html#torch.Tensor)*) → [bool](https://docs.python.org/3/library/functions.html#bool)

Returns True if the data type of `input` is a floating point data type i.e.,
one of `torch.float64`, `torch.float32`, `torch.float16`, and `torch.bfloat16`.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Example:

```
>>> torch.is_floating_point(torch.tensor([1.0, 2.0, 3.0]))
True
>>> torch.is_floating_point(torch.tensor([1, 2, 3], dtype=torch.int32))
False
>>> torch.is_floating_point(torch.tensor([1.0, 2.0, 3.0], dtype=torch.float16))
True
>>> torch.is_floating_point(torch.tensor([1, 2, 3], dtype=torch.complex64))
False
```