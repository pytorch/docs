# torch.linalg.vecdot

torch.linalg.vecdot(*x*, *y*, ***, *dim=-1*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/linalg/__init__.py#L3091)

Computes the dot product of two batches of vectors along a dimension.

In symbols, this function computes

∑i=1nxi‾yi.\sum_{i=1}^n \overline{x_i}y_i.i=1∑n​xi​​yi​.

over the dimension `dim` where xi‾\overline{x_i}xi​​ denotes the conjugate for complex
vectors, and it is the identity for real vectors.

Supports input of half, bfloat16, float, double, cfloat, cdouble and integral dtypes.
It also supports broadcasting.

Parameters:

- **x** ([*Tensor*](../tensors.html#torch.Tensor)) - first batch of vectors of shape (*, n).
- **y** ([*Tensor*](../tensors.html#torch.Tensor)) - second batch of vectors of shape (*, n).

Keyword Arguments:

- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Dimension along which to compute the dot product. Default: -1.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - output tensor. Ignored if None. Default: None.

Examples:

```
>>> v1 = torch.randn(3, 2)
>>> v2 = torch.randn(3, 2)
>>> linalg.vecdot(v1, v2)
tensor([ 0.3223, 0.2815, -0.1944])
>>> torch.vdot(v1[0], v2[0])
tensor(0.3223)
```