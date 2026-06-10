# torch.movedim

torch.movedim(*input*, *source*, *destination*) → [Tensor](../tensors.html#torch.Tensor)

Moves the dimension(s) of `input` at the position(s) in `source`
to the position(s) in `destination`.

Other dimensions of `input` that are not explicitly moved remain in
their original order and appear at the positions not specified in `destination`.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **source** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**ints*) - Original positions of the dims to move. These must be unique.
- **destination** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**ints*) - Destination positions for each of the original dims. These must also be unique.

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
>>> torch.movedim(t, 1, 0).shape
torch.Size([2, 3, 1])
>>> torch.movedim(t, 1, 0)
tensor([[[-0.3362],
 [-0.9627],
 [ 0.5173]],

 [[-0.8437],
 [ 0.1727],
 [-0.1398]]])
>>> torch.movedim(t, (1, 2), (0, 1)).shape
torch.Size([2, 1, 3])
>>> torch.movedim(t, (1, 2), (0, 1))
tensor([[[-0.3362, -0.9627, 0.5173]],

 [[-0.8437, 0.1727, -0.1398]]])
```