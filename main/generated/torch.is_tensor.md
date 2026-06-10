# torch.is_tensor

torch.is_tensor(*obj*, */*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/__init__.py#L1161)

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