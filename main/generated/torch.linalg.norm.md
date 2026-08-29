# torch.linalg.norm

torch.linalg.norm(*input*, *ord=None*, *dim=None*, *keepdim=False*, ***, *out=None*, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/fe3f518c806b6f1fb8acc283135e5414b8606887/torch/linalg/__init__.py#L1353)

Computes a vector or matrix norm.

Supports input of float, double, cfloat and cdouble dtypes.

Whether this function computes a vector or matrix norm is determined as follows:

- If `dim` is an int, the vector norm will be computed.
- If `dim` is a 2-tuple, the matrix norm will be computed.
- If `dim`= None and `ord`= None,
`input` will be flattened to 1D and the 2-norm of the resulting vector will be computed.
- If `dim`= None and `ord` != None, `input` must be 1D or 2D.

`ord` defines the norm that is computed. The following norms are supported:

| `ord` | norm for matrices | norm for vectors |
| --- | --- | --- |
| None (default) | Frobenius norm | 2-norm (see below) |
| 'fro' | Frobenius norm | - not supported - |
| 'nuc' | nuclear norm | - not supported - |
| inf | max(sum(abs(x), dim=1)) | max(abs(x)) |
| -inf | min(sum(abs(x), dim=1)) | min(abs(x)) |
| 0 | - not supported - | sum(x != 0) |
| 1 | max(sum(abs(x), dim=0)) | as below |
| -1 | min(sum(abs(x), dim=0)) | as below |
| 2 | largest [singular value](https://en.wikipedia.org/wiki/Singular_value_decomposition#Singular_values,_singular_vectors,_and_their_relation_to_the_SVD) | as below |
| -2 | smallest [singular value](https://en.wikipedia.org/wiki/Singular_value_decomposition#Singular_values,_singular_vectors,_and_their_relation_to_the_SVD) | as below |
| other int or float | - not supported - | sum(abs(x)^{ord})^{(1 / ord)} |

where inf refers to float('inf'), NumPy's inf object, or any equivalent object.

See also

[`torch.linalg.vector_norm()`](torch.linalg.vector_norm.html#torch.linalg.vector_norm) computes a vector norm.

[`torch.linalg.matrix_norm()`](torch.linalg.matrix_norm.html#torch.linalg.matrix_norm) computes a matrix norm.

The above functions are often clearer and more flexible than using `torch.linalg.norm()`.
For example, torch.linalg.norm(input, ord=1, dim=(0, 1)) always
computes a matrix norm, but with torch.linalg.vector_norm(input, ord=1, dim=(0, 1)) it is possible
to compute a vector norm over the two dimensions.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, n) or (*, m, n) where * is zero or more batch dimensions
- **ord** ([*int*](https://docs.python.org/3/library/functions.html#int)*,*[*float*](https://docs.python.org/3/library/functions.html#float)*,**inf**,**-inf**,**'fro'**,**'nuc'**,**optional*) - order of norm. Default: None
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - dimensions over which to compute
the vector or matrix norm. See above for the behavior when `dim`= None.
Default: None
- **keepdim** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set to True, the reduced dimensions are retained
in the result as dimensions with size one. Default: False

Keyword Arguments:

- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - output tensor. Ignored if None. Default: None.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - If specified `x` is cast to
`dtype` prior to doing the accumulation. Default: None

Returns:

A real-valued tensor, even when `input` is complex.

Examples:

```
>>> from torch import linalg as LA
>>> a = torch.arange(9, dtype=torch.float) - 4
>>> a
tensor([-4., -3., -2., -1., 0., 1., 2., 3., 4.])
>>> B = a.reshape((3, 3))
>>> B
tensor([[-4., -3., -2.],
 [-1., 0., 1.],
 [ 2., 3., 4.]])

>>> LA.norm(a)
tensor(7.7460)
>>> LA.norm(B)
tensor(7.7460)
>>> LA.norm(B, 'fro')
tensor(7.7460)
>>> LA.norm(a, float('inf'))
tensor(4.)
>>> LA.norm(B, float('inf'))
tensor(9.)
>>> LA.norm(a, -float('inf'))
tensor(0.)
>>> LA.norm(B, -float('inf'))
tensor(2.)

>>> LA.norm(a, 1)
tensor(20.)
>>> LA.norm(B, 1)
tensor(7.)
>>> LA.norm(a, -1)
tensor(0.)
>>> LA.norm(B, -1)
tensor(6.)
>>> LA.norm(a, 2)
tensor(7.7460)
>>> LA.norm(B, 2)
tensor(7.3485)

>>> LA.norm(a, -2)
tensor(0.)
>>> LA.norm(B.double(), -2)
tensor(1.8570e-16, dtype=torch.float64)
>>> LA.norm(a, 3)
tensor(5.8480)
>>> LA.norm(a, -3)
tensor(0.)
```

Using the `dim` argument to compute vector norms:

```
>>> c = torch.tensor([[1., 2., 3.],
... [-1, 1, 4]])
>>> LA.norm(c, dim=0)
tensor([1.4142, 2.2361, 5.0000])
>>> LA.norm(c, dim=1)
tensor([3.7417, 4.2426])
>>> LA.norm(c, ord=1, dim=1)
tensor([6., 6.])
```

Using the `dim` argument to compute matrix norms:

```
>>> A = torch.arange(8, dtype=torch.float).reshape(2, 2, 2)
>>> LA.norm(A, dim=(1,2))
tensor([ 3.7417, 11.2250])
>>> LA.norm(A[0, :, :]), LA.norm(A[1, :, :])
(tensor(3.7417), tensor(11.2250))
```