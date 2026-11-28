# torch.is_tensor

torch.is_tensor(*obj*, */*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/__init__.py#L1554)

Returns True if obj is a PyTorch tensor.

Parameters:

**obj** ([*object*](https://docs.python.org/3/builtins/functions.html#object)) - Object to test

Return type:

*TypeIs*[[*Tensor*](../tensors.html#torch.Tensor)]

Example:

```
>>> x = torch.tensor([1, 2, 3])
>>> torch.is_tensor(x)
True
```