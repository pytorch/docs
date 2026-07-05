# torch.linalg.tensorinv

torch.linalg.tensorinv(*A*, *ind=2*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/linalg/__init__.py#L2736)

Computes the multiplicative inverse of [`torch.tensordot()`](torch.tensordot.html#torch.tensordot).

If m is the product of the first `ind` dimensions of `A` and n is the product of
the rest of the dimensions, this function expects m and n to be equal.
If this is the case, it computes a tensor X such that
tensordot(`A`, X, `ind`) is the identity matrix in dimension m.
X will have the shape of `A` but with the first `ind` dimensions pushed back to the end

```
X.shape == A.shape[ind:] + A.shape[:ind]
```

Supports input of float, double, cfloat and cdouble dtypes.

Note

When `A` is a 2-dimensional tensor and `ind`= 1,
this function computes the (multiplicative) inverse of `A`
(see [`torch.linalg.inv()`](torch.linalg.inv.html#torch.linalg.inv)).

Note

Consider using [`torch.linalg.tensorsolve()`](torch.linalg.tensorsolve.html#torch.linalg.tensorsolve) if possible for multiplying a tensor on the left
by the tensor inverse, as:

```
linalg.tensorsolve(A, B) == torch.tensordot(linalg.tensorinv(A), B) # When B is a tensor with shape A.shape[:B.ndim]
```

It is always preferred to use [`tensorsolve()`](torch.linalg.tensorsolve.html#torch.linalg.tensorsolve) when possible, as it is faster and more
numerically stable than computing the pseudoinverse explicitly.

See also

[`torch.linalg.tensorsolve()`](torch.linalg.tensorsolve.html#torch.linalg.tensorsolve) computes
torch.tensordot(tensorinv(`A`), `B`).

Parameters:

- **A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor to invert. Its shape must satisfy
prod(`A`.shape[:`ind`]) ==
prod(`A`.shape[`ind`:]).
- **ind** ([*int*](https://docs.python.org/3/library/functions.html#int)) - index at which to compute the inverse of [`torch.tensordot()`](torch.tensordot.html#torch.tensordot). Default: 2.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - output tensor. Ignored if None. Default: None.

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - if the reshaped `A` is not invertible or the product of the first
 `ind` dimensions is not equal to the product of the rest.

Examples:

```
>>> A = torch.eye(4 * 6).reshape((4, 6, 8, 3))
>>> Ainv = torch.linalg.tensorinv(A, ind=2)
>>> Ainv.shape
torch.Size([8, 3, 4, 6])
>>> B = torch.randn(4, 6)
>>> torch.allclose(torch.tensordot(Ainv, B), torch.linalg.tensorsolve(A, B))
True

>>> A = torch.randn(4, 4)
>>> Atensorinv = torch.linalg.tensorinv(A, ind=1)
>>> Ainv = torch.linalg.inv(A)
>>> torch.allclose(Atensorinv, Ainv)
True
```