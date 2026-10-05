# torch.log

torch.log(*input*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the natural logarithm of the elements
of `input`.

yi=log⁡e(xi)y_{i} = \log_{e} (x_{i})

yi​=loge​(xi​)
Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.rand(5) * 5
>>> a
tensor([4.7767, 4.3234, 1.2156, 0.2411, 4.5739])
>>> torch.log(a)
tensor([ 1.5637, 1.4640, 0.1952, -1.4226, 1.5204])
```