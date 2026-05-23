# torch.linalg.matrix_exp

torch.linalg.matrix_exp(*A*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/2f696474dc8fe614670ddb889f4ae1c75d1a11e6/torch/linalg/__init__.py#L2168)

Computes the matrix exponential of a square matrix.

Letting K\mathbb{K}K be R\mathbb{R}R or C\mathbb{C}C,
this function computes the **matrix exponential** of A∈Kn×nA \in \mathbb{K}^{n \times n}A∈Kn×n, which is defined as

matrix_exp(A)=∑k=0∞1k!Ak∈Kn×n.\mathrm{matrix\_exp}(A) = \sum_{k=0}^\infty \frac{1}{k!}A^k \in \mathbb{K}^{n \times n}.

matrix_exp(A)=k=0∑∞​k!1​Ak∈Kn×n.

If the matrix AAA has eigenvalues λi∈C\lambda_i \in \mathbb{C}λi​∈C,
the matrix matrix_exp(A)\mathrm{matrix\_exp}(A)matrix_exp(A) has eigenvalues eλi∈Ce^{\lambda_i} \in \mathbb{C}eλi​∈C.

Supports input of bfloat16, float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if `A` is a batch of matrices then
the output has the same batch dimensions.

Parameters:

**A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, n, n) where * is zero or more batch dimensions.

Example:

```
>>> A = torch.empty(2, 2, 2)
>>> A[0, :, :] = torch.eye(2, 2)
>>> A[1, :, :] = 2 * torch.eye(2, 2)
>>> A
tensor([[[1., 0.],
 [0., 1.]],

 [[2., 0.],
 [0., 2.]]])
>>> torch.linalg.matrix_exp(A)
tensor([[[2.7183, 0.0000],
 [0.0000, 2.7183]],

 [[7.3891, 0.0000],
 [0.0000, 7.3891]]])

>>> import math
>>> A = torch.tensor([[0, math.pi/3], [-math.pi/3, 0]]) # A is skew-symmetric
>>> torch.linalg.matrix_exp(A) # matrix_exp(A) = [[cos(pi/3), sin(pi/3)], [-sin(pi/3), cos(pi/3)]]
tensor([[ 0.5000, 0.8660],
 [-0.8660, 0.5000]])
```