# torch.linalg.inv

torch.linalg.inv(*A*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/6e3cf2e4280672104341718ea51a55799bb3aca4/torch/linalg/__init__.py#L214)

Computes the inverse of a square matrix if it exists.
Throws a RuntimeError if the matrix is not invertible.

Letting K\mathbb{K}K be R\mathbb{R}R or C\mathbb{C}C,
for a matrix A∈Kn×nA \in \mathbb{K}^{n \times n}A∈Kn×n,
its **inverse matrix** A−1∈Kn×nA^{-1} \in \mathbb{K}^{n \times n}A−1∈Kn×n (if it exists) is defined as

A−1A=AA−1=InA^{-1}A = AA^{-1} = \mathrm{I}_nA−1A=AA−1=In​

where In\mathrm{I}_nIn​ is the n-dimensional identity matrix.

The inverse matrix exists if and only if AAA is [invertible](https://en.wikipedia.org/wiki/Invertible_matrix#The_invertible_matrix_theorem). In this case,
the inverse is unique.

Supports input of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if `A` is a batch of matrices
then the output has the same batch dimensions.

Note

When inputs are on a CUDA device, this function synchronizes that device with the CPU. For a version of this function that does not synchronize, see [`torch.linalg.inv_ex()`](torch.linalg.inv_ex.html#torch.linalg.inv_ex).

Note

Consider using [`torch.linalg.solve()`](torch.linalg.solve.html#torch.linalg.solve) if possible for multiplying a matrix on the left by
the inverse, as:

```
linalg.solve(A, B) == linalg.inv(A) @ B # When B is a matrix
```

It is always preferred to use [`solve()`](torch.linalg.solve.html#torch.linalg.solve) when possible, as it is faster and more
numerically stable than computing the inverse explicitly.

See also

[`torch.linalg.pinv()`](torch.linalg.pinv.html#torch.linalg.pinv) computes the pseudoinverse (Moore-Penrose inverse) of matrices
of any shape.

[`torch.linalg.solve()`](torch.linalg.solve.html#torch.linalg.solve) computes `A`.inv() @ `B` with a
numerically stable algorithm.

Parameters:

**A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, n, n) where * is zero or more batch dimensions
consisting of invertible matrices.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - output tensor. Ignored if None. Default: None.

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - if the matrix `A` or any matrix in the batch of matrices `A` is not invertible.

Examples:

```
>>> A = torch.randn(4, 4)
>>> Ainv = torch.linalg.inv(A)
>>> torch.dist(A @ Ainv, torch.eye(4))
tensor(1.1921e-07)

>>> A = torch.randn(2, 3, 4, 4) # Batch of matrices
>>> Ainv = torch.linalg.inv(A)
>>> torch.dist(A @ Ainv, torch.eye(4))
tensor(1.9073e-06)

>>> A = torch.randn(4, 4, dtype=torch.complex128) # Complex matrix
>>> Ainv = torch.linalg.inv(A)
>>> torch.dist(A @ Ainv, torch.eye(4))
tensor(7.5107e-16, dtype=torch.float64)
```