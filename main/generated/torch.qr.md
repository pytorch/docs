# torch.qr

torch.qr(*input: [Tensor](../tensors.html#torch.Tensor)*, *some: [bool](https://docs.python.org/3/library/functions.html#bool) = True*, ***, *out: [Tensor](../tensors.html#torch.Tensor) | Tuple[[Tensor](../tensors.html#torch.Tensor), ...] | List[[Tensor](../tensors.html#torch.Tensor)] | [None](https://docs.python.org/3/library/constants.html#None)*)

Computes the QR decomposition of a matrix or a batch of matrices `input`,
and returns a namedtuple (Q, R) of tensors such that input=QR\text{input} = Q Rinput=QR
with QQQ being an orthogonal matrix or batch of orthogonal matrices and
RRR being an upper triangular matrix or batch of upper triangular matrices.

If `some` is `True`, then this function returns the thin (reduced) QR factorization.
Otherwise, if `some` is `False`, this function returns the complete QR factorization.

Warning

`torch.qr()` is deprecated in favor of [`torch.linalg.qr()`](torch.linalg.qr.html#torch.linalg.qr)
and will be removed in a future PyTorch release. The boolean parameter `some` has been
replaced with a string parameter [`mode`](torch.mode.html#torch.mode).

`Q, R = torch.qr(A)` should be replaced with

```
Q, R = torch.linalg.qr(A)
```

`Q, R = torch.qr(A, some=False)` should be replaced with

```
Q, R = torch.linalg.qr(A, mode="complete")
```

Warning

If you plan to backpropagate through QR, note that the current backward implementation
is only well-defined when the first min⁡(input.size(−1),input.size(−2))\min(input.size(-1), input.size(-2))min(input.size(−1),input.size(−2))
columns of `input` are linearly independent.
This behavior will probably change once QR supports pivoting.

Note

This function uses LAPACK for CPU inputs and MAGMA for CUDA inputs,
and may produce different (valid) decompositions on different device types
or different platforms.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor of size (∗,m,n)(*, m, n)(∗,m,n) where * is zero or more
batch dimensions consisting of matrices of dimension m×nm \times nm×n.
- **some** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) -

Set to `True` for reduced QR decomposition and `False` for
complete QR decomposition. If k = min(m, n) then:

> - `some=True` : returns (Q, R) with dimensions (m, k), (k, n) (default)
> - `'some=False'`: returns (Q, R) with dimensions (m, m), (m, n)

Keyword Arguments:

**out** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - tuple of Q and R tensors.
The dimensions of Q and R are detailed in the description of `some` above.

Example:

```
>>> a = torch.tensor([[12., -51, 4], [6, 167, -68], [-4, 24, -41]])
>>> q, r = torch.qr(a)
>>> q
tensor([[-0.8571, 0.3943, 0.3314],
 [-0.4286, -0.9029, -0.0343],
 [ 0.2857, -0.1714, 0.9429]])
>>> r
tensor([[ -14.0000, -21.0000, 14.0000],
 [ 0.0000, -175.0000, 70.0000],
 [ 0.0000, 0.0000, -35.0000]])
>>> torch.mm(q, r).round()
tensor([[ 12., -51., 4.],
 [ 6., 167., -68.],
 [ -4., 24., -41.]])
>>> torch.mm(q.t(), q).round()
tensor([[ 1., 0., 0.],
 [ 0., 1., -0.],
 [ 0., -0., 1.]])
>>> a = torch.randn(3, 4, 5)
>>> q, r = torch.qr(a, some=False)
>>> torch.allclose(torch.matmul(q, r), a)
True
>>> torch.allclose(torch.matmul(q.mT, q), torch.eye(5))
True
```