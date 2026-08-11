# torch.cat

torch.cat(*tensors*, *dim=0*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Concatenates the given sequence of tensors in `tensors` in the given dimension.
All tensors must either have the same shape (except in the concatenating
dimension) or be a 1-D empty tensor with size `(0,)`.

`torch.cat()` can be seen as an inverse operation for [`torch.split()`](torch.split.html#torch.split)
and [`torch.chunk()`](torch.chunk.html#torch.chunk).

`torch.cat()` can be best understood via examples.

See also

[`torch.stack()`](torch.stack.html#torch.stack) concatenates the given sequence along a new dimension.

Parameters:

- **tensors** (*sequence**of**Tensors*) - Non-empty tensors provided must have the same shape,
except in the cat dimension.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the dimension over which the tensors are concatenated

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> x = torch.randn(2, 3)
>>> x
tensor([[ 0.6580, -1.0969, -0.4614],
 [-0.1034, -0.5790, 0.1497]])
>>> torch.cat((x, x, x), 0)
tensor([[ 0.6580, -1.0969, -0.4614],
 [-0.1034, -0.5790, 0.1497],
 [ 0.6580, -1.0969, -0.4614],
 [-0.1034, -0.5790, 0.1497],
 [ 0.6580, -1.0969, -0.4614],
 [-0.1034, -0.5790, 0.1497]])
>>> torch.cat((x, x, x), 1)
tensor([[ 0.6580, -1.0969, -0.4614, 0.6580, -1.0969, -0.4614, 0.6580,
 -1.0969, -0.4614],
 [-0.1034, -0.5790, 0.1497, -0.1034, -0.5790, 0.1497, -0.1034,
 -0.5790, 0.1497]])
```