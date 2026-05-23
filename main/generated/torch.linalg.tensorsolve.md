# torch.linalg.tensorsolve

torch.linalg.tensorsolve(*A*, *B*, *dims=None*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/2f696474dc8fe614670ddb889f4ae1c75d1a11e6/torch/linalg/__init__.py#L2757)

Computes the solution X to the system torch.tensordot(A, X) = B.

If m is the product of the first `B`.ndim dimensions of `A` and
n is the product of the rest of the dimensions, this function expects m and n to be equal.

The returned tensor x satisfies
tensordot(`A`, x, dims=x.ndim) == `B`.
x has shape `A`[B.ndim:].

If `dims` is specified, `A` will be reshaped as

```
A = movedim(A, dims, range(len(dims) - A.ndim + 1, 0))
```

Supports inputs of float, double, cfloat and cdouble dtypes.

See also

[`torch.linalg.tensorinv()`](torch.linalg.tensorinv.html#torch.linalg.tensorinv) computes the multiplicative inverse of
[`torch.tensordot()`](torch.tensordot.html#torch.tensordot).

Parameters:

- **A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor to solve for. Its shape must satisfy
prod(`A`.shape[:`B`.ndim]) ==
prod(`A`.shape[`B`.ndim:]).
- **B** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape `A`.shape[:`B`.ndim].
- **dims** (*Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - dimensions of `A` to be moved.
If None, no dimensions are moved. Default: None.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - output tensor. Ignored if None. Default: None.

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - if the reshaped `A`.view(m, m) with m as above is not
 invertible or the product of the first `ind` dimensions is not equal
 to the product of the rest of the dimensions.

Examples:

```
>>> A = torch.eye(2 * 3 * 4).reshape((2 * 3, 4, 2, 3, 4))
>>> B = torch.randn(2 * 3, 4)
>>> X = torch.linalg.tensorsolve(A, B)
>>> X.shape
torch.Size([2, 3, 4])
>>> torch.allclose(torch.tensordot(A, X, dims=X.ndim), B)
True

>>> A = torch.randn(6, 4, 4, 3, 2)
>>> B = torch.randn(4, 3, 2)
>>> X = torch.linalg.tensorsolve(A, B, dims=(0, 2))
>>> X.shape
torch.Size([6, 4])
>>> A = A.permute(1, 3, 4, 0, 2)
>>> A.shape[B.ndim:]
torch.Size([6, 4])
>>> torch.allclose(torch.tensordot(A, X, dims=X.ndim), B, atol=1e-6)
True
```