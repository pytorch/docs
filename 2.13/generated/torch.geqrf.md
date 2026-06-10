# torch.geqrf

torch.geqrf(*input*, ***, *out=None*)

This is a low-level function for calling LAPACK's geqrf directly. This function
returns a namedtuple (a, tau) as defined in [LAPACK documentation for geqrf](http://www.netlib.org/lapack/explore-html/df/dc5/group__variants_g_ecomputational_ga3766ea903391b5cf9008132f7440ec7b.html) .

Computes a QR decomposition of `input`.
Both Q and R matrices are stored in the same output tensor a.
The elements of R are stored on and above the diagonal.
Elementary reflectors (or Householder vectors) implicitly defining matrix Q
are stored below the diagonal.
The results of this function can be used together with [`torch.linalg.householder_product()`](torch.linalg.householder_product.html#torch.linalg.householder_product)
to obtain the Q matrix or
with [`torch.ormqr()`](torch.ormqr.html#torch.ormqr), which uses an implicit representation of the Q matrix,
for an efficient matrix-matrix multiplication.

See [LAPACK documentation for geqrf](http://www.netlib.org/lapack/explore-html/df/dc5/group__variants_g_ecomputational_ga3766ea903391b5cf9008132f7440ec7b.html) for further details.

Note

See also [`torch.linalg.qr()`](torch.linalg.qr.html#torch.linalg.qr), which computes Q and R matrices, and [`torch.linalg.lstsq()`](torch.linalg.lstsq.html#torch.linalg.lstsq)
with the `driver="gels"` option for a function that can solve matrix equations using a QR decomposition.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input matrix

Keyword Arguments:

**out** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - the output tuple of (Tensor, Tensor). Ignored if None. Default: None.