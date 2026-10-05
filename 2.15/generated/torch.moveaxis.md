# torch.moveaxis

torch.moveaxis(*input*, *source*, *destination*) → [Tensor](../tensors.html#torch.Tensor)

Alias for [`torch.movedim()`](torch.movedim.html#torch.movedim).

This function is equivalent to NumPy's moveaxis function.

Examples:

```
>>> t = torch.randn(3,2,1)
>>> t
tensor([[[-0.3362],
 [-0.8437]],

 [[-0.9627],
 [ 0.1727]],

 [[ 0.5173],
 [-0.1398]]])
>>> torch.moveaxis(t, 1, 0).shape
torch.Size([2, 3, 1])
>>> torch.moveaxis(t, 1, 0)
tensor([[[-0.3362],
 [-0.9627],
 [ 0.5173]],

 [[-0.8437],
 [ 0.1727],
 [-0.1398]]])
>>> torch.moveaxis(t, (1, 2), (0, 1)).shape
torch.Size([2, 1, 3])
>>> torch.moveaxis(t, (1, 2), (0, 1))
tensor([[[-0.3362, -0.9627, 0.5173]],

 [[-0.8437, 0.1727, -0.1398]]])
```