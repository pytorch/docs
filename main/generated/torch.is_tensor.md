# torch.is_tensor

torch.is_tensor(*obj*, */*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/__init__.py#L1615)

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