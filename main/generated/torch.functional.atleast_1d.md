# torch.functional.atleast_1d

torch.functional.atleast_1d(**tensors*)[[source]](https://github.com/pytorch/pytorch/blob/b14e6fb508b03fc0a98fefe9b0750ba0d63500da/torch/functional.py#L1495)

Returns a 1-dimensional view of each input tensor with zero dimensions.
Input tensors with one or more dimensions are returned as-is.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)*or**sequence**of**Tensors*) - tensor(s) to be converted to at least 1-dimensional.

Returns:

output (Tensor or tuple of Tensors)

Example:

```
>>> x = torch.arange(2)
>>> x
tensor([0, 1])
>>> torch.atleast_1d(x)
tensor([0, 1])
>>> x = torch.tensor(1.)
>>> x
tensor(1.)
>>> torch.atleast_1d(x)
tensor([1.])
>>> x = torch.tensor(0.5)
>>> y = torch.tensor(1.)
>>> torch.atleast_1d((x, y))
(tensor([0.5000]), tensor([1.]))
>>> torch.atleast_1d()
()
```