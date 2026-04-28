# torch.deg2rad

torch.deg2rad(*input*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with each of the elements of `input`
converted from angles in degrees to radians.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.tensor([[180.0, -180.0], [360.0, -360.0], [90.0, -90.0]])
>>> torch.deg2rad(a)
tensor([[ 3.1416, -3.1416],
 [ 6.2832, -6.2832],
 [ 1.5708, -1.5708]])
```