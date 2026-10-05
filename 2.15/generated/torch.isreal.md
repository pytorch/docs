# torch.isreal

torch.isreal(*input*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with boolean elements representing if each element of `input` is real-valued or not.
All real-valued types are considered real. Complex values are considered real when their imaginary part is 0.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Returns:

A boolean tensor that is True where `input` is real and False elsewhere

Example:

```
>>> torch.isreal(torch.tensor([1, 1+1j, 2+0j]))
tensor([True, False, True])
```