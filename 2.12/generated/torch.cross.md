# torch.cross

torch.cross(*input*, *other*, *dim=None*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns the cross product of vectors in dimension `dim` of `input`
and `other`.

Supports input of float, double, cfloat and cdouble dtypes. Also supports batches
of vectors, for which it computes the product along the dimension `dim`.
In this case, the output has the same batch dimensions as the inputs.

Warning

If `dim` is not given, it defaults to the first dimension found
with the size 3. Note that this might be unexpected.

This behavior is deprecated and will be changed to match that of [`torch.linalg.cross()`](torch.linalg.cross.html#torch.linalg.cross)
in a future release.

See also

[`torch.linalg.cross()`](torch.linalg.cross.html#torch.linalg.cross) which has dim=-1 as default.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - the second input tensor
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the dimension to take the cross-product in.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(4, 3)
>>> a
tensor([[-0.3956, 1.1455, 1.6895],
 [-0.5849, 1.3672, 0.3599],
 [-1.1626, 0.7180, -0.0521],
 [-0.1339, 0.9902, -2.0225]])
>>> b = torch.randn(4, 3)
>>> b
tensor([[-0.0257, -1.4725, -1.2251],
 [-1.1479, -0.7005, -1.9757],
 [-1.3904, 0.3726, -1.1836],
 [-0.9688, -0.7153, 0.2159]])
>>> torch.cross(a, b, dim=1)
tensor([[ 1.0844, -0.5281, 0.6120],
 [-2.4490, -1.5687, 1.9792],
 [-0.8304, -1.3037, 0.5650],
 [-1.2329, 1.9883, 1.0551]])
>>> torch.cross(a, b)
tensor([[ 1.0844, -0.5281, 0.6120],
 [-2.4490, -1.5687, 1.9792],
 [-0.8304, -1.3037, 0.5650],
 [-1.2329, 1.9883, 1.0551]])
```