# torch.positive

torch.positive(*input*) → [Tensor](../tensors.html#torch.Tensor)

Returns `input`.
Throws a runtime error if `input` is a bool tensor.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Example:

```
>>> t = torch.randn(5)
>>> t
tensor([ 0.0090, -0.2262, -0.0682, -0.2866, 0.3940])
>>> torch.positive(t)
tensor([ 0.0090, -0.2262, -0.0682, -0.2866, 0.3940])
```