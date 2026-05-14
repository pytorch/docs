# torch.linalg.matrix_rank

torch.linalg.matrix_rank(*A*, ***, *atol=None*, *rtol=None*, *hermitian=False*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/linalg/__init__.py#L1263)

Computes the numerical rank of a matrix.

The matrix rank is computed as the number of singular values
(or eigenvalues in absolute value when `hermitian`= True)
that are greater than max⁡(atol,σ1∗rtol)\max(\text{atol}, \sigma_1 * \text{rtol})max(atol,σ1​∗rtol) threshold,
where σ1\sigma_1σ1​ is the largest singular value (or eigenvalue).

Supports input of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if `A` is a batch of matrices then
the output has the same batch dimensions.

If `hermitian`= True, `A` is assumed to be Hermitian if complex or
symmetric if real, but this is not checked internally. Instead, just the lower
triangular part of the matrix is used in the computations.

If `rtol` is not specified and `A` is a matrix of dimensions (m, n),
the relative tolerance is set to be rtol=max⁡(m,n)ε\text{rtol} = \max(m, n) \varepsilonrtol=max(m,n)ε
and ε\varepsilonε is the epsilon value for the dtype of `A` (see [`finfo`](../type_info.html#torch.torch.finfo)).
If `rtol` is not specified and `atol` is specified to be larger than zero then
`rtol` is set to zero.

If `atol` or `rtol` is a [`torch.Tensor`](../tensors.html#torch.Tensor), its shape must be broadcastable to that
of the singular values of `A` as returned by [`torch.linalg.svdvals()`](torch.linalg.svdvals.html#torch.linalg.svdvals).

Note

This function has NumPy compatible variant linalg.matrix_rank(A, tol, hermitian=False).
However, use of the positional argument `tol` is deprecated in favor of `atol` and `rtol`.

Note

The matrix rank is computed using a singular value decomposition
[`torch.linalg.svdvals()`](torch.linalg.svdvals.html#torch.linalg.svdvals) if `hermitian`= False (default) and the eigenvalue
decomposition [`torch.linalg.eigvalsh()`](torch.linalg.eigvalsh.html#torch.linalg.eigvalsh) when `hermitian`= True.
When inputs are on a CUDA device, this function synchronizes that device with the CPU.

Parameters:

- **A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, m, n) where * is zero or more batch dimensions.
- **tol** ([*float*](https://docs.python.org/3/library/functions.html#float)*,*[*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - [NumPy Compat] Alias for `atol`. Default: None.

Keyword Arguments:

- **atol** ([*float*](https://docs.python.org/3/library/functions.html#float)*,*[*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the absolute tolerance value. When None it's considered to be zero.
Default: None.
- **rtol** ([*float*](https://docs.python.org/3/library/functions.html#float)*,*[*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the relative tolerance value. See above for the value it takes when None.
Default: None.
- **hermitian** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - indicates whether `A` is Hermitian if complex
or symmetric if real. Default: False.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - output tensor. Ignored if None. Default: None.

Examples:

```
>>> A = torch.eye(10)
>>> torch.linalg.matrix_rank(A)
tensor(10)
>>> B = torch.eye(10)
>>> B[0, 0] = 0
>>> torch.linalg.matrix_rank(B)
tensor(9)

>>> A = torch.randn(4, 3, 2)
>>> torch.linalg.matrix_rank(A)
tensor([2, 2, 2, 2])

>>> A = torch.randn(2, 4, 2, 3)
>>> torch.linalg.matrix_rank(A)
tensor([[2, 2, 2, 2],
 [2, 2, 2, 2]])

>>> A = torch.randn(2, 4, 3, 3, dtype=torch.complex64)
>>> torch.linalg.matrix_rank(A)
tensor([[3, 3, 3, 3],
 [3, 3, 3, 3]])
>>> torch.linalg.matrix_rank(A, hermitian=True)
tensor([[3, 3, 3, 3],
 [3, 3, 3, 3]])
>>> torch.linalg.matrix_rank(A, atol=1.0, rtol=0.0)
tensor([[3, 2, 2, 2],
 [1, 2, 1, 2]])
>>> torch.linalg.matrix_rank(A, atol=1.0, rtol=0.0, hermitian=True)
tensor([[2, 2, 2, 1],
 [1, 2, 2, 2]])
```