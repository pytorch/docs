# torch.rad2deg

torch.rad2deg(*input: [Tensor](../tensors.html#torch.Tensor)*, ***, *out: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with each of the elements of `input`
converted from angles in radians to degrees.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.tensor([[3.142, -3.142], [6.283, -6.283], [1.570, -1.570]])
>>> torch.rad2deg(a)
tensor([[ 180.0233, -180.0233],
 [ 359.9894, -359.9894],
 [ 89.9544, -89.9544]])
```