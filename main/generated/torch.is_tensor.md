# torch.is_tensor

torch.is_tensor(*obj*, */*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/__init__.py#L1534)

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