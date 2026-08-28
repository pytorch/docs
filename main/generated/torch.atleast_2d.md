# torch.atleast_2d

torch.atleast_2d(**tensors*)[[source]](https://github.com/pytorch/pytorch/blob/7e9fd4e82a01d43fc8afdf03258cf85ee22db2ea/torch/functional.py#L1582)

Returns a 2-dimensional view of each input tensor with zero dimensions.
Input tensors with two or more dimensions are returned as-is.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)*or**sequence**of**Tensors*) - tensor(s) to be converted to at least 2-dimensional.

Returns:

output (Tensor or tuple of Tensors)

Example:

```
>>> x = torch.tensor(1.)
>>> x
tensor(1.)
>>> torch.atleast_2d(x)
tensor([[1.]])
>>> x = torch.arange(4).view(2, 2)
>>> x
tensor([[0, 1],
 [2, 3]])
>>> torch.atleast_2d(x)
tensor([[0, 1],
 [2, 3]])
>>> x = torch.tensor(0.5)
>>> y = torch.tensor(1.)
>>> torch.atleast_2d((x, y))
(tensor([[0.5000]]), tensor([[1.]]))
>>> torch.atleast_2d()
()
```