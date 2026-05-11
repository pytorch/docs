# torch.segment_reduce

torch.segment_reduce(*data: [Tensor](../tensors.html#torch.Tensor)*, *reduce: [str](https://docs.python.org/3/library/stdtypes.html#str)*, ***, *lengths: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *indices: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *offsets: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *axis: _int = 0*, *unsafe: _bool = False*, *initial: Number | _complex | [None](https://docs.python.org/3/library/constants.html#None) = None*) → [Tensor](../tensors.html#torch.Tensor)

Perform a segment reduction operation on the input tensor along the specified axis.

Parameters:

- **data** ([*Tensor*](../tensors.html#torch.Tensor)) - The input tensor on which the segment reduction operation will be performed.
- **reduce** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The type of reduction operation. Supported values are `sum`, `mean`, `max`, `min`, `prod`.

Keyword Arguments:

- **lengths** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - Length of each segment. Default: `None`.
- **offsets** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - Offset of each segment. Default: `None`.
- **axis** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The axis perform reduction. Default: `0`.
- **unsafe** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Skip validation If True. Default: `False`.
- **initial** (*Number**,**optional*) - The initial value for the reduction operation. Default: `None`.

Example:

```
>>> data = torch.tensor([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]], dtype=torch.float32, device='cuda')
>>> lengths = torch.tensor([2, 1], device='cuda')
>>> torch.segment_reduce(data, 'max', lengths=lengths)
tensor([[ 5., 6., 7., 8.],
 [ 9., 10., 11., 12.]], device='cuda:0')
```