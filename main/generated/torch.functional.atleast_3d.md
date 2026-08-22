# torch.functional.atleast_3d

torch.functional.atleast_3d(**tensors*)[[source]](https://github.com/pytorch/pytorch/blob/f744a6b99cda942b3dd232f56c0ebf413660c13f/torch/functional.py#L1622)

Returns a 3-dimensional view of each input tensor with zero dimensions.
Input tensors with three or more dimensions are returned as-is.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)*or**sequence**of**Tensors*) - tensor(s) to be converted to at least 3-dimensional.

Returns:

output (Tensor or tuple of Tensors)

Example

```
>>> x = torch.tensor(0.5)
>>> x
tensor(0.5000)
>>> torch.atleast_3d(x)
tensor([[[0.5000]]])
>>> y = torch.arange(4).view(2, 2)
>>> y
tensor([[0, 1],
 [2, 3]])
>>> torch.atleast_3d(y)
tensor([[[0],
 [1]],

 [[2],
 [3]]])
>>> x = torch.tensor(1).view(1, 1, 1)
>>> x
tensor([[[1]]])
>>> torch.atleast_3d(x)
tensor([[[1]]])
>>> x = torch.tensor(0.5)
>>> y = torch.tensor(1.0)
>>> torch.atleast_3d((x, y))
(tensor([[[0.5000]]]), tensor([[[1.]]]))
>>> torch.atleast_3d()
()
```