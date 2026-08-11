# torch.lu_unpack

torch.lu_unpack(*LU_data*, *LU_pivots*, *unpack_data=True*, *unpack_pivots=True*, ***, *out=None*)

Unpacks the LU decomposition returned by [`lu_factor()`](torch.linalg.lu_factor.html#torch.linalg.lu_factor) into the P, L, U matrices.

See also

[`lu()`](torch.linalg.lu.html#torch.linalg.lu) returns the matrices from the LU decomposition. Its gradient formula is more efficient
than that of doing [`lu_factor()`](torch.linalg.lu_factor.html#torch.linalg.lu_factor) followed by `lu_unpack()`.

Parameters:

- **LU_data** ([*Tensor*](../tensors.html#torch.Tensor)) - the packed LU factorization data
- **LU_pivots** ([*Tensor*](../tensors.html#torch.Tensor)) - the packed LU factorization pivots
- **unpack_data** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - flag indicating if the data should be unpacked.
If `False`, then the returned `L` and `U` are empty tensors.
Default: `True`
- **unpack_pivots** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - flag indicating if the pivots should be unpacked into a permutation matrix `P`.
If `False`, then the returned `P` is an empty tensor.
Default: `True`

Keyword Arguments:

**out** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - output tuple of three tensors. Ignored if None.

Returns:

A namedtuple `(P, L, U)`

Examples:

```
>>> A = torch.randn(2, 3, 3)
>>> LU, pivots = torch.linalg.lu_factor(A)
>>> P, L, U = torch.lu_unpack(LU, pivots)
>>> # We can recover A from the factorization
>>> A_ = P @ L @ U
>>> torch.allclose(A, A_)
True

>>> # LU factorization of a rectangular matrix:
>>> A = torch.randn(2, 3, 2)
>>> LU, pivots = torch.linalg.lu_factor(A)
>>> P, L, U = torch.lu_unpack(LU, pivots)
>>> # P, L, U are the same as returned by linalg.lu
>>> P_, L_, U_ = torch.linalg.lu(A)
>>> torch.allclose(P, P_) and torch.allclose(L, L_) and torch.allclose(U, U_)
True
```