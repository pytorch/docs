# torch.stack

torch.stack(*tensors*, *dim=0*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Concatenates a sequence of tensors along a new dimension.

All tensors need to be of the same size.

See also

[`torch.cat()`](torch.cat.html#torch.cat) concatenates the given sequence along an existing dimension.

Parameters:

- **tensors** (*sequence**of**Tensors*) - sequence of tensors to concatenate
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - dimension to insert. Has to be between 0 and the number
of dimensions of concatenated tensors (inclusive). Default: 0

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> x = torch.randn(2, 3)
>>> x
tensor([[ 0.3367, 0.1288, 0.2345],
 [ 0.2303, -1.1229, -0.1863]])
>>> torch.stack((x, x)) # same as torch.stack((x, x), dim=0)
tensor([[[ 0.3367, 0.1288, 0.2345],
 [ 0.2303, -1.1229, -0.1863]],

 [[ 0.3367, 0.1288, 0.2345],
 [ 0.2303, -1.1229, -0.1863]]])
>>> torch.stack((x, x)).size()
torch.Size([2, 2, 3])
>>> torch.stack((x, x), dim=1)
tensor([[[ 0.3367, 0.1288, 0.2345],
 [ 0.3367, 0.1288, 0.2345]],

 [[ 0.2303, -1.1229, -0.1863],
 [ 0.2303, -1.1229, -0.1863]]])
>>> torch.stack((x, x), dim=2)
tensor([[[ 0.3367, 0.3367],
 [ 0.1288, 0.1288],
 [ 0.2345, 0.2345]],

 [[ 0.2303, 0.2303],
 [-1.1229, -1.1229],
 [-0.1863, -0.1863]]])
>>> torch.stack((x, x), dim=-1)
tensor([[[ 0.3367, 0.3367],
 [ 0.1288, 0.1288],
 [ 0.2345, 0.2345]],

 [[ 0.2303, 0.2303],
 [-1.1229, -1.1229],
 [-0.1863, -0.1863]]])
```