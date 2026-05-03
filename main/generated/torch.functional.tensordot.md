# torch.functional.tensordot

torch.functional.tensordot(*a*, *b*, *dims=2*, *out=None*)[[source]](https://github.com/pytorch/pytorch/blob/474b9649dd111ae9b0c31728da812cc3dda2c4ae/torch/functional.py#L1257)

Returns a contraction of a and b over multiple dimensions.

`tensordot` implements a generalized matrix product.

Parameters:

- **a** ([*Tensor*](../tensors.html#torch.Tensor)) - Left tensor to contract
- **b** ([*Tensor*](../tensors.html#torch.Tensor)) - Right tensor to contract
- **dims** ([*int*](https://docs.python.org/3/library/functions.html#int)*or**Tuple**[**List**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**List**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**] or**List**[**List**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**]**containing two lists**or*[*Tensor*](../tensors.html#torch.Tensor)) - number of dimensions to
contract or explicit lists of dimensions for `a` and
`b` respectively

When called with a non-negative integer argument `dims` = ddd, and
the number of dimensions of `a` and `b` is mmm and nnn,
respectively, [`tensordot()`](torch.tensordot.html#torch.tensordot) computes the tensor rrr of shape
`a.shape[:-dims] + b.shape[dims:]` given by:

ri1,...,im−d,j1,...,jn−d=∑k1,...,kdai1,...,im−d,k1,...,kd×bk1,...,kd,j1,...,jn−d.r_{i_1,...,i_{m-d}, j_1,...,j_{n-d}}
 = \sum_{k_1,...,k_d} a_{i_1,...,i_{m-d},k_1,...,k_d} \times b_{k_1,...,k_d, j_1,...,j_{n-d}}.

ri1​,...,im−d​,j1​,...,jn−d​​=k1​,...,kd​∑​ai1​,...,im−d​,k1​,...,kd​​×bk1​,...,kd​,j1​,...,jn−d​​.

When called with `dims` of the list form, the given dimensions will be contracted
in place of the last ddd of `a` and the first ddd of bbb. The sizes
in these dimensions must match, but [`tensordot()`](torch.tensordot.html#torch.tensordot) will deal with broadcasted
dimensions.

Examples:

```
>>> a = torch.arange(60.).reshape(3, 4, 5)
>>> b = torch.arange(24.).reshape(4, 3, 2)
>>> torch.tensordot(a, b, dims=([1, 0], [0, 1]))
tensor([[4400., 4730.],
 [4532., 4874.],
 [4664., 5018.],
 [4796., 5162.],
 [4928., 5306.]])

>>> a = torch.randn(3, 4, 5, device='cuda')
>>> b = torch.randn(4, 5, 6, device='cuda')
>>> c = torch.tensordot(a, b, dims=2).cpu()
tensor([[ 8.3504, -2.5436, 6.2922, 2.7556, -1.0732, 3.2741],
 [ 3.3161, 0.0704, 5.0187, -0.4079, -4.3126, 4.8744],
 [ 0.8223, 3.9445, 3.2168, -0.2400, 3.4117, 1.7780]])

>>> a = torch.randn(3, 5, 4, 6)
>>> b = torch.randn(6, 4, 5, 3)
>>> torch.tensordot(a, b, dims=([2, 1, 3], [1, 2, 0]))
tensor([[ 7.7193, -2.4867, -10.3204],
 [ 1.5513, -14.4737, -6.5113],
 [ -0.2850, 4.2573, -3.5997]])
```