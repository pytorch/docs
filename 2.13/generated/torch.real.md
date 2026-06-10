# torch.real

torch.real(*input*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor containing real values of the `self` tensor.
The returned tensor and `self` share the same underlying storage.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Example:

```
>>> x=torch.randn(4, dtype=torch.cfloat)
>>> x
tensor([(0.3100+0.3553j), (-0.5445-0.7896j), (-1.6492-0.0633j), (-0.0638-0.8119j)])
>>> x.real
tensor([ 0.3100, -0.5445, -1.6492, -0.0638])
```