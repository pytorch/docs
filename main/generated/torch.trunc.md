# torch.trunc

torch.trunc(*input*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the truncated integer values of
the elements of `input`.

For integer inputs, follows the array-api convention of returning a
copy of the input tensor.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(4)
>>> a
tensor([ 3.4742, 0.5466, -0.8008, -0.9079])
>>> torch.trunc(a)
tensor([ 3., 0., -0., -0.])
```