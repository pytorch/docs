# torch.linalg.qr

torch.linalg.qr(*A*, *mode='reduced'*, ***, *out=None*)[[source]](https://github.com/pytorch/pytorch/blob/c9fded8194d3b089ed610b586eb746a6e74c6616/torch/linalg/__init__.py#L2865)

Computes the QR decomposition of a matrix.

Letting K\mathbb{K}K be R\mathbb{R}R or C\mathbb{C}C,
the **full QR decomposition** of a matrix
A∈Km×nA \in \mathbb{K}^{m \times n}A∈Km×n is defined as

A=QRQ∈Km×m,R∈Km×nA = QR\mathrlap{\qquad Q \in \mathbb{K}^{m \times m}, R \in \mathbb{K}^{m \times n}}A=QRQ∈Km×m,R∈Km×n

where QQQ is orthogonal in the real case and unitary in the complex case,
and RRR is upper triangular with real diagonal (even in the complex case).

When m > n (tall matrix), as R is upper triangular, its last m - n rows are zero.
In this case, we can drop the last m - n columns of Q to form the
**reduced QR decomposition**:

A=QRQ∈Km×n,R∈Kn×nA = QR\mathrlap{\qquad Q \in \mathbb{K}^{m \times n}, R \in \mathbb{K}^{n \times n}}A=QRQ∈Km×n,R∈Kn×n

The reduced QR decomposition agrees with the full QR decomposition when n >= m (wide matrix).

Supports input of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if `A` is a batch of matrices then
the output has the same batch dimensions.

The parameter `mode` chooses between the full and reduced QR decomposition.
If `A` has shape (*, m, n), denoting k = min(m, n)

- `mode`= 'reduced' (default): Returns (Q, R) of shapes (*, m, k), (*, k, n) respectively.
It is always differentiable.
- `mode`= 'complete': Returns (Q, R) of shapes (*, m, m), (*, m, n) respectively.
It is differentiable for m <= n.
- `mode`= 'r': Computes only the reduced R. Returns (Q, R) with Q empty and R of shape (*, k, n).
It is never differentiable.

Differences with numpy.linalg.qr:

- `mode`= 'raw' is not implemented.
- Unlike numpy.linalg.qr, this function always returns a tuple of two tensors.
When `mode`= 'r', the Q tensor is an empty tensor.

Warning

The elements in the diagonal of R are not necessarily positive.
As such, the returned QR decomposition is only unique up to the sign of the diagonal of R.
Therefore, different platforms, like NumPy, or inputs on different devices,
may produce different valid decompositions.

Warning

The QR decomposition is only well-defined if the first k = min(m, n) columns
of every matrix in `A` are linearly independent.
If this condition is not met, no error will be thrown, but the QR produced
may be incorrect and its autodiff may fail or produce incorrect results.

Parameters:

- **A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, m, n) where * is zero or more batch dimensions.
- **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - one of 'reduced', 'complete', 'r'.
Controls the shape of the returned tensors. Default: 'reduced'.

Keyword Arguments:

**out** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - output tuple of two tensors. Ignored if None. Default: None.

Returns:

A named tuple (Q, R).

Examples:

```
>>> A = torch.tensor([[12., -51, 4], [6, 167, -68], [-4, 24, -41]])
>>> Q, R = torch.linalg.qr(A)
>>> Q
tensor([[-0.8571, 0.3943, 0.3314],
 [-0.4286, -0.9029, -0.0343],
 [ 0.2857, -0.1714, 0.9429]])
>>> R
tensor([[ -14.0000, -21.0000, 14.0000],
 [ 0.0000, -175.0000, 70.0000],
 [ 0.0000, 0.0000, -35.0000]])
>>> (Q @ R).round()
tensor([[ 12., -51., 4.],
 [ 6., 167., -68.],
 [ -4., 24., -41.]])
>>> (Q.T @ Q).round()
tensor([[ 1., 0., 0.],
 [ 0., 1., -0.],
 [ 0., -0., 1.]])
>>> Q2, R2 = torch.linalg.qr(A, mode='r')
>>> Q2
tensor([])
>>> torch.equal(R, R2)
True
>>> A = torch.randn(3, 4, 5)
>>> Q, R = torch.linalg.qr(A, mode='complete')
>>> torch.dist(Q @ R, A)
tensor(1.6099e-06)
>>> torch.dist(Q.mT @ Q, torch.eye(4))
tensor(6.2158e-07)
```