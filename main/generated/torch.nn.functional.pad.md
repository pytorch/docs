# torch.nn.functional.pad

torch.nn.functional.pad(*input*, *pad*, *mode='constant'*, *value=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/d4258aa05fc98e7852a6c78350d44e3fa7bdb2ab/torch/nn/functional.py#L5773)

Pads tensor.

Padding size:

The padding size by which to pad some dimensions of `input`
are described starting from the last dimension and moving forward.
⌊len(pad)2⌋\left\lfloor\frac{\text{len(pad)}}{2}\right\rfloor⌊2len(pad)​⌋ dimensions
of `input` will be padded.
For example, to pad only the last dimension of the input tensor, then
`pad` has the form
(padding_left,padding_right)(\text{padding\_left}, \text{padding\_right})(padding_left,padding_right);
to pad the last 2 dimensions of the input tensor, then use
(padding_left,padding_right,(\text{padding\_left}, \text{padding\_right},(padding_left,padding_right,
padding_top,padding_bottom)\text{padding\_top}, \text{padding\_bottom})padding_top,padding_bottom);
to pad the last 3 dimensions, use
(padding_left,padding_right,(\text{padding\_left}, \text{padding\_right},(padding_left,padding_right,
padding_top,padding_bottom\text{padding\_top}, \text{padding\_bottom}padding_top,padding_bottom
padding_front,padding_back)\text{padding\_front}, \text{padding\_back})padding_front,padding_back).

Padding mode:

See [`torch.nn.CircularPad2d`](torch.nn.CircularPad2d.html#torch.nn.CircularPad2d), [`torch.nn.ConstantPad2d`](torch.nn.ConstantPad2d.html#torch.nn.ConstantPad2d),
[`torch.nn.ReflectionPad2d`](torch.nn.ReflectionPad2d.html#torch.nn.ReflectionPad2d), and [`torch.nn.ReplicationPad2d`](torch.nn.ReplicationPad2d.html#torch.nn.ReplicationPad2d)
for concrete examples on how each of the padding modes works. Constant
padding is implemented for arbitrary dimensions. Circular, replicate and
reflection padding are implemented for padding the last 3 dimensions of a
4D or 5D input tensor, the last 2 dimensions of a 3D or 4D input tensor,
or the last dimension of a 2D or 3D input tensor.

Note

When using the CUDA backend, this operation may induce nondeterministic
behaviour in its backward pass that is not easily switched off.
Please see the notes on [Reproducibility](../notes/randomness.html) for background.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - N-dimensional tensor
- **pad** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) - m-elements tuple, where
m2≤\frac{m}{2} \leq2m​≤ input dimensions and mmm is even.
- **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - `'constant'`, `'reflect'`, `'replicate'` or `'circular'`.
Default: `'constant'`
- **value** ([*float*](https://docs.python.org/3/library/functions.html#float)*|**None*) - fill value for `'constant'` padding. Default: `0`

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Examples:

```
>>> t4d = torch.empty(3, 3, 4, 2)
>>> p1d = (1, 1) # pad last dim by 1 on each side
>>> out = F.pad(t4d, p1d, "constant", 0) # effectively zero padding
>>> print(out.size())
torch.Size([3, 3, 4, 4])
>>> p2d = (1, 1, 2, 2) # pad last dim by (1, 1) and 2nd to last by (2, 2)
>>> out = F.pad(t4d, p2d, "constant", 0)
>>> print(out.size())
torch.Size([3, 3, 8, 4])
>>> t4d = torch.empty(3, 3, 4, 2)
>>> p3d = (0, 1, 2, 1, 3, 3) # pad by (0, 1), (2, 1), and (3, 3)
>>> out = F.pad(t4d, p3d, "constant", 0)
>>> print(out.size())
torch.Size([3, 9, 7, 3])
```