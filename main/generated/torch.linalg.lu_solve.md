# torch.linalg.lu_solve

torch.linalg.lu_solve(*LU*, *pivots*, *B*, ***, *left=True*, *adjoint=False*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/34424f27313fbcddaafe4a1a855000f17e05a260/torch/linalg/__init__.py#L2523)

Computes the solution of a square system of linear equations with a unique solution given an LU decomposition.

Letting K\mathbb{K}K be R\mathbb{R}R or C\mathbb{C}C,
this function computes the solution X∈Kn×kX \in \mathbb{K}^{n \times k}X∈Kn×k of the **linear system** associated to
A∈Kn×n,B∈Kn×kA \in \mathbb{K}^{n \times n}, B \in \mathbb{K}^{n \times k}A∈Kn×n,B∈Kn×k, which is defined as

AX=BAX = B

AX=B

where AAA is given factorized as returned by [`lu_factor()`](torch.linalg.lu_factor.html#torch.linalg.lu_factor).

If `left`= False, this function returns the matrix X∈Kn×kX \in \mathbb{K}^{n \times k}X∈Kn×k that solves the system

XA=BA∈Kk×k,B∈Kn×k.XA = B\mathrlap{\qquad A \in \mathbb{K}^{k \times k}, B \in \mathbb{K}^{n \times k}.}XA=BA∈Kk×k,B∈Kn×k.

If `adjoint`= True (and `left`= True), given an LU factorization of AAA
this function function returns the X∈Kn×kX \in \mathbb{K}^{n \times k}X∈Kn×k that solves the system

AHX=BA∈Kk×k,B∈Kn×k.A^{\text{H}}X = B\mathrlap{\qquad A \in \mathbb{K}^{k \times k}, B \in \mathbb{K}^{n \times k}.}AHX=BA∈Kk×k,B∈Kn×k.

where AHA^{\text{H}}AH is the conjugate transpose when AAA is complex, and the
transpose when AAA is real-valued. The `left`= False case is analogous.

Supports inputs of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if the inputs are batches of matrices then
the output has the same batch dimensions.

Parameters:

- **LU** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, n, n) (or (*, k, k) if `left`= True)
where * is zero or more batch dimensions as returned by [`lu_factor()`](torch.linalg.lu_factor.html#torch.linalg.lu_factor).
- **pivots** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, n) (or (*, k) if `left`= True)
where * is zero or more batch dimensions as returned by [`lu_factor()`](torch.linalg.lu_factor.html#torch.linalg.lu_factor).
- **B** ([*Tensor*](../tensors.html#torch.Tensor)) - right-hand side tensor of shape (*, n, k).

Keyword Arguments:

- **left** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether to solve the system AX=BAX=BAX=B or XA=BXA = BXA=B. Default: True.
- **adjoint** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether to solve the system AX=BAX=BAX=B or AHX=BA^{\text{H}}X = BAHX=B. Default: False.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - output tensor. Ignored if None. Default: None.

Examples:

```
>>> A = torch.randn(3, 3)
>>> LU, pivots = torch.linalg.lu_factor(A)
>>> B = torch.randn(3, 2)
>>> X = torch.linalg.lu_solve(LU, pivots, B)
>>> torch.allclose(A @ X, B)
True

>>> B = torch.randn(3, 3, 2) # Broadcasting rules apply: A is broadcasted
>>> X = torch.linalg.lu_solve(LU, pivots, B)
>>> torch.allclose(A @ X, B)
True

>>> B = torch.randn(3, 5, 3)
>>> X = torch.linalg.lu_solve(LU, pivots, B, left=False)
>>> torch.allclose(X @ A, B)
True

>>> B = torch.randn(3, 3, 4) # Now solve for A^T
>>> X = torch.linalg.lu_solve(LU, pivots, B, adjoint=True)
>>> torch.allclose(A.mT @ X, B)
True
```