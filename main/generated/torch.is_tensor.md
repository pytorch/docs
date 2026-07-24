# torch.is_tensor

torch.is_tensor(*obj*, */*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/__init__.py#L1615)

Returns True if obj is a PyTorch tensor.

Parameters:

**obj** ([*object*](https://docs.python.org/3/library/functions.html#object)) - Object to test

Return type:

*TypeIs*[[*Tensor*](../tensors.html#torch.Tensor)]

Example:

```
>>> x = torch.tensor([1, 2, 3])
>>> torch.is_tensor(x)
True
```