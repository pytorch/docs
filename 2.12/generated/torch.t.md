# torch.t

torch.t(*input*) → [Tensor](../tensors.html#torch.Tensor)

Expects `input` to be <= 2-D tensor and transposes dimensions 0
and 1.

0-D and 1-D tensors are returned as is. When input is a 2-D tensor this
is equivalent to `transpose(input, 0, 1)`.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Example:

```
>>> x = torch.randn(())
>>> x
tensor(0.1995)
>>> torch.t(x)
tensor(0.1995)
>>> x = torch.randn(3)
>>> x
tensor([ 2.4320, -0.4608, 0.7702])
>>> torch.t(x)
tensor([ 2.4320, -0.4608, 0.7702])
>>> x = torch.randn(2, 3)
>>> x
tensor([[ 0.4875, 0.9158, -0.5872],
 [ 0.3938, -0.6929, 0.6932]])
>>> torch.t(x)
tensor([[ 0.4875, 0.3938],
 [ 0.9158, -0.6929],
 [-0.5872, 0.6932]])
```

See also [`torch.transpose()`](torch.transpose.html#torch.transpose).