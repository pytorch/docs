# torch.linalg.cross

torch.linalg.cross(*input*, *other*, ***, *dim=-1*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/ab02f71479d3b0fb41d5b722bbe1943340f2022b/torch/linalg/__init__.py#L22)

Computes the cross product of two 3-dimensional vectors.

Supports input of float, double, cfloat and cdouble dtypes. Also supports batches
of vectors, for which it computes the product along the dimension `dim`.
It broadcasts over the batch dimensions.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the first input tensor.
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - the second input tensor.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the dimension along which to take the cross-product. Default: -1.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor. Ignored if None. Default: None.

Example

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
>>> torch.linalg.cross(a, b)
tensor([[ 1.0844, -0.5281, 0.6120],
 [-2.4490, -1.5687, 1.9792],
 [-0.8304, -1.3037, 0.5650],
 [-1.2329, 1.9883, 1.0551]])
>>> a = torch.randn(1, 3) # a is broadcast to match shape of b
>>> a
tensor([[-0.9941, -0.5132, 0.5681]])
>>> torch.linalg.cross(a, b)
tensor([[ 1.4653, -1.2325, 1.4507],
 [ 1.4119, -2.6163, 0.1073],
 [ 0.3957, -1.9666, -1.0840],
 [ 0.2956, -0.3357, 0.2139]])
```