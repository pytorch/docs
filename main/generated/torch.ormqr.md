# torch.ormqr

torch.ormqr(*input*, *tau*, *other*, *left=True*, *transpose=False*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the matrix-matrix multiplication of a product of Householder matrices with a general matrix.

Multiplies a m×nm \times nm×n matrix C (given by `other`) with a matrix Q,
where Q is represented using Householder reflectors (input, tau).
See [Representation of Orthogonal or Unitary Matrices](https://www.netlib.org/lapack/lug/node128.html) for further details.

If `left` is True then op(Q) times C is computed, otherwise the result is C times op(Q).
When `left` is True, the implicit matrix Q has size m×mm \times mm×m.
It has size n×nn \times nn×n otherwise.
If [`transpose`](torch.transpose.html#torch.transpose) is True then op is the conjugate transpose operation, otherwise it's a no-op.

Supports inputs of float, double, cfloat and cdouble dtypes.
Also supports batched inputs, and, if the input is batched, the output is batched with the same dimensions.

See also

[`torch.geqrf()`](torch.geqrf.html#torch.geqrf) can be used to form the Householder representation (input, tau) of matrix Q
from the QR decomposition.

Note

This function supports backward but it is only fast when `(input, tau)` do not require gradients
and/or `tau.size(-1)` is very small.
``

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, mn, k) where * is zero or more batch dimensions
and mn equals to m or n depending on the `left`.
- **tau** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, min(mn, k)) where * is zero or more batch dimensions.
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, m, n) where * is zero or more batch dimensions.
- **left** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - controls the order of multiplication.
- **transpose** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - controls whether the matrix Q is conjugate transposed or not.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output Tensor. Ignored if None. Default: None.