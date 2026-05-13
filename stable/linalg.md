# torch.linalg

Common linear algebra operations.

See [Linear algebra (torch.linalg)](notes/numerical_accuracy.html#linear-algebra-stability) for some common numerical edge-cases.

## Matrix Properties

| [`norm`](generated/torch.linalg.norm.html#torch.linalg.norm) | Computes a vector or matrix norm. |
| --- | --- |
| [`vector_norm`](generated/torch.linalg.vector_norm.html#torch.linalg.vector_norm) | Computes a vector norm. |
| [`matrix_norm`](generated/torch.linalg.matrix_norm.html#torch.linalg.matrix_norm) | Computes a matrix norm. |
| [`diagonal`](generated/torch.linalg.diagonal.html#torch.linalg.diagonal) | Alias for [`torch.diagonal()`](generated/torch.diagonal.html#torch.diagonal) with defaults `dim1`= -2, `dim2`= -1. |
| [`det`](generated/torch.linalg.det.html#torch.linalg.det) | Computes the determinant of a square matrix. |
| [`slogdet`](generated/torch.linalg.slogdet.html#torch.linalg.slogdet) | Computes the sign and natural logarithm of the absolute value of the determinant of a square matrix. |
| [`cond`](generated/torch.linalg.cond.html#torch.linalg.cond) | Computes the condition number of a matrix with respect to a matrix norm. |
| [`matrix_rank`](generated/torch.linalg.matrix_rank.html#torch.linalg.matrix_rank) | Computes the numerical rank of a matrix. |

## Decompositions

| [`cholesky`](generated/torch.linalg.cholesky.html#torch.linalg.cholesky) | Computes the Cholesky decomposition of a complex Hermitian or real symmetric positive-definite matrix. |
| --- | --- |
| [`qr`](generated/torch.linalg.qr.html#torch.linalg.qr) | Computes the QR decomposition of a matrix. |
| [`lu`](generated/torch.linalg.lu.html#torch.linalg.lu) | Computes the LU decomposition with partial pivoting of a matrix. |
| [`lu_factor`](generated/torch.linalg.lu_factor.html#torch.linalg.lu_factor) | Computes a compact representation of the LU factorization with partial pivoting of a matrix. |
| [`eig`](generated/torch.linalg.eig.html#torch.linalg.eig) | Computes the eigenvalue decomposition of a square matrix if it exists. |
| [`eigvals`](generated/torch.linalg.eigvals.html#torch.linalg.eigvals) | Computes the eigenvalues of a square matrix. |
| [`eigh`](generated/torch.linalg.eigh.html#torch.linalg.eigh) | Computes the eigenvalue decomposition of a complex Hermitian or real symmetric matrix. |
| [`eigvalsh`](generated/torch.linalg.eigvalsh.html#torch.linalg.eigvalsh) | Computes the eigenvalues of a complex Hermitian or real symmetric matrix. |
| [`svd`](generated/torch.linalg.svd.html#torch.linalg.svd) | Computes the singular value decomposition (SVD) of a matrix. |
| [`svdvals`](generated/torch.linalg.svdvals.html#torch.linalg.svdvals) | Computes the singular values of a matrix. |

## Solvers

| [`solve`](generated/torch.linalg.solve.html#torch.linalg.solve) | Computes the solution of a square system of linear equations with a unique solution. |
| --- | --- |
| [`solve_triangular`](generated/torch.linalg.solve_triangular.html#torch.linalg.solve_triangular) | Computes the solution of a triangular system of linear equations with a unique solution. |
| [`lu_solve`](generated/torch.linalg.lu_solve.html#torch.linalg.lu_solve) | Computes the solution of a square system of linear equations with a unique solution given an LU decomposition. |
| [`lstsq`](generated/torch.linalg.lstsq.html#torch.linalg.lstsq) | Computes a solution to the least squares problem of a system of linear equations. |

## Inverses

| [`inv`](generated/torch.linalg.inv.html#torch.linalg.inv) | Computes the inverse of a square matrix if it exists. |
| --- | --- |
| [`pinv`](generated/torch.linalg.pinv.html#torch.linalg.pinv) | Computes the pseudoinverse (Moore-Penrose inverse) of a matrix. |

## Matrix Functions

| [`matrix_exp`](generated/torch.linalg.matrix_exp.html#torch.linalg.matrix_exp) | Computes the matrix exponential of a square matrix. |
| --- | --- |
| [`matrix_power`](generated/torch.linalg.matrix_power.html#torch.linalg.matrix_power) | Computes the n-th power of a square matrix for an integer n. |

## Matrix Products

| [`cross`](generated/torch.linalg.cross.html#torch.linalg.cross) | Computes the cross product of two 3-dimensional vectors. |
| --- | --- |
| [`matmul`](generated/torch.linalg.matmul.html#torch.linalg.matmul) | Alias for [`torch.matmul()`](generated/torch.matmul.html#torch.matmul) |
| [`vecdot`](generated/torch.linalg.vecdot.html#torch.linalg.vecdot) | Computes the dot product of two batches of vectors along a dimension. |
| [`multi_dot`](generated/torch.linalg.multi_dot.html#torch.linalg.multi_dot) | Efficiently multiplies two or more matrices by reordering the multiplications so that the fewest arithmetic operations are performed. |
| [`householder_product`](generated/torch.linalg.householder_product.html#torch.linalg.householder_product) | Computes the first n columns of a product of Householder matrices. |

## Tensor Operations

| [`tensorinv`](generated/torch.linalg.tensorinv.html#torch.linalg.tensorinv) | Computes the multiplicative inverse of [`torch.tensordot()`](generated/torch.tensordot.html#torch.tensordot). |
| --- | --- |
| [`tensorsolve`](generated/torch.linalg.tensorsolve.html#torch.linalg.tensorsolve) | Computes the solution X to the system torch.tensordot(A, X) = B. |

## Misc

| [`vander`](generated/torch.linalg.vander.html#torch.linalg.vander) | Generates a Vandermonde matrix. |
| --- | --- |

## Experimental Functions

| [`cholesky_ex`](generated/torch.linalg.cholesky_ex.html#torch.linalg.cholesky_ex) | Computes the Cholesky decomposition of a complex Hermitian or real symmetric positive-definite matrix. |
| --- | --- |
| [`inv_ex`](generated/torch.linalg.inv_ex.html#torch.linalg.inv_ex) | Computes the inverse of a square matrix if it is invertible. |
| [`solve_ex`](generated/torch.linalg.solve_ex.html#torch.linalg.solve_ex) | A version of [`solve()`](generated/torch.linalg.solve.html#torch.linalg.solve) that does not perform error checks unless `check_errors`= True. |
| [`lu_factor_ex`](generated/torch.linalg.lu_factor_ex.html#torch.linalg.lu_factor_ex) | This is a version of [`lu_factor()`](generated/torch.linalg.lu_factor.html#torch.linalg.lu_factor) that does not perform error checks unless `check_errors`= True. |
| [`ldl_factor`](generated/torch.linalg.ldl_factor.html#torch.linalg.ldl_factor) | Computes a compact representation of the LDL factorization of a Hermitian or symmetric (possibly indefinite) matrix. |
| [`ldl_factor_ex`](generated/torch.linalg.ldl_factor_ex.html#torch.linalg.ldl_factor_ex) | This is a version of [`ldl_factor()`](generated/torch.linalg.ldl_factor.html#torch.linalg.ldl_factor) that does not perform error checks unless `check_errors`= True. |
| [`ldl_solve`](generated/torch.linalg.ldl_solve.html#torch.linalg.ldl_solve) | Computes the solution of a system of linear equations using the LDL factorization. |