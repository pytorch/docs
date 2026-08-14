# torch.linalg.solve

torch.linalg.solve(*A*, *B*, ***, *left=True*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/linalg/__init__.py#L2260)

Computes the solution of a square system of linear equations with a unique solution.

Letting K\mathbb{K}K be R\mathbb{R}R or C\mathbb{C}C,
this function computes the solution X∈Kn×kX \in \mathbb{K}^{n \times k}X∈Kn×k of the **linear system** associated to
A∈Kn×n,B∈Kn×kA \in \mathbb{K}^{n \times n}, B \in \mathbb{K}^{n \times k}A∈Kn×n,B∈Kn×k, which is defined as

AX=BAX = B

AX=B

If `left`= False, this function returns the matrix X∈Kn×kX \in \mathbb{K}^{n \times k}X∈Kn×k that solves the system

XA=BA∈Kk×k,B∈Kn×k.XA = B\mathrlap{\qquad A \in \mathbb{K}^{k \times k}, B \in \mathbb{K}^{n \times k}.}XA=BA∈Kk×k,B∈Kn×k.

This system of linear equations has one solution if and only if AAA is [invertible](https://en.wikipedia.org/wiki/Invertible_matrix#The_invertible_matrix_theorem).
This function assumes that AAA is invertible.

Supports inputs of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if the inputs are batches of matrices then
the output has the same batch dimensions.

Letting * be zero or more batch dimensions,

- If `A` has shape (*, n, n) and `B` has shape (*, n) (a batch of vectors) or shape
(*, n, k) (a batch of matrices or "multiple right-hand sides"), this function returns X of shape
(*, n) or (*, n, k) respectively.
- Otherwise, if `A` has shape (*, n, n) and `B` has shape (n,) or (n, k), `B`
is broadcasted to have shape (*, n) or (*, n, k) respectively.
This function then returns the solution of the resulting batch of systems of linear equations.

Note

This function computes X = `A`.inverse() @ `B` in a faster and
more numerically stable way than performing the computations separately.

Note

It is possible to compute the solution of the system XA=BXA = BXA=B by passing the inputs
`A` and `B` transposed and transposing the output returned by this function.

Note

`A` is allowed to be a non-batched torch.sparse_csr_tensor, but only with left=True.

Note

When inputs are on a CUDA device, this function synchronizes that device with the CPU. For a version of this function that does not synchronize, see [`torch.linalg.solve_ex()`](torch.linalg.solve_ex.html#torch.linalg.solve_ex).

See also

[`torch.linalg.solve_triangular()`](torch.linalg.solve_triangular.html#torch.linalg.solve_triangular) computes the solution of a triangular system of linear
equations with a unique solution.

Parameters:

- **A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, n, n) where * is zero or more batch dimensions.
- **B** ([*Tensor*](../tensors.html#torch.Tensor)) - right-hand side tensor of shape (*, n) or (*, n, k) or (n,) or (n, k)
according to the rules described above

Keyword Arguments:

- **left** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether to solve the system AX=BAX=BAX=B or XA=BXA = BXA=B. Default: True.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - output tensor. Ignored if None. Default: None.

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - if the `A` matrix is not invertible or any matrix in a batched `A`
 is not invertible.

Examples:

```
>>> A = torch.randn(3, 3)
>>> b = torch.randn(3)
>>> x = torch.linalg.solve(A, b)
>>> torch.allclose(A @ x, b)
True
>>> A = torch.randn(2, 3, 3)
>>> B = torch.randn(2, 3, 4)
>>> X = torch.linalg.solve(A, B)
>>> X.shape
torch.Size([2, 3, 4])
>>> torch.allclose(A @ X, B)
True

>>> A = torch.randn(2, 3, 3)
>>> b = torch.randn(3, 1)
>>> x = torch.linalg.solve(A, b) # b is broadcasted to size (2, 3, 1)
>>> x.shape
torch.Size([2, 3, 1])
>>> torch.allclose(A @ x, b)
True
>>> b = torch.randn(3)
>>> x = torch.linalg.solve(A, b) # b is broadcasted to size (2, 3)
>>> x.shape
torch.Size([2, 3])
>>> Ax = A @ x.unsqueeze(-1)
>>> torch.allclose(Ax, b.unsqueeze(-1).expand_as(Ax))
True
```