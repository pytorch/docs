# torch.linalg.cond

torch.linalg.cond(*A*, *p=None*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/847b7df02b84551445eda7d44d08f15bda4c6159/torch/linalg/__init__.py#L1943)

Computes the condition number of a matrix with respect to a matrix norm.

Letting K\mathbb{K}K be R\mathbb{R}R or C\mathbb{C}C,
the **condition number** κ\kappaκ of a matrix
A∈Kn×nA \in \mathbb{K}^{n \times n}A∈Kn×n is defined as

κ(A)=∥A∥p∥A−1∥p\kappa(A) = \|A\|_p\|A^{-1}\|_pκ(A)=∥A∥p​∥A−1∥p​

The condition number of `A` measures the numerical stability of the linear system AX = B
with respect to a matrix norm.

Supports input of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if `A` is a batch of matrices then
the output has the same batch dimensions.

`p` defines the matrix norm that is computed. The following norms are supported:

| `p` | matrix norm |
| --- | --- |
| None | 2-norm (largest singular value) |
| 'fro' | Frobenius norm |
| 'nuc' | nuclear norm |
| inf | max(sum(abs(x), dim=1)) |
| -inf | min(sum(abs(x), dim=1)) |
| 1 | max(sum(abs(x), dim=0)) |
| -1 | min(sum(abs(x), dim=0)) |
| 2 | largest singular value |
| -2 | smallest singular value |

where inf refers to float('inf'), NumPy's inf object, or any equivalent object.

For `p` is one of ('fro', 'nuc', inf, -inf, 1, -1), this function uses
[`torch.linalg.norm()`](torch.linalg.norm.html#torch.linalg.norm) and [`torch.linalg.inv()`](torch.linalg.inv.html#torch.linalg.inv).
As such, in this case, the matrix (or every matrix in the batch) `A` has to be square
and invertible.

For `p` in (2, -2), this function can be computed in terms of the singular values
σ1≥...≥σn\sigma_1 \geq \ldots \geq \sigma_nσ1​≥...≥σn​

κ2(A)=σ1σnκ−2(A)=σnσ1\kappa_2(A) = \frac{\sigma_1}{\sigma_n}\qquad \kappa_{-2}(A) = \frac{\sigma_n}{\sigma_1}κ2​(A)=σn​σ1​​κ−2​(A)=σ1​σn​​

In these cases, it is computed using [`torch.linalg.svdvals()`](torch.linalg.svdvals.html#torch.linalg.svdvals). For these norms, the matrix
(or every matrix in the batch) `A` may have any shape.

Note

When inputs are on a CUDA device, this function synchronizes that device with the CPU
if `p` is one of ('fro', 'nuc', inf, -inf, 1, -1).

See also

[`torch.linalg.solve()`](torch.linalg.solve.html#torch.linalg.solve) for a function that solves linear systems of square matrices.

[`torch.linalg.lstsq()`](torch.linalg.lstsq.html#torch.linalg.lstsq) for a function that solves linear systems of general matrices.

Parameters:

- **A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, m, n) where * is zero or more batch dimensions
for `p` in (2, -2), and of shape (*, n, n) where every matrix
is invertible for `p` in ('fro', 'nuc', inf, -inf, 1, -1).
- **p** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**inf**,**-inf**,**'fro'**,**'nuc'**,**optional*) - the type of the matrix norm to use in the computations (see above). Default: None

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - output tensor. Ignored if None. Default: None.

Returns:

A real-valued tensor, even when `A` is complex.

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - if `p` is one of ('fro', 'nuc', inf, -inf, 1, -1)
 and the `A` matrix or any matrix in the batch `A` is not square
 or invertible.

Examples:

```
>>> A = torch.randn(3, 4, 4, dtype=torch.complex64)
>>> torch.linalg.cond(A)
>>> A = torch.tensor([[1., 0, -1], [0, 1, 0], [1, 0, 1]])
>>> torch.linalg.cond(A)
tensor([1.4142])
>>> torch.linalg.cond(A, 'fro')
tensor(3.1623)
>>> torch.linalg.cond(A, 'nuc')
tensor(9.2426)
>>> torch.linalg.cond(A, float('inf'))
tensor(2.)
>>> torch.linalg.cond(A, float('-inf'))
tensor(1.)
>>> torch.linalg.cond(A, 1)
tensor(2.)
>>> torch.linalg.cond(A, -1)
tensor(1.)
>>> torch.linalg.cond(A, 2)
tensor([1.4142])
>>> torch.linalg.cond(A, -2)
tensor([0.7071])

>>> A = torch.randn(2, 3, 3)
>>> torch.linalg.cond(A)
tensor([[9.5917],
 [3.2538]])
>>> A = torch.randn(2, 3, 3, dtype=torch.complex64)
>>> torch.linalg.cond(A)
tensor([[4.6245],
 [4.5671]])
```