# SparseSemiStructuredTensorCUTLASS

*class*torch.sparse.semi_structured.SparseSemiStructuredTensorCUTLASS(*shape*, *packed*, *meta*, *packed_t*, *meta_t*, *compressed_swizzled_bitmask*, *fuse_transpose_cusparselt=False*, *alg_id_cusparselt=0*, *requires_grad=False*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/sparse/semi_structured.py#L380)

This class implements semi-structured sparsity for the CUTLASS backend.

In this implementation, the specified elements and metadata are stored separately,
in packed and meta respectively.

When _FORCE_CUTLASS is set, or when cuSPARSELt is not available, this subclass calls into _sparse_semi_structured_(mm|addmm) and
sparse_semi_structured_from_dense for conversion to the compressed format.

H

Returns a view of a matrix (2-D tensor) conjugated and transposed.

`x.H` is equivalent to `x.transpose(0, 1).conj()` for complex matrices and
`x.transpose(0, 1)` for real matrices.

See also

[`mH`](../tensors.html#torch.Tensor.mH): An attribute that also works on batches of matrices.

T

Returns a view of this tensor with its dimensions reversed.

If `n` is the number of dimensions in `x`,
`x.T` is equivalent to `x.permute(n-1, n-2, ..., 0)`.

Warning

The use of `Tensor.T` on tensors of dimension other than 2 to reverse their shape
is deprecated and it will throw an error in a future release. Consider [`mT`](../tensors.html#torch.Tensor.mT)
to transpose batches of matrices or x.permute(*torch.arange(x.ndim - 1, -1, -1)) to reverse
the dimensions of a tensor.

abs() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.abs()`](torch.abs.html#torch.abs)

abs_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `abs()`

absolute() → [Tensor](../tensors.html#torch.Tensor)

Alias for `abs()`

absolute_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `absolute()`
Alias for `abs_()`

acos() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.acos()`](torch.acos.html#torch.acos)

acos_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `acos()`

acosh() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.acosh()`](torch.acosh.html#torch.acosh)

acosh_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `acosh()`

add(*other*, ***, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

Add a scalar or tensor to `self` tensor. If both `alpha`
and `other` are specified, each element of `other` is scaled by
`alpha` before being used.

When `other` is a tensor, the shape of `other` must be
[broadcastable](../notes/broadcasting.html#broadcasting-semantics) with the shape of the underlying
tensor

See [`torch.add()`](torch.add.html#torch.add)

add_(*other*, ***, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `add()`

addbmm(*batch1*, *batch2*, ***, *beta=1*, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.addbmm()`](torch.addbmm.html#torch.addbmm)

addbmm_(*batch1*, *batch2*, ***, *beta=1*, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `addbmm()`

addcdiv(*tensor1*, *tensor2*, ***, *value=1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.addcdiv()`](torch.addcdiv.html#torch.addcdiv)

addcdiv_(*tensor1*, *tensor2*, ***, *value=1*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `addcdiv()`

addcmul(*tensor1*, *tensor2*, ***, *value=1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.addcmul()`](torch.addcmul.html#torch.addcmul)

addcmul_(*tensor1*, *tensor2*, ***, *value=1*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `addcmul()`

addmm(*mat1*, *mat2*, ***, *beta=1*, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.addmm()`](torch.addmm.html#torch.addmm)

addmm_(*mat1*, *mat2*, ***, *beta=1*, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `addmm()`

addmv(*mat*, *vec*, ***, *beta=1*, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.addmv()`](torch.addmv.html#torch.addmv)

addmv_(*mat*, *vec*, ***, *beta=1*, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `addmv()`

addr(*vec1*, *vec2*, ***, *beta=1*, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.addr()`](torch.addr.html#torch.addr)

addr_(*vec1*, *vec2*, ***, *beta=1*, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `addr()`

adjoint() → [Tensor](../tensors.html#torch.Tensor)

Alias for `adjoint()`

all(*dim=None*, *keepdim=False*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.all()`](torch.all.html#torch.all)

allclose(*other*, *rtol=1e-05*, *atol=1e-08*, *equal_nan=False*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.allclose()`](torch.allclose.html#torch.allclose)

amax(*dim=None*, *keepdim=False*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.amax()`](torch.amax.html#torch.amax)

amin(*dim=None*, *keepdim=False*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.amin()`](torch.amin.html#torch.amin)

aminmax(***, *dim=None*, *keepdim=False) -> (Tensor min*, *Tensor max*)

See [`torch.aminmax()`](torch.aminmax.html#torch.aminmax)

angle() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.angle()`](torch.angle.html#torch.angle)

any(*dim=None*, *keepdim=False*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.any()`](torch.any.html#torch.any)

apply_(*callable*) → [Tensor](../tensors.html#torch.Tensor)

Applies the function `callable` to each element in the tensor, replacing
each element with the value returned by `callable`.

Note

This function only works with CPU tensors and should not be used in code
sections that require high performance.

arccos() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.arccos()`](torch.arccos.html#torch.arccos)

arccos_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `arccos()`

arccosh()

acosh() -> Tensor

See [`torch.arccosh()`](torch.arccosh.html#torch.arccosh)

arccosh_()

acosh_() -> Tensor

In-place version of `arccosh()`

arcsin() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.arcsin()`](torch.arcsin.html#torch.arcsin)

arcsin_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `arcsin()`

arcsinh() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.arcsinh()`](torch.arcsinh.html#torch.arcsinh)

arcsinh_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `arcsinh()`

arctan() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.arctan()`](torch.arctan.html#torch.arctan)

arctan2(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.arctan2()`](torch.arctan2.html#torch.arctan2)

arctan2_()

atan2_(other) -> Tensor

In-place version of `arctan2()`

arctan_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `arctan()`

arctanh() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.arctanh()`](torch.arctanh.html#torch.arctanh)

arctanh_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `arctanh()`

argmax(*dim=None*, *keepdim=False*) → LongTensor

See [`torch.argmax()`](torch.argmax.html#torch.argmax)

argmin(*dim=None*, *keepdim=False*) → LongTensor

See [`torch.argmin()`](torch.argmin.html#torch.argmin)

argsort(*dim=-1*, *descending=False*) → LongTensor

See [`torch.argsort()`](torch.argsort.html#torch.argsort)

argwhere() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.argwhere()`](torch.argwhere.html#torch.argwhere)

as_strided(*size*, *stride*, *storage_offset=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.as_strided()`](torch.as_strided.html#torch.as_strided)

as_strided_(*size*, *stride*, *storage_offset=None*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `as_strided()`

as_strided_scatter(*src*, *size*, *stride*, *storage_offset=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.as_strided_scatter()`](torch.as_strided_scatter.html#torch.as_strided_scatter)

as_subclass(*cls*) → [Tensor](../tensors.html#torch.Tensor)

Makes a `cls` instance with the same data pointer as `self`. Changes
in the output mirror changes in `self`, and the output stays attached
to the autograd graph. `cls` must be a subclass of `Tensor`.

asin() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.asin()`](torch.asin.html#torch.asin)

asin_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `asin()`

asinh() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.asinh()`](torch.asinh.html#torch.asinh)

asinh_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `asinh()`

atan() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.atan()`](torch.atan.html#torch.atan)

atan2(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.atan2()`](torch.atan2.html#torch.atan2)

atan2_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `atan2()`

atan_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `atan()`

atanh() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.atanh()`](torch.atanh.html#torch.atanh)

atanh_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `atanh()`

backward(*gradient=None*, *retain_graph=None*, *create_graph=False*, *inputs=None*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L566)

Computes the gradient of current tensor wrt graph leaves.

The graph is differentiated using the chain rule. If the tensor is
non-scalar (i.e. its data has more than one element) and requires
gradient, the function additionally requires specifying a `gradient`.
It should be a tensor of matching type and shape, that represents
the gradient of the differentiated function w.r.t. `self`.

This function accumulates gradients in the leaves - you might need to zero
`.grad` attributes or set them to `None` before calling it.
See [Default gradient layouts](../autograd.html#default-grad-layouts)
for details on the memory layout of accumulated gradients.

Note

If you run any forward ops, create `gradient`, and/or call `backward`
in a user-specified CUDA stream context, see
[Stream semantics of backward passes](../notes/cuda.html#bwd-cuda-stream-semantics).

Note

When `inputs` are provided and a given input is not a leaf,
the current implementation will call its grad_fn (though it is not strictly needed to get this gradients).
It is an implementation detail on which the user should not rely.
See [pytorch/pytorch#60521](https://github.com/pytorch/pytorch/pull/60521#issuecomment-867061780) for more details.

Parameters:

- **gradient** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - The gradient of the function
being differentiated w.r.t. `self`.
This argument can be omitted if `self` is a scalar. Defaults to `None`.
- **retain_graph** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `False`, the graph used to compute the grads will be freed;
If `True`, it will be retained. The default is `None`, in which case the value is inferred from `create_graph`
(i.e., the graph is retained only when higher-order derivative tracking is requested). Note that in nearly all cases
setting this option to True is not needed and often can be worked around in a much more efficient way.
- **create_graph** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `True`, graph of the derivative will
be constructed, allowing to compute higher order derivative
products. Defaults to `False`.
- **inputs** (*Sequence**[*[*Tensor*](../tensors.html#torch.Tensor)*] or*[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*Tensor*](../tensors.html#torch.Tensor)*]**,**optional*) - Inputs w.r.t. which
the gradient will be accumulated into `.grad`. All other tensors will be
ignored. If not provided, the gradient is accumulated into all the leaf
Tensors that were used to compute the `tensors`. A dict of tensors
(e.g. `dict(model.named_parameters())`) is also accepted.
Defaults to `None`.

baddbmm(*batch1*, *batch2*, ***, *beta=1*, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.baddbmm()`](torch.baddbmm.html#torch.baddbmm)

baddbmm_(*batch1*, *batch2*, ***, *beta=1*, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `baddbmm()`

bernoulli(***, *generator=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns a result tensor where each result[i]\texttt{result[i]}result[i] is independently
sampled from Bernoulli(self[i])\text{Bernoulli}(\texttt{self[i]})Bernoulli(self[i]). `self` must have
floating point `dtype`, and the result will have the same `dtype`.

See [`torch.bernoulli()`](torch.bernoulli.html#torch.bernoulli)

bernoulli_(*p=0.5*, ***, *generator=None*) → [Tensor](../tensors.html#torch.Tensor)

Fills each location of `self` with an independent sample from
Bernoulli(p)\text{Bernoulli}(\texttt{p})Bernoulli(p). `self` can have integral
`dtype`.

`p` should either be a scalar or tensor containing probabilities to be
used for drawing the binary random number.

If it is a tensor, the ith\text{i}^{th}ith element of `self` tensor
will be set to a value sampled from
Bernoulli(p_tensor[i])\text{Bernoulli}(\texttt{p\_tensor[i]})Bernoulli(p_tensor[i]). In this case p must have
floating point `dtype`.

See also `bernoulli()` and [`torch.bernoulli()`](torch.bernoulli.html#torch.bernoulli)

bfloat16(*memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

`self.bfloat16()` is equivalent to `self.to(torch.bfloat16)`. See `to()`.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

bincount(*weights=None*, *minlength=0*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.bincount()`](torch.bincount.html#torch.bincount)

bitwise_and() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.bitwise_and()`](torch.bitwise_and.html#torch.bitwise_and)

bitwise_and_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `bitwise_and()`

bitwise_left_shift(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.bitwise_left_shift()`](torch.bitwise_left_shift.html#torch.bitwise_left_shift)

bitwise_left_shift_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `bitwise_left_shift()`

bitwise_not() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.bitwise_not()`](torch.bitwise_not.html#torch.bitwise_not)

bitwise_not_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `bitwise_not()`

bitwise_or() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.bitwise_or()`](torch.bitwise_or.html#torch.bitwise_or)

bitwise_or_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `bitwise_or()`

bitwise_right_shift(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.bitwise_right_shift()`](torch.bitwise_right_shift.html#torch.bitwise_right_shift)

bitwise_right_shift_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `bitwise_right_shift()`

bitwise_xor() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.bitwise_xor()`](torch.bitwise_xor.html#torch.bitwise_xor)

bitwise_xor_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `bitwise_xor()`

bmm(*batch2*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.bmm()`](torch.bmm.html#torch.bmm)

bool(*memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

`self.bool()` is equivalent to `self.to(torch.bool)`. See `to()`.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

broadcast_to(*shape*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.broadcast_to()`](torch.broadcast_to.html#torch.broadcast_to).

byte(*memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

`self.byte()` is equivalent to `self.to(torch.uint8)`. See `to()`.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

cauchy_(*median=0*, *sigma=1*, ***, *generator=None*) → [Tensor](../tensors.html#torch.Tensor)

Fills the tensor with numbers drawn from the Cauchy distribution:

f(x)=1πσ(x−median)2+σ2f(x) = \dfrac{1}{\pi} \dfrac{\sigma}{(x - \text{median})^2 + \sigma^2}f(x)=π1​(x−median)2+σ2σ​

Note

Sigma (σ\sigmaσ) is used to denote the scale parameter in Cauchy distribution.

cdouble(*memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

`self.cdouble()` is equivalent to `self.to(torch.complex128)`. See `to()`.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

ceil() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.ceil()`](torch.ceil.html#torch.ceil)

ceil_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `ceil()`

cfloat(*memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

`self.cfloat()` is equivalent to `self.to(torch.complex64)`. See `to()`.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

chalf(*memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

`self.chalf()` is equivalent to `self.to(torch.complex32)`. See `to()`.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

char(*memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

`self.char()` is equivalent to `self.to(torch.int8)`. See `to()`.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

cholesky_inverse(*upper=False*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.cholesky_inverse()`](torch.cholesky_inverse.html#torch.cholesky_inverse)

cholesky_solve(*input2*, *upper=False*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.cholesky_solve()`](torch.cholesky_solve.html#torch.cholesky_solve)

chunk(*chunks*, *dim=0*) → List of Tensors

See [`torch.chunk()`](torch.chunk.html#torch.chunk)

clamp(*min=None*, *max=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.clamp()`](torch.clamp.html#torch.clamp)

clamp_(*min=None*, *max=None*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `clamp()`

clip(*min=None*, *max=None*) → [Tensor](../tensors.html#torch.Tensor)

Alias for `clamp()`.

clip_(*min=None*, *max=None*) → [Tensor](../tensors.html#torch.Tensor)

Alias for `clamp_()`.

clone(***, *memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.clone()`](torch.clone.html#torch.clone)

coalesce() → [Tensor](../tensors.html#torch.Tensor)

Returns a coalesced copy of `self` if `self` is an
[uncoalesced tensor](../sparse.html#sparse-uncoalesced-coo-docs).

Returns `self` if `self` is a coalesced tensor.

Warning

Throws an error if `self` is not a sparse COO tensor.

col_indices() → IntTensor

Returns the tensor containing the column indices of the `self`
tensor when `self` is a sparse CSR tensor of layout `sparse_csr`.
The `col_indices` tensor is strictly of shape (`self`.nnz())
and of type `int32` or `int64`. When using MKL routines such as sparse
matrix multiplication, it is necessary to use `int32` indexing in order
to avoid downcasting and potentially losing information.

Example:

```
>>> csr = torch.eye(5,5).to_sparse_csr()
>>> csr.col_indices()
tensor([0, 1, 2, 3, 4], dtype=torch.int32)
```

conj() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.conj()`](torch.conj.html#torch.conj)

conj_physical() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.conj_physical()`](torch.conj_physical.html#torch.conj_physical)

conj_physical_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `conj_physical()`

const_data_ptr() → [int](https://docs.python.org/3/library/functions.html#int)

Returns the address of the first element of `self` tensor.

Unlike `data_ptr()`, this is guaranteed to be a read-only access
that will not trigger copy-on-write materialization. For regular
(non-COW) tensors, the return value is identical to `data_ptr()`.

Warning

The returned pointer must not be used to mutate the tensor data.
Use `data_ptr()` when write access is needed.

contiguous(*memory_format=torch.contiguous_format*) → [Tensor](../tensors.html#torch.Tensor)

Returns a contiguous in memory tensor containing the same data as `self` tensor. If
`self` tensor is already in the specified memory format, this function returns the
`self` tensor.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.contiguous_format`.

copy_(*src*, *non_blocking=False*) → [Tensor](../tensors.html#torch.Tensor)

Copies the elements from `src` into `self` tensor and returns
`self`.

The `src` tensor must be [broadcastable](../notes/broadcasting.html#broadcasting-semantics)
with the `self` tensor. It may be of a different data type or reside on a
different device.

Parameters:

- **src** ([*Tensor*](../tensors.html#torch.Tensor)) - the source tensor to copy from
- **non_blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - if `True` and this copy is between CPU and GPU,
the copy may occur asynchronously with respect to the host. For other
cases, this argument has no effect. Default: `False`

Note

When `non_blocking` is `True` and the copy is issued on a
non-default CUDA stream, the caller is responsible for proper
cross-stream synchronization. See [CUDA streams](../notes/cuda.html#cuda-stream-semantics) for
the required pattern.

copysign(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.copysign()`](torch.copysign.html#torch.copysign)

copysign_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `copysign()`

corrcoef() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.corrcoef()`](torch.corrcoef.html#torch.corrcoef)

cos() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.cos()`](torch.cos.html#torch.cos)

cos_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `cos()`

cosh() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.cosh()`](torch.cosh.html#torch.cosh)

cosh_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `cosh()`

count_nonzero(*dim=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.count_nonzero()`](torch.count_nonzero.html#torch.count_nonzero)

cov(***, *correction=1*, *fweights=None*, *aweights=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.cov()`](torch.cov.html#torch.cov)

cpu(*memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

Returns a copy of this object in CPU memory.

If this object is already in CPU memory,
then no copy is performed and the original object is returned.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

cross(*other*, *dim=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.cross()`](torch.cross.html#torch.cross)

crow_indices() → IntTensor

Returns the tensor containing the compressed row indices of the `self`
tensor when `self` is a sparse CSR tensor of layout `sparse_csr`.
The `crow_indices` tensor is strictly of shape (`self`.size(0) + 1)
and of type `int32` or `int64`. When using MKL routines such as sparse
matrix multiplication, it is necessary to use `int32` indexing in order
to avoid downcasting and potentially losing information.

Example:

```
>>> csr = torch.eye(5,5).to_sparse_csr()
>>> csr.crow_indices()
tensor([0, 1, 2, 3, 4, 5], dtype=torch.int32)
```

cuda(*device=None*, *non_blocking=False*, *memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

Returns a copy of this object in CUDA memory.

If this object is already in CUDA memory and on the correct device,
then no copy is performed and the original object is returned.

Parameters:

- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - The destination GPU device.
Defaults to the current CUDA device.
- **non_blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `True` and the source is in pinned memory,
the copy will be asynchronous with respect to the host.
Otherwise, the argument has no effect. Default: `False`.
- **memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

cummax(*dim*)

See [`torch.cummax()`](torch.cummax.html#torch.cummax)

cummin(*dim*)

See [`torch.cummin()`](torch.cummin.html#torch.cummin)

cumprod(*dim*, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.cumprod()`](torch.cumprod.html#torch.cumprod)

cumprod_(*dim*, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `cumprod()`

cumsum(*dim*, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.cumsum()`](torch.cumsum.html#torch.cumsum)

cumsum_(*dim*, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `cumsum()`

data_ptr() → [int](https://docs.python.org/3/library/functions.html#int)

Returns the address of the first element of `self` tensor.

Note

If the tensor is a copy-on-write tensor (e.g. created via
`_lazy_clone()`), calling this method will materialize the
copy. Use `const_data_ptr()` if you only need read-only access
to the data pointer.

deg2rad() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.deg2rad()`](torch.deg2rad.html#torch.deg2rad)

deg2rad_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `deg2rad()`

dense_dim() → [int](https://docs.python.org/3/library/functions.html#int)

Return the number of dense dimensions in a [sparse tensor](../sparse.html#sparse-docs) `self`.

Note

Returns `len(self.shape)` if `self` is not a sparse tensor.

See also `Tensor.sparse_dim()` and [hybrid tensors](../sparse.html#sparse-hybrid-coo-docs).

dequantize() → [Tensor](../tensors.html#torch.Tensor)

Given a quantized Tensor, dequantize it and return the dequantized float Tensor.

det() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.det()`](torch.det.html#torch.det)

detach()

Returns a new Tensor, detached from the current graph.

The result will never require gradient.

This method also affects forward mode AD gradients and the result will never
have forward mode AD gradients.

Note

Returned Tensor shares the same storage with the original one.
In-place modifications on either of them will be seen, and may trigger
errors in correctness checks.

detach_()

Detaches the Tensor from the graph that created it, making it a leaf.
Views cannot be detached in-place.

This method also affects forward mode AD gradients and the result will never
have forward mode AD gradients.

device

Is the [`torch.device`](../tensor_attributes.html#torch.device) where this Tensor is.

diag(*diagonal=0*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.diag()`](torch.diag.html#torch.diag)

diag_embed(*offset=0*, *dim1=-2*, *dim2=-1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.diag_embed()`](torch.diag_embed.html#torch.diag_embed)

diagflat(*offset=0*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.diagflat()`](torch.diagflat.html#torch.diagflat)

diagonal(*offset=0*, *dim1=0*, *dim2=1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.diagonal()`](torch.diagonal.html#torch.diagonal)

diagonal_scatter(*src*, *offset=0*, *dim1=0*, *dim2=1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.diagonal_scatter()`](torch.diagonal_scatter.html#torch.diagonal_scatter)

diff(*n=1*, *dim=-1*, *prepend=None*, *append=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.diff()`](torch.diff.html#torch.diff)

digamma() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.digamma()`](torch.digamma.html#torch.digamma)

digamma_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `digamma()`

dim() → [int](https://docs.python.org/3/library/functions.html#int)

Returns the number of dimensions of `self` tensor.

dim_order(*ambiguity_check=False*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L1381)

Returns the uniquely determined tuple of int describing the dim order or
physical layout of `self`.

The dim order represents how dimensions are laid out in memory of dense tensors,
starting from the outermost to the innermost dimension.

Note that the dim order may not always be uniquely determined.
If ambiguity_check is True, this function raises a RuntimeError when the dim order cannot be uniquely determined;
If ambiguity_check is a list of memory formats, this function raises a RuntimeError when tensor can not be interpreted
into exactly one of the given memory formats, or it cannot be uniquely determined.
If ambiguity_check is False, it will return one of legal dim order(s) without checking its uniqueness.
Otherwise, it will raise TypeError.

Parameters:

**ambiguity_check** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*or**List**[*[*torch.memory_format*](../tensor_attributes.html#torch.memory_format)*]*) - The check method for ambiguity of dim order.

Examples:

```
>>> torch.empty((2, 3, 5, 7)).dim_order()
(0, 1, 2, 3)
>>> torch.empty((2, 3, 5, 7)).transpose(1, 2).dim_order()
(0, 2, 1, 3)
>>> torch.empty((2, 3, 5, 7), memory_format=torch.channels_last).dim_order()
(0, 2, 3, 1)
>>> torch.empty((1, 2, 3, 4)).dim_order()
(0, 1, 2, 3)
>>> try:
... torch.empty((1, 2, 3, 4)).dim_order(ambiguity_check=True)
... except RuntimeError as e:
... print(e)
The tensor does not have unique dim order, or cannot map to exact one of the given memory formats.
>>> torch.empty((1, 2, 3, 4)).dim_order(
... ambiguity_check=[torch.contiguous_format, torch.channels_last]
... ) # It can be mapped to contiguous format
(0, 1, 2, 3)
>>> try:
... torch.empty((1, 2, 3, 4)).dim_order(ambiguity_check="ILLEGAL") # type: ignore[arg-type]
... except TypeError as e:
... print(e)
The ambiguity_check argument must be a bool or a list of memory formats.
```

Warning

The dim_order tensor API is experimental and subject to change.

dist(*other*, *p=2*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.dist()`](torch.dist.html#torch.dist)

div(*value*, ***, *rounding_mode=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.div()`](torch.div.html#torch.div)

div_(*value*, ***, *rounding_mode=None*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `div()`

divide(*value*, ***, *rounding_mode=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.divide()`](torch.divide.html#torch.divide)

divide_(*value*, ***, *rounding_mode=None*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `divide()`

dot(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.dot()`](torch.dot.html#torch.dot)

double(*memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

`self.double()` is equivalent to `self.to(torch.float64)`. See `to()`.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

dsplit(*split_size_or_sections*) → List of Tensors

See [`torch.dsplit()`](torch.dsplit.html#torch.dsplit)

element_size() → [int](https://docs.python.org/3/library/functions.html#int)

Returns the size in bytes of an individual element.

Example:

```
>>> torch.tensor([]).element_size()
4
>>> torch.tensor([], dtype=torch.uint8).element_size()
1
```

eq(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.eq()`](torch.eq.html#torch.eq)

eq_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `eq()`

equal(*other*) → [bool](https://docs.python.org/3/library/functions.html#bool)

See [`torch.equal()`](torch.equal.html#torch.equal)

erf() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.erf()`](torch.erf.html#torch.erf)

erf_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `erf()`

erfc() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.erfc()`](torch.erfc.html#torch.erfc)

erfc_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `erfc()`

erfinv() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.erfinv()`](torch.erfinv.html#torch.erfinv)

erfinv_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `erfinv()`

exp() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.exp()`](torch.exp.html#torch.exp)

exp2() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.exp2()`](torch.exp2.html#torch.exp2)

exp2_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `exp2()`

exp_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `exp()`

expand(**size*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new view of the `self` tensor with singleton dimensions expanded
to a larger size.

Passing -1 as the size for a dimension means not changing the size of
that dimension.

Tensor can be also expanded to a larger number of dimensions, and the
new ones will be appended at the front. For the new dimensions, the
size cannot be set to -1.

Expanding a tensor does not allocate new memory, but only creates a
new view on the existing tensor where a dimension of size one is
expanded to a larger size by setting the `stride` to 0. Any dimension
of size 1 can be expanded to an arbitrary value without allocating new
memory.

Note

Operations on an expanded view may still allocate memory if they need to
materialize the expanded values. For example, changing dtype after
`expand()` can allocate memory for the full expanded shape.

Parameters:

***size** ([*torch.Size*](../size.html#torch.Size)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*...*) - the desired expanded size

Warning

More than one element of an expanded tensor may refer to a single
memory location. As a result, in-place operations (especially ones that
are vectorized) may result in incorrect behavior. If you need to write
to the tensors, please clone them first.

Example:

```
>>> x = torch.tensor([[1], [2], [3]])
>>> x.size()
torch.Size([3, 1])
>>> x.expand(3, 4)
tensor([[ 1, 1, 1, 1],
 [ 2, 2, 2, 2],
 [ 3, 3, 3, 3]])
>>> x.expand(-1, 4) # -1 means not changing the size of that dimension
tensor([[ 1, 1, 1, 1],
 [ 2, 2, 2, 2],
 [ 3, 3, 3, 3]])
```

expand_as(*other*) → [Tensor](../tensors.html#torch.Tensor)

Expand this tensor to the same size as `other`.
`self.expand_as(other)` is equivalent to `self.expand(other.size())`.

Please see `expand()` for more information about `expand`.

Parameters:

**other** ([`torch.Tensor`](../tensors.html#torch.Tensor)) - The result tensor has the same size
as `other`.

expm1() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.expm1()`](torch.expm1.html#torch.expm1)

expm1_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `expm1()`

exponential_(*lambd=1*, ***, *generator=None*) → [Tensor](../tensors.html#torch.Tensor)

Fills `self` tensor with elements drawn from the PDF (probability density function):

f(x)=λe−λx,x>0f(x) = \lambda e^{-\lambda x}, x > 0f(x)=λe−λx,x>0

Note

In probability theory, exponential distribution is supported on interval [0, inf⁡\infinf) (i.e., x>=0x >= 0x>=0)
implying that zero can be sampled from the exponential distribution.
However, [`torch.Tensor.exponential_()`](torch.Tensor.exponential_.html#torch.Tensor.exponential_) does not sample zero,
which means that its actual support is the interval (0, inf⁡\infinf).

Note that [`torch.distributions.exponential.Exponential()`](../distributions.html#torch.distributions.exponential.Exponential) is supported on the interval [0, inf⁡\infinf) and can sample zero.

fill_(*value*) → [Tensor](../tensors.html#torch.Tensor)

Fills `self` tensor with the specified value.

fill_diagonal_(*fill_value*, *wrap=False*) → [Tensor](../tensors.html#torch.Tensor)

Fill the main diagonal of a tensor that has at least 2-dimensions.
When dims>2, all dimensions of input must be of equal length.
This function modifies the input tensor in-place, and returns the input tensor.

Parameters:

- **fill_value** (*Scalar*) - the fill value
- **wrap** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - the diagonal 'wrapped' after N columns for tall matrices. Default: `False`

Example:

```
>>> a = torch.zeros(3, 3)
>>> a.fill_diagonal_(5)
tensor([[5., 0., 0.],
 [0., 5., 0.],
 [0., 0., 5.]])
>>> b = torch.zeros(7, 3)
>>> b.fill_diagonal_(5)
tensor([[5., 0., 0.],
 [0., 5., 0.],
 [0., 0., 5.],
 [0., 0., 0.],
 [0., 0., 0.],
 [0., 0., 0.],
 [0., 0., 0.]])
>>> c = torch.zeros(7, 3)
>>> c.fill_diagonal_(5, wrap=True)
tensor([[5., 0., 0.],
 [0., 5., 0.],
 [0., 0., 5.],
 [0., 0., 0.],
 [5., 0., 0.],
 [0., 5., 0.],
 [0., 0., 5.]])
```

fix() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.fix()`](torch.fix.html#torch.fix).

fix_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `fix()`

flatten(*start_dim=0*, *end_dim=-1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.flatten()`](torch.flatten.html#torch.flatten)

flip(*dims*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.flip()`](torch.flip.html#torch.flip)

fliplr() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.fliplr()`](torch.fliplr.html#torch.fliplr)

flipud() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.flipud()`](torch.flipud.html#torch.flipud)

float(*memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

`self.float()` is equivalent to `self.to(torch.float32)`. See `to()`.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

float_power(*exponent*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.float_power()`](torch.float_power.html#torch.float_power)

float_power_(*exponent*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `float_power()`

floor() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.floor()`](torch.floor.html#torch.floor)

floor_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `floor()`

floor_divide(*value*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.floor_divide()`](torch.floor_divide.html#torch.floor_divide)

floor_divide_(*value*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `floor_divide()`

fmax(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.fmax()`](torch.fmax.html#torch.fmax)

fmin(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.fmin()`](torch.fmin.html#torch.fmin)

fmod(*divisor*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.fmod()`](torch.fmod.html#torch.fmod)

fmod_(*divisor*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `fmod()`

frac() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.frac()`](torch.frac.html#torch.frac)

frac_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `frac()`

frexp(*input) -> (Tensor mantissa*, *Tensor exponent*)

See [`torch.frexp()`](torch.frexp.html#torch.frexp)

gather(*dim*, *index*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.gather()`](torch.gather.html#torch.gather)

gcd(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.gcd()`](torch.gcd.html#torch.gcd)

gcd_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `gcd()`

ge(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.ge()`](torch.ge.html#torch.ge).

ge_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `ge()`.

geometric_(*p*, ***, *generator=None*) → [Tensor](../tensors.html#torch.Tensor)

Fills `self` tensor with elements drawn from the geometric distribution:

P(X=k)=(1−p)k−1p,k=1,2,...P(X=k) = (1 - p)^{k - 1} p, k = 1, 2, ...P(X=k)=(1−p)k−1p,k=1,2,...

Note

[`torch.Tensor.geometric_()`](torch.Tensor.geometric_.html#torch.Tensor.geometric_) k-th trial is the first success hence draws samples in {1,2,...}\{1, 2, \ldots\}{1,2,...}, whereas
[`torch.distributions.geometric.Geometric()`](../distributions.html#torch.distributions.geometric.Geometric) (k+1)(k+1)(k+1)-th trial is the first success
hence draws samples in {0,1,...}\{0, 1, \ldots\}{0,1,...}.

geqrf()

See [`torch.geqrf()`](torch.geqrf.html#torch.geqrf)

ger(*vec2*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.ger()`](torch.ger.html#torch.ger)

get_device(*) -> Device ordinal (Integer*)

For CUDA tensors, this function returns the device ordinal of the GPU on which the tensor resides.
For CPU tensors, this function returns -1.

Example:

```
>>> x = torch.randn(3, 4, 5, device='cuda:0')
>>> x.get_device()
0
>>> x.cpu().get_device()
-1
```

grad

This attribute is `None` by default and becomes a Tensor the first time a call to
`backward()` computes gradients for `self`.
The attribute will then contain the gradients computed and future calls to
`backward()` will accumulate (add) gradients into it.

grad_dtype

The allowed dtype of :attr:`grad` for this tensor.

:attr:`grad_dtype` can be set to a specific dtype or `None`. By default,
`t.grad_dtype == t.dtype`. When not None, the autograd engine casts
incoming gradients to this dtype. This attribute is only accessible and
settable for leaf tensors.

Warning

Use with caution. Diverging the dtypes of a tensor and its gradient may
break downstream systems that assume they match.

Example:

```
>>> x = torch.tensor([1.0, 2.0], requires_grad=True)
>>> x.grad_dtype
torch.float32

>>> x.grad_dtype = torch.float16
>>> x.grad_dtype
torch.float16

>>> # Allow any gradient dtype
>>> x.grad_dtype = None
>>> x.grad_dtype
```

greater(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.greater()`](torch.greater.html#torch.greater).

greater_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `greater()`.

greater_equal(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.greater_equal()`](torch.greater_equal.html#torch.greater_equal).

greater_equal_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `greater_equal()`.

gt(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.gt()`](torch.gt.html#torch.gt).

gt_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `gt()`.

half(*memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

`self.half()` is equivalent to `self.to(torch.float16)`. See `to()`.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

hardshrink(*lambd=0.5*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.nn.functional.hardshrink()`](torch.nn.functional.hardshrink.html#torch.nn.functional.hardshrink)

heaviside(*values*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.heaviside()`](torch.heaviside.html#torch.heaviside)

heaviside_(*values*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `heaviside()`

histc(*bins=100*, *min=0*, *max=0*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.histc()`](torch.histc.html#torch.histc)

histogram(*input*, *bins*, ***, *range=None*, *weight=None*, *density=False*)

See [`torch.histogram()`](torch.histogram.html#torch.histogram)

hsplit(*split_size_or_sections*) → List of Tensors

See [`torch.hsplit()`](torch.hsplit.html#torch.hsplit)

hypot(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.hypot()`](torch.hypot.html#torch.hypot)

hypot_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `hypot()`

i0() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.i0()`](torch.i0.html#torch.i0)

i0_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `i0()`

igamma(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.igamma()`](torch.igamma.html#torch.igamma)

igamma_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `igamma()`

igammac(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.igammac()`](torch.igammac.html#torch.igammac)

igammac_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `igammac()`

imag

Returns a new tensor containing imaginary values of the `self` tensor.
The returned tensor and `self` share the same underlying storage.

Warning

`imag()` is only supported for tensors with complex dtypes.

Example:

```
>>> x=torch.randn(4, dtype=torch.cfloat)
>>> x
tensor([(0.3100+0.3553j), (-0.5445-0.7896j), (-1.6492-0.0633j), (-0.0638-0.8119j)])
>>> x.imag
tensor([ 0.3553, -0.7896, -0.0633, -0.8119])
```

index(*positions*, *dims*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L627)

Index a regular tensor by binding specified positions to dims.

This converts a regular tensor to a first-class tensor by binding
the specified positional dimensions to Dim objects.

Parameters:

- **positions** - Tuple of dimension positions to bind
- **dims** - Dim objects or tuple of Dim objects to bind to

Returns:

First-class tensor with specified dimensions bound

index_add(*dim*, *index*, *source*, ***, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

Out-of-place version of [`torch.Tensor.index_add_()`](torch.Tensor.index_add_.html#torch.Tensor.index_add_).

index_add_(*dim*, *index*, *source*, ***, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

Accumulate the elements of `alpha` times `source` into the `self`
tensor by adding to the indices in the order given in `index`. For example,
if `dim == 0`, `index[i] == j`, and `alpha=-1`, then the `i`th row of
`source` is subtracted from the `j`th row of `self`.

The `dim`th dimension of `source` must have the same size as the
length of `index` (which must be a vector), and all other dimensions must
match `self`, or an error will be raised.

For a 3-D tensor the output is given as:

```
self[index[i], :, :] += alpha * src[i, :, :] # if dim == 0
self[:, index[i], :] += alpha * src[:, i, :] # if dim == 1
self[:, :, index[i]] += alpha * src[:, :, i] # if dim == 2
```

Note

This operation may behave nondeterministically when given tensors on a CUDA device. See [Reproducibility](../notes/randomness.html) for more information.

Parameters:

- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - dimension along which to index
- **index** ([*Tensor*](../tensors.html#torch.Tensor)) - indices of `source` to select from,
should have dtype either torch.int64 or torch.int32
- **source** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor containing values to add

Keyword Arguments:

**alpha** (*Number*) - the scalar multiplier for `source`

Example:

```
>>> x = torch.ones(5, 3)
>>> t = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
>>> index = torch.tensor([0, 4, 2])
>>> x.index_add_(0, index, t)
tensor([[ 2., 3., 4.],
 [ 1., 1., 1.],
 [ 8., 9., 10.],
 [ 1., 1., 1.],
 [ 5., 6., 7.]])
>>> x.index_add_(0, index, t, alpha=-1)
tensor([[ 1., 1., 1.],
 [ 1., 1., 1.],
 [ 1., 1., 1.],
 [ 1., 1., 1.],
 [ 1., 1., 1.]])
```

index_copy(*dim*, *index*, *tensor2*) → [Tensor](../tensors.html#torch.Tensor)

Out-of-place version of [`torch.Tensor.index_copy_()`](torch.Tensor.index_copy_.html#torch.Tensor.index_copy_).

index_copy_(*dim*, *index*, *tensor*) → [Tensor](../tensors.html#torch.Tensor)

Copies the elements of `tensor` into the `self` tensor by selecting
the indices in the order given in `index`. For example, if `dim == 0`
and `index[i] == j`, then the `i`th row of `tensor` is copied to the
`j`th row of `self`.

The `dim`th dimension of `tensor` must have the same size as the
length of `index` (which must be a vector), and all other dimensions must
match `self`, or an error will be raised.

Note

If `index` contains duplicate entries, multiple elements from
`tensor` will be copied to the same index of `self`. The result
is nondeterministic since it depends on which copy occurs last.

Parameters:

- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - dimension along which to index
- **index** (*LongTensor*) - indices of `tensor` to select from
- **tensor** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor containing values to copy

Example:

```
>>> x = torch.zeros(5, 3)
>>> t = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
>>> index = torch.tensor([0, 4, 2])
>>> x.index_copy_(0, index, t)
tensor([[ 1., 2., 3.],
 [ 0., 0., 0.],
 [ 7., 8., 9.],
 [ 0., 0., 0.],
 [ 4., 5., 6.]])
```

index_fill(*dim*, *index*, *value*) → [Tensor](../tensors.html#torch.Tensor)

Out-of-place version of [`torch.Tensor.index_fill_()`](torch.Tensor.index_fill_.html#torch.Tensor.index_fill_).

index_fill_(*dim*, *index*, *value*) → [Tensor](../tensors.html#torch.Tensor)

Fills the elements of the `self` tensor with value `value` by
selecting the indices in the order given in `index`.

Parameters:

- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - dimension along which to index
- **index** (*LongTensor*) - indices of `self` tensor to fill in
- **value** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the value to fill with

Example:

```
>>> x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
>>> index = torch.tensor([0, 2])
>>> x.index_fill_(1, index, -1)
tensor([[-1., 2., -1.],
 [-1., 5., -1.],
 [-1., 8., -1.]])
```

index_put(*indices*, *values*, *accumulate=False*) → [Tensor](../tensors.html#torch.Tensor)

Out-place version of `index_put_()`.

index_put_(*indices*, *values*, *accumulate=False*) → [Tensor](../tensors.html#torch.Tensor)

Puts values from the tensor `values` into the tensor `self` using
the indices specified in `indices` (which is a tuple of Tensors). The
expression `tensor.index_put_(indices, values)` is equivalent to
`tensor[indices] = values`. Returns `self`.

If `accumulate` is `True`, the elements in `values` are added to
`self`. If accumulate is `False`, the behavior is undefined if indices
contain duplicate elements.

Parameters:

- **indices** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**LongTensor*) - tensors used to index into self.
- **values** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of same dtype as self.
- **accumulate** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - whether to accumulate into self

index_reduce_(*dim*, *index*, *source*, *reduce*, ***, *include_self=True*) → [Tensor](../tensors.html#torch.Tensor)

Accumulate the elements of `source` into the `self`
tensor by accumulating to the indices in the order given in `index`
using the reduction given by the `reduce` argument. For example, if `dim == 0`,
`index[i] == j`, `reduce == prod` and `include_self == True` then the `i`th
row of `source` is multiplied by the `j`th row of `self`. If
`include_self="True"`, the values in the `self` tensor are included
in the reduction, otherwise, rows in the `self` tensor that are accumulated
to are treated as if they were filled with the reduction identities.

The `dim`th dimension of `source` must have the same size as the
length of `index` (which must be a vector), and all other dimensions must
match `self`, or an error will be raised.

For a 3-D tensor with `reduce="prod"` and `include_self=True` the
output is given as:

```
self[index[i], :, :] *= src[i, :, :] # if dim == 0
self[:, index[i], :] *= src[:, i, :] # if dim == 1
self[:, :, index[i]] *= src[:, :, i] # if dim == 2
```

Note

This operation may behave nondeterministically when given tensors on a CUDA device. See [Reproducibility](../notes/randomness.html) for more information.

Note

This function only supports floating point tensors.

Warning

This function is in beta and may change in the near future.

Parameters:

- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - dimension along which to index
- **index** ([*Tensor*](../tensors.html#torch.Tensor)) - indices of `self` to accumulate into,
should have dtype either torch.int64 or torch.int32
- **source** (*FloatTensor*) - the tensor containing values to accumulate
- **reduce** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - the reduction operation to apply
(`"prod"`, `"mean"`, `"amax"`, `"amin"`)

Keyword Arguments:

**include_self** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - whether the elements from the `self` tensor are
included in the reduction

Example:

```
>>> x = torch.empty(5, 3).fill_(2)
>>> t = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=torch.float)
>>> index = torch.tensor([0, 4, 2, 0])
>>> x.index_reduce_(0, index, t, 'prod')
tensor([[20., 44., 72.],
 [ 2., 2., 2.],
 [14., 16., 18.],
 [ 2., 2., 2.],
 [ 8., 10., 12.]])
>>> x = torch.empty(5, 3).fill_(2)
>>> x.index_reduce_(0, index, t, 'prod', include_self=False)
tensor([[10., 22., 36.],
 [ 2., 2., 2.],
 [ 7., 8., 9.],
 [ 2., 2., 2.],
 [ 4., 5., 6.]])
```

index_select(*dim*, *index*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.index_select()`](torch.index_select.html#torch.index_select)

indices() → [Tensor](../tensors.html#torch.Tensor)

Return the indices tensor of a [sparse COO tensor](../sparse.html#sparse-coo-docs).

Warning

Throws an error if `self` is not a sparse COO tensor.

See also `Tensor.values()`.

Note

This method can only be called on a coalesced sparse tensor. See
`Tensor.coalesce()` for details.

inner(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.inner()`](torch.inner.html#torch.inner).

int(*memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

`self.int()` is equivalent to `self.to(torch.int32)`. See `to()`.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

int_repr() → [Tensor](../tensors.html#torch.Tensor)

Given a quantized Tensor,
`self.int_repr()` returns a CPU Tensor with uint8_t as data type that stores the
underlying uint8_t values of the given Tensor.

inverse() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.inverse()`](torch.inverse.html#torch.inverse)

ipu(*device=None*, *non_blocking=False*, *memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

Returns a copy of this object in IPU memory.

If this object is already in IPU memory and on the correct device,
then no copy is performed and the original object is returned.

Parameters:

- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - The destination IPU device.
Defaults to the current IPU device.
- **non_blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `True` and the source is in pinned memory,
the copy will be asynchronous with respect to the host.
Otherwise, the argument has no effect. Default: `False`.
- **memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

is_coalesced() → [bool](https://docs.python.org/3/library/functions.html#bool)

Returns `True` if `self` is a [sparse COO tensor](../sparse.html#sparse-coo-docs) that is coalesced, `False` otherwise.

Warning

Throws an error if `self` is not a sparse COO tensor.

See `coalesce()` and [uncoalesced tensors](../sparse.html#sparse-uncoalesced-coo-docs).

is_complex() → [bool](https://docs.python.org/3/library/functions.html#bool)

Returns True if the data type of `self` is a complex data type.

is_conj() → [bool](https://docs.python.org/3/library/functions.html#bool)

Returns True if the conjugate bit of `self` is set to true.

is_contiguous(*memory_format=torch.contiguous_format*) → [bool](https://docs.python.org/3/library/functions.html#bool)

Returns True if `self` tensor is contiguous in memory in the order specified
by memory format.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - Specifies memory allocation
order. Default: `torch.contiguous_format`.

is_cpu

Is `True` if the Tensor is stored on the CPU, `False` otherwise.

is_cuda

Is `True` if the Tensor is stored on the GPU, `False` otherwise.

is_floating_point() → [bool](https://docs.python.org/3/library/functions.html#bool)

Returns True if the data type of `self` is a floating point data type.

is_inference() → [bool](https://docs.python.org/3/library/functions.html#bool)

See [`torch.is_inference()`](torch.is_inference.html#torch.is_inference)

is_ipu

Is `True` if the Tensor is stored on the IPU, `False` otherwise.

is_leaf

All Tensors that have `requires_grad` which is `False` will be leaf Tensors by convention.

For Tensors that have `requires_grad` which is `True`, they will be leaf Tensors if they were
created by the user. This means that they are not the result of an operation and so
`grad_fn` is None.

Only leaf Tensors will have their `grad` populated during a call to `backward()`.
To get `grad` populated for non-leaf Tensors, you can use `retain_grad()`.

Example:

```
>>> a = torch.rand(10, requires_grad=True)
>>> a.is_leaf
True
>>> b = torch.rand(10, requires_grad=True).cuda()
>>> b.is_leaf
False
# b was created by the operation that cast a cpu Tensor into a cuda Tensor
>>> c = torch.rand(10, requires_grad=True) + 2
>>> c.is_leaf
False
# c was created by the addition operation
>>> d = torch.rand(10).cuda()
>>> d.is_leaf
True
# d does not require gradients and so has no operation creating it (that is tracked by the autograd engine)
>>> e = torch.rand(10).cuda().requires_grad_()
>>> e.is_leaf
True
# e requires gradients and has no operations creating it
>>> f = torch.rand(10, requires_grad=True, device="cuda")
>>> f.is_leaf
True
# f requires grad, has no operation creating it
```

is_meta

Is `True` if the Tensor is a meta tensor, `False` otherwise. Meta tensors
are like normal tensors, but they carry no data.

is_mps

Is `True` if the Tensor is stored on the MPS device, `False` otherwise.

is_neg() → [bool](https://docs.python.org/3/library/functions.html#bool)

Returns True if the negative bit of `self` is set to true.

is_pinned()

Returns true if this tensor resides in pinned memory.
By default, the device pinned memory on will be the current [accelerator](../torch.html#accelerators).

is_quantized

Is `True` if the Tensor is quantized, `False` otherwise.

is_set_to(*tensor*) → [bool](https://docs.python.org/3/library/functions.html#bool)

Returns True if both tensors are pointing to the exact same memory (same
storage, offset, size and stride).

is_shared()[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L827)

Checks if tensor is in shared memory.

This is always `True` for CUDA tensors.

is_signed() → [bool](https://docs.python.org/3/library/functions.html#bool)

Returns True if the data type of `self` is a signed data type.

is_sparse

Is `True` if the Tensor uses sparse COO storage layout, `False` otherwise.

is_sparse_csr

Is `True` if the Tensor uses sparse CSR storage layout, `False` otherwise.

is_xla

Is `True` if the Tensor is stored on an XLA device, `False` otherwise.

is_xpu

Is `True` if the Tensor is stored on the XPU, `False` otherwise.

isclose(*other*, *rtol=1e-05*, *atol=1e-08*, *equal_nan=False*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.isclose()`](torch.isclose.html#torch.isclose)

isfinite() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.isfinite()`](torch.isfinite.html#torch.isfinite)

isinf() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.isinf()`](torch.isinf.html#torch.isinf)

isnan() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.isnan()`](torch.isnan.html#torch.isnan)

isneginf() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.isneginf()`](torch.isneginf.html#torch.isneginf)

isposinf() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.isposinf()`](torch.isposinf.html#torch.isposinf)

isreal() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.isreal()`](torch.isreal.html#torch.isreal)

istft(*n_fft*, *hop_length=None*, *win_length=None*, *window=None*, *center=True*, *normalized=False*, *onesided=None*, *length=None*, *return_complex=False*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L997)

See [`torch.istft()`](torch.istft.html#torch.istft)

item() → number

Returns the value of this tensor as a standard Python number. This only works
for tensors with one element. For other cases, see `tolist()`.

This operation is not differentiable.

Example:

```
>>> x = torch.tensor([1.0])
>>> x.item()
1.0
```

itemsize

Alias for `element_size()`

kron(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.kron()`](torch.kron.html#torch.kron)

kthvalue(*k*, *dim=None*, *keepdim=False*)

See [`torch.kthvalue()`](torch.kthvalue.html#torch.kthvalue)

lcm(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.lcm()`](torch.lcm.html#torch.lcm)

lcm_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `lcm()`

ldexp(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.ldexp()`](torch.ldexp.html#torch.ldexp)

ldexp_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `ldexp()`

le(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.le()`](torch.le.html#torch.le).

le_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `le()`.

lerp(*end*, *weight*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.lerp()`](torch.lerp.html#torch.lerp)

lerp_(*end*, *weight*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `lerp()`

less()

lt(other) -> Tensor

See [`torch.less()`](torch.less.html#torch.less).

less_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `less()`.

less_equal(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.less_equal()`](torch.less_equal.html#torch.less_equal).

less_equal_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `less_equal()`.

lgamma() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.lgamma()`](torch.lgamma.html#torch.lgamma)

lgamma_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `lgamma()`

log() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.log()`](torch.log.html#torch.log)

log10() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.log10()`](torch.log10.html#torch.log10)

log10_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `log10()`

log1p() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.log1p()`](torch.log1p.html#torch.log1p)

log1p_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `log1p()`

log2() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.log2()`](torch.log2.html#torch.log2)

log2_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `log2()`

log_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `log()`

log_normal_(*mean=1*, *std=2*, ***, *generator=None*)

Fills `self` tensor with numbers samples from the log-normal distribution
parameterized by the given mean μ\muμ and standard deviation
σ\sigmaσ. Note that `mean` and `std` are the mean and
standard deviation of the underlying normal distribution, and not of the
returned distribution:

f(x)=1xσ2π e−(ln⁡x−μ)22σ2f(x) = \dfrac{1}{x \sigma \sqrt{2\pi}}\ e^{-\frac{(\ln x - \mu)^2}{2\sigma^2}}f(x)=xσ2π​1​ e−2σ2(lnx−μ)2​

logaddexp(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.logaddexp()`](torch.logaddexp.html#torch.logaddexp)

logaddexp2(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.logaddexp2()`](torch.logaddexp2.html#torch.logaddexp2)

logcumsumexp(*dim*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.logcumsumexp()`](torch.logcumsumexp.html#torch.logcumsumexp)

logdet() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.logdet()`](torch.logdet.html#torch.logdet)

logical_and() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.logical_and()`](torch.logical_and.html#torch.logical_and)

logical_and_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `logical_and()`

logical_not() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.logical_not()`](torch.logical_not.html#torch.logical_not)

logical_not_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `logical_not()`

logical_or() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.logical_or()`](torch.logical_or.html#torch.logical_or)

logical_or_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `logical_or()`

logical_xor() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.logical_xor()`](torch.logical_xor.html#torch.logical_xor)

logical_xor_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `logical_xor()`

logit() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.logit()`](torch.logit.html#torch.logit)

logit_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `logit()`

logsumexp(*dim*, *keepdim=False*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.logsumexp()`](torch.logsumexp.html#torch.logsumexp)

long(*memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

`self.long()` is equivalent to `self.to(torch.int64)`. See `to()`.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

lt(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.lt()`](torch.lt.html#torch.lt).

lt_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `lt()`.

lu(*pivot=True*, *get_infos=False*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L932)

See [`torch.lu()`](torch.lu.html#torch.lu)

lu_solve(*LU_data*, *LU_pivots*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.lu_solve()`](torch.lu_solve.html#torch.lu_solve)

mH

Accessing this property is equivalent to calling `adjoint()`.

mT

Returns a view of this tensor with the last two dimensions transposed.

`x.mT` is equivalent to `x.transpose(-2, -1)`.

map_(*tensor*, *callable*)

Applies `callable` for each element in `self` tensor and the given
`tensor` and stores the results in `self` tensor. `self` tensor and
the given `tensor` must be [broadcastable](../notes/broadcasting.html#broadcasting-semantics).

The `callable` should have the signature:

```
def callable(a, b) -> number
```

masked_fill(*mask*, *value*) → [Tensor](../tensors.html#torch.Tensor)

Out-of-place version of [`torch.Tensor.masked_fill_()`](torch.Tensor.masked_fill_.html#torch.Tensor.masked_fill_)

masked_fill_(*mask*, *value*)

Fills elements of `self` tensor with `value` where `mask` is
True. The shape of `mask` must be
[broadcastable](../notes/broadcasting.html#broadcasting-semantics) with the shape of the underlying
tensor.

Parameters:

- **mask** (*BoolTensor*) - the boolean mask
- **value** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the value to fill in with

masked_scatter(*mask*, *tensor*) → [Tensor](../tensors.html#torch.Tensor)

Out-of-place version of [`torch.Tensor.masked_scatter_()`](torch.Tensor.masked_scatter_.html#torch.Tensor.masked_scatter_)

Note

The inputs `self` and `mask`
[broadcast](../notes/broadcasting.html#broadcasting-semantics).

Example

```
>>> self = torch.tensor([0, 0, 0, 0, 0])
>>> mask = torch.tensor(
... [[0, 0, 0, 1, 1], [1, 1, 0, 1, 1]],
... dtype=torch.bool,
... )
>>> source = torch.tensor([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
>>> self.masked_scatter(mask, source)
tensor([[0, 0, 0, 0, 1],
 [2, 3, 0, 4, 5]])
```

masked_scatter_(*mask*, *source*)

Copies elements from `source` into `self` tensor at positions where
the `mask` is True. Elements from `source` are copied into `self`
starting at position 0 of `source` and continuing in order one-by-one for each
occurrence of `mask` being True.
The shape of `mask` must be [broadcastable](../notes/broadcasting.html#broadcasting-semantics)
with the shape of the underlying tensor. The `source` should have at least
as many elements as the number of ones in `mask`.

Parameters:

- **mask** (*BoolTensor*) - the boolean mask
- **source** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor to copy from

Note

The `mask` operates on the `self` tensor, not on the given
`source` tensor.

Example

```
>>> self = torch.tensor([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
>>> mask = torch.tensor(
... [[0, 0, 0, 1, 1], [1, 1, 0, 1, 1]],
... dtype=torch.bool,
... )
>>> source = torch.tensor([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
>>> self.masked_scatter_(mask, source)
tensor([[0, 0, 0, 0, 1],
 [2, 3, 0, 4, 5]])
```

masked_select(*mask*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.masked_select()`](torch.masked_select.html#torch.masked_select)

matmul(*tensor2*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.matmul()`](torch.matmul.html#torch.matmul)

matrix_exp() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.matrix_exp()`](torch.matrix_exp.html#torch.matrix_exp)

matrix_power(*n*) → [Tensor](../tensors.html#torch.Tensor)

Note

`matrix_power()` is deprecated, use [`torch.linalg.matrix_power()`](torch.linalg.matrix_power.html#torch.linalg.matrix_power) instead.

Alias for [`torch.linalg.matrix_power()`](torch.linalg.matrix_power.html#torch.linalg.matrix_power)

max(*dim=None*, *keepdim=False*)

See [`torch.max()`](torch.max.html#torch.max)

maximum(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.maximum()`](torch.maximum.html#torch.maximum)

mean(*dim=None*, *keepdim=False*, ***, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.mean()`](torch.mean.html#torch.mean)

median(*dim=None*, *keepdim=False*)

See [`torch.median()`](torch.median.html#torch.median)

min(*dim=None*, *keepdim=False*)

See [`torch.min()`](torch.min.html#torch.min)

minimum(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.minimum()`](torch.minimum.html#torch.minimum)

mm(*mat2*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.mm()`](torch.mm.html#torch.mm)

mode(*dim=None*, *keepdim=False*)

See [`torch.mode()`](torch.mode.html#torch.mode)

module_load(*other*, *assign=False*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L849)

Defines how to transform `other` when loading it into `self` in `load_state_dict()`.

Used when [`get_swap_module_params_on_conversion()`](../future_mod.html#torch.__future__.get_swap_module_params_on_conversion) is `True`.

It is expected that `self` is a parameter or buffer in an `nn.Module` and `other` is the
value in the state dictionary with the corresponding key, this method defines
how `other` is remapped before being swapped with `self` via
[`swap_tensors()`](torch.utils.swap_tensors.html#torch.utils.swap_tensors) in `load_state_dict()`.

Note

This method should always return a new object that is not `self` or `other`.
For example, the default implementation returns `self.copy_(other).detach()`
if `assign` is `False` or `other.detach()` if `assign` is `True`.

Parameters:

- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - value in state dict with key corresponding to `self`
- **assign** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - the assign argument passed to `nn.Module.load_state_dict()`

moveaxis(*source*, *destination*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.moveaxis()`](torch.moveaxis.html#torch.moveaxis)

movedim(*source*, *destination*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.movedim()`](torch.movedim.html#torch.movedim)

msort() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.msort()`](torch.msort.html#torch.msort)

mtia(*device=None*, *non_blocking=False*, *memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

Returns a copy of this object in MTIA memory.

If this object is already in MTIA memory and on the correct device,
then no copy is performed and the original object is returned.

Parameters:

- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - The destination MTIA device.
Defaults to the current MTIA device.
- **non_blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `True` and the source is in pinned memory,
the copy will be asynchronous with respect to the host.
Otherwise, the argument has no effect. Default: `False`.
- **memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

mul(*value*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.mul()`](torch.mul.html#torch.mul).

mul_(*value*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `mul()`.

multinomial(*num_samples*, *replacement=False*, ***, *generator=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.multinomial()`](torch.multinomial.html#torch.multinomial)

multiply(*value*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.multiply()`](torch.multiply.html#torch.multiply).

multiply_(*value*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `multiply()`.

mv(*vec*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.mv()`](torch.mv.html#torch.mv)

mvlgamma(*p*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.mvlgamma()`](torch.mvlgamma.html#torch.mvlgamma)

mvlgamma_(*p*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `mvlgamma()`

nan_to_num(*nan=0.0*, *posinf=None*, *neginf=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.nan_to_num()`](torch.nan_to_num.html#torch.nan_to_num).

nan_to_num_(*nan=0.0*, *posinf=None*, *neginf=None*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `nan_to_num()`.

nanmean(*dim=None*, *keepdim=False*, ***, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.nanmean()`](torch.nanmean.html#torch.nanmean)

nanmedian(*dim=None*, *keepdim=False*)

See [`torch.nanmedian()`](torch.nanmedian.html#torch.nanmedian)

nanquantile(*q*, *dim=None*, *keepdim=False*, ***, *interpolation='linear'*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.nanquantile()`](torch.nanquantile.html#torch.nanquantile)

nansum(*dim=None*, *keepdim=False*, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.nansum()`](torch.nansum.html#torch.nansum)

narrow(*dimension*, *start*, *length*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.narrow()`](torch.narrow.html#torch.narrow).

narrow_copy(*dimension*, *start*, *length*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.narrow_copy()`](torch.narrow_copy.html#torch.narrow_copy).

nbytes

Returns the number of bytes consumed by the "view" of elements of the Tensor
if the Tensor does not use sparse storage layout.
Defined to be `numel()` * `element_size()`

ndim

Alias for `dim()`

ndimension() → [int](https://docs.python.org/3/library/functions.html#int)

Alias for `dim()`

ne(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.ne()`](torch.ne.html#torch.ne).

ne_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `ne()`.

neg() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.neg()`](torch.neg.html#torch.neg)

neg_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `neg()`

negative() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.negative()`](torch.negative.html#torch.negative)

negative_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `negative()`

nelement() → [int](https://docs.python.org/3/library/functions.html#int)

Alias for `numel()`

new_empty(*size*, ***, *dtype=None*, *device=None*, *requires_grad=False*, *layout=torch.strided*, *pin_memory=False*) → [Tensor](../tensors.html#torch.Tensor)

Returns a Tensor of size `size` filled with uninitialized data.
By default, the returned Tensor has the same [`torch.dtype`](../tensor_attributes.html#torch.dtype) and
[`torch.device`](../tensor_attributes.html#torch.device) as this tensor.

Parameters:

**size** ([*int*](https://docs.python.org/3/library/functions.html#int)*...*) - a list, tuple, or [`torch.Size`](../size.html#torch.Size) of integers defining the
shape of the output tensor.

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired type of returned tensor.
Default: if None, same [`torch.dtype`](../tensor_attributes.html#torch.dtype) as this tensor.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if None, same [`torch.device`](../tensor_attributes.html#torch.device) as this tensor.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned Tensor.
Default: `torch.strided`.
- **pin_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set, returned tensor would be allocated in
the pinned memory. Works only for CPU tensors. Default: `False`.

Example:

```
>>> tensor = torch.ones(())
>>> tensor.new_empty((2, 3))
tensor([[ 5.8182e-18, 4.5765e-41, -1.0545e+30],
 [ 3.0949e-41, 4.4842e-44, 0.0000e+00]])
```

new_empty_strided(*size*, *stride*, *dtype=None*, *device=None*, *requires_grad=False*, *layout=torch.strided*, *pin_memory=False*) → [Tensor](../tensors.html#torch.Tensor)

Returns a Tensor of size `size` and strides `stride` filled with
uninitialized data. By default, the returned Tensor has the same
[`torch.dtype`](../tensor_attributes.html#torch.dtype) and [`torch.device`](../tensor_attributes.html#torch.device) as this tensor.

Parameters:

**size** ([*int*](https://docs.python.org/3/library/functions.html#int)*...*) - a list, tuple, or [`torch.Size`](../size.html#torch.Size) of integers defining the
shape of the output tensor.

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired type of returned tensor.
Default: if None, same [`torch.dtype`](../tensor_attributes.html#torch.dtype) as this tensor.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if None, same [`torch.device`](../tensor_attributes.html#torch.device) as this tensor.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned Tensor.
Default: `torch.strided`.
- **pin_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set, returned tensor would be allocated in
the pinned memory. Works only for CPU tensors. Default: `False`.

Example:

```
>>> tensor = torch.ones(())
>>> tensor.new_empty_strided((2, 3), (3, 1))
tensor([[ 5.8182e-18, 4.5765e-41, -1.0545e+30],
 [ 3.0949e-41, 4.4842e-44, 0.0000e+00]])
```

new_full(*size*, *fill_value*, ***, *dtype=None*, *device=None*, *requires_grad=False*, *layout=torch.strided*, *pin_memory=False*) → [Tensor](../tensors.html#torch.Tensor)

Returns a Tensor of size `size` filled with `fill_value`.
By default, the returned Tensor has the same [`torch.dtype`](../tensor_attributes.html#torch.dtype) and
[`torch.device`](../tensor_attributes.html#torch.device) as this tensor.

Parameters:

**fill_value** (*scalar*) - the number to fill the output tensor with.

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired type of returned tensor.
Default: if None, same [`torch.dtype`](../tensor_attributes.html#torch.dtype) as this tensor.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if None, same [`torch.device`](../tensor_attributes.html#torch.device) as this tensor.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned Tensor.
Default: `torch.strided`.
- **pin_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set, returned tensor would be allocated in
the pinned memory. Works only for CPU tensors. Default: `False`.

Example:

```
>>> tensor = torch.ones((2,), dtype=torch.float64)
>>> tensor.new_full((3, 4), 3.141592)
tensor([[ 3.1416, 3.1416, 3.1416, 3.1416],
 [ 3.1416, 3.1416, 3.1416, 3.1416],
 [ 3.1416, 3.1416, 3.1416, 3.1416]], dtype=torch.float64)
```

new_ones(*size*, ***, *dtype=None*, *device=None*, *requires_grad=False*, *layout=torch.strided*, *pin_memory=False*) → [Tensor](../tensors.html#torch.Tensor)

Returns a Tensor of size `size` filled with `1`.
By default, the returned Tensor has the same [`torch.dtype`](../tensor_attributes.html#torch.dtype) and
[`torch.device`](../tensor_attributes.html#torch.device) as this tensor.

Parameters:

**size** ([*int*](https://docs.python.org/3/library/functions.html#int)*...*) - a list, tuple, or [`torch.Size`](../size.html#torch.Size) of integers defining the
shape of the output tensor.

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired type of returned tensor.
Default: if None, same [`torch.dtype`](../tensor_attributes.html#torch.dtype) as this tensor.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if None, same [`torch.device`](../tensor_attributes.html#torch.device) as this tensor.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned Tensor.
Default: `torch.strided`.
- **pin_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set, returned tensor would be allocated in
the pinned memory. Works only for CPU tensors. Default: `False`.

Example:

```
>>> tensor = torch.tensor((), dtype=torch.int32)
>>> tensor.new_ones((2, 3))
tensor([[ 1, 1, 1],
 [ 1, 1, 1]], dtype=torch.int32)
```

new_tensor(*data*, ***, *dtype=None*, *device=None*, *requires_grad=False*, *layout=torch.strided*, *pin_memory=False*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new Tensor with `data` as the tensor data.
By default, the returned Tensor has the same [`torch.dtype`](../tensor_attributes.html#torch.dtype) and
[`torch.device`](../tensor_attributes.html#torch.device) as this tensor.

Warning

`new_tensor()` always copies `data`. If you have a Tensor
`data` and want to avoid a copy, use [`torch.Tensor.requires_grad_()`](torch.Tensor.requires_grad_.html#torch.Tensor.requires_grad_)
or [`torch.Tensor.detach()`](torch.Tensor.detach.html#torch.Tensor.detach).
If you have a numpy array and want to avoid a copy, use
[`torch.from_numpy()`](torch.from_numpy.html#torch.from_numpy).

Warning

When data is a tensor x, `new_tensor()` reads out 'the data' from whatever it is passed,
and constructs a leaf variable. Therefore `tensor.new_tensor(x)` is equivalent to `x.detach().clone()`
and `tensor.new_tensor(x, requires_grad=True)` is equivalent to `x.detach().clone().requires_grad_(True)`.
The equivalents using `detach()` and `clone()` are recommended.

Parameters:

**data** (*array_like*) - The returned Tensor copies `data`.

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired type of returned tensor.
Default: if None, same [`torch.dtype`](../tensor_attributes.html#torch.dtype) as this tensor.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if None, same [`torch.device`](../tensor_attributes.html#torch.device) as this tensor.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned Tensor.
Default: `torch.strided`.
- **pin_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set, returned tensor would be allocated in
the pinned memory. Works only for CPU tensors. Default: `False`.

Example:

```
>>> tensor = torch.ones((2,), dtype=torch.int8)
>>> data = [[0, 1], [2, 3]]
>>> tensor.new_tensor(data)
tensor([[ 0, 1],
 [ 2, 3]], dtype=torch.int8)
```

new_zeros(*size*, ***, *dtype=None*, *device=None*, *requires_grad=False*, *layout=torch.strided*, *pin_memory=False*) → [Tensor](../tensors.html#torch.Tensor)

Returns a Tensor of size `size` filled with `0`.
By default, the returned Tensor has the same [`torch.dtype`](../tensor_attributes.html#torch.dtype) and
[`torch.device`](../tensor_attributes.html#torch.device) as this tensor.

Parameters:

**size** ([*int*](https://docs.python.org/3/library/functions.html#int)*...*) - a list, tuple, or [`torch.Size`](../size.html#torch.Size) of integers defining the
shape of the output tensor.

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired type of returned tensor.
Default: if None, same [`torch.dtype`](../tensor_attributes.html#torch.dtype) as this tensor.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if None, same [`torch.device`](../tensor_attributes.html#torch.device) as this tensor.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned Tensor.
Default: `torch.strided`.
- **pin_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set, returned tensor would be allocated in
the pinned memory. Works only for CPU tensors. Default: `False`.

Example:

```
>>> tensor = torch.tensor((), dtype=torch.float64)
>>> tensor.new_zeros((2, 3))
tensor([[ 0., 0., 0.],
 [ 0., 0., 0.]], dtype=torch.float64)
```

nextafter(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.nextafter()`](torch.nextafter.html#torch.nextafter)

nextafter_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `nextafter()`

nonzero() → LongTensor

See [`torch.nonzero()`](torch.nonzero.html#torch.nonzero)

nonzero_static(***, *size*, *fill_value=-1*) → LongTensor

See [`torch.nonzero_static()`](torch.nonzero_static.html#torch.nonzero_static)

norm(*p='fro'*, *dim=None*, *keepdim=False*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L888)

See [`torch.linalg.norm()`](torch.linalg.norm.html#torch.linalg.norm)

normal_(*mean=0*, *std=1*, ***, *generator=None*) → [Tensor](../tensors.html#torch.Tensor)

Fills `self` tensor with elements samples from the normal distribution
parameterized by `mean` and `std`.

not_equal(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.not_equal()`](torch.not_equal.html#torch.not_equal).

not_equal_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `not_equal()`.

numel() → [int](https://docs.python.org/3/library/functions.html#int)

See [`torch.numel()`](torch.numel.html#torch.numel)

numpy(***, *force=False*) → [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)

Returns the tensor as a NumPy `ndarray`.

If `force` is `False` (the default), the conversion
is performed only if the tensor is on the CPU, does not require grad,
does not have its conjugate bit set, and is a dtype and layout that
NumPy supports. The returned ndarray and the tensor will share their
storage, so changes to the tensor will be reflected in the ndarray
and vice versa.

If `force` is `True` this is equivalent to
calling `t.detach().cpu().resolve_conj().resolve_neg().numpy()`.
If the tensor isn't on the CPU or the conjugate or negative bit is set,
the tensor won't share its storage with the returned ndarray.
Setting `force` to `True` can be a useful shorthand.

Parameters:

**force** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - if `True`, the ndarray may be a copy of the tensor
instead of always sharing memory, defaults to `False`.

orgqr(*input2*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.orgqr()`](torch.orgqr.html#torch.orgqr)

ormqr(*input2*, *input3*, *left=True*, *transpose=False*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.ormqr()`](torch.ormqr.html#torch.ormqr)

outer(*vec2*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.outer()`](torch.outer.html#torch.outer).

permute(**dims*) → [Tensor](../tensors.html#torch.Tensor)

Returns a view of the tensor with its dimensions permuted.

Parameters:

**dims** ([*torch.Size*](../size.html#torch.Size)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*...**,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*of*[*int*](https://docs.python.org/3/library/functions.html#int)) - the desired ordering of dimensions.

Example

```
>>> x = torch.randn(2, 3, 5)
>>> x.size()
torch.Size([2, 3, 5])
>>> x.permute(2, 0, 1).size()
torch.Size([5, 2, 3])
```

pin_memory() → [Tensor](../tensors.html#torch.Tensor)

Copies the tensor to pinned memory, if it's not already pinned.
By default, the device pinned memory on will be the current [accelerator](../torch.html#accelerators).

pinverse() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.pinverse()`](torch.pinverse.html#torch.pinverse)

polygamma(*n*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.polygamma()`](torch.polygamma.html#torch.polygamma)

polygamma_(*n*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `polygamma()`

positive() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.positive()`](torch.positive.html#torch.positive)

pow(*exponent*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.pow()`](torch.pow.html#torch.pow)

pow_(*exponent*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `pow()`

prod(*dim=None*, *keepdim=False*, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.prod()`](torch.prod.html#torch.prod)

*classmethod*prune_dense_static_sort(*original_tensor*, *algorithm=''*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/sparse/semi_structured.py#L434)

This function takes in a unpruned dense tensor and runs a (branchless) static sort across a 4x4 tile.

It greedily picks the largest values in the tile, upholding the 2:4 sparsity constraint across both rows and columns.
The algorithm used to prune the matrix is implemented in _sparse_semi_structured_tile.

Then it creates the packed and meta tensors for the compressed sparse representation of the pruned dense tensor.
It also calculates the packed_t and meta_t tensors for the compressed sparse representation of the transposed
pruned dense tensor.
Since we cannot transpose the compressed representations, we store both for the fw/bw pass respectively.

Finally, this function also computes a compressed swizzled bitmask that encodes the sparsity pattern.
This can be used in the backward pass to mask the gradients.

```
[9 1 7 4] [9 0 7 0]
[1 2 3 0] [0 2 0 0]
[8 3 5 4] -> prune 4x4 tile -> [8 0 0 4] -> pack to CUTLASS semi-structured -> packed
[1 2 6 2] [0 0 6 2] -> metadata

 -> pack to transposed CUTLASS -> packed_t
 semi-structured representation -> metadata_t

 -> compute swizzled bitmask -> compressed_swizzled_bitmask
```

The equivalent PyTorch code to create the same five outputs from the dense tensor can be found below:

```
from torch.sparse import SparseSemiStructuredTensorCUTLASS
from torch.sparse._semi_structured_conversions import (
 _sparse_semi_structured_tile,
 _compute_compressed_swizzled_bitmask,
)

pruned = _sparse_semi_structured_tile(dense)
packed_cutlass, meta_cutlass = sparse_semi_structured_from_dense_cutlass(
 pruned
)
packed_t_cutlass, meta_t_cutlass = (
 sparse_semi_structured_from_dense_cutlass(pruned.t().contiguous())
)
bitmask = _compute_compressed_swizzled_bitmask(pruned)

SparseSemiStructuredTensorCUTLASS(
 dense.shape,
 packed_cutlass,
 meta_cutlass,
 packed_t_cutlass,
 meta_t_cutlass,
 bitmask,
)
```

Return type:

*SparseSemiStructuredTensor*

put(*input*, *index*, *source*, *accumulate=False*) → [Tensor](../tensors.html#torch.Tensor)

Out-of-place version of [`torch.Tensor.put_()`](torch.Tensor.put_.html#torch.Tensor.put_).
input corresponds to self in [`torch.Tensor.put_()`](torch.Tensor.put_.html#torch.Tensor.put_).

put_(*index*, *source*, *accumulate=False*) → [Tensor](../tensors.html#torch.Tensor)

Copies the elements from `source` into the positions specified by
`index`. For the purpose of indexing, the `self` tensor is treated as if
it were a 1-D tensor.

`index` and `source` need to have the same number of elements, but not necessarily
the same shape.

If `accumulate` is `True`, the elements in `source` are added to
`self`. If accumulate is `False`, the behavior is undefined if `index`
contain duplicate elements.

Parameters:

- **index** (*LongTensor*) - the indices into self
- **source** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor containing values to copy from
- **accumulate** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether to accumulate into self. Default: `False`

Example:

```
>>> src = torch.tensor([[4, 3, 5],
... [6, 7, 8]])
>>> src.put_(torch.tensor([1, 3]), torch.tensor([9, 10]))
tensor([[ 4, 9, 5],
 [ 10, 7, 8]])
```

q_per_channel_axis() → [int](https://docs.python.org/3/library/functions.html#int)

Given a Tensor quantized by linear (affine) per-channel quantization,
returns the index of dimension on which per-channel quantization is applied.

q_per_channel_scales() → [Tensor](../tensors.html#torch.Tensor)

Given a Tensor quantized by linear (affine) per-channel quantization,
returns a Tensor of scales of the underlying quantizer. It has the number of
elements that matches the corresponding dimensions (from q_per_channel_axis) of
the tensor.

q_per_channel_zero_points() → [Tensor](../tensors.html#torch.Tensor)

Given a Tensor quantized by linear (affine) per-channel quantization,
returns a tensor of zero_points of the underlying quantizer. It has the number of
elements that matches the corresponding dimensions (from q_per_channel_axis) of
the tensor.

q_scale() → [float](https://docs.python.org/3/library/functions.html#float)

Given a Tensor quantized by linear(affine) quantization,
returns the scale of the underlying quantizer().

q_zero_point() → [int](https://docs.python.org/3/library/functions.html#int)

Given a Tensor quantized by linear(affine) quantization,
returns the zero_point of the underlying quantizer().

qscheme() → torch.qscheme

Returns the quantization scheme of a given QTensor.

quantile(*q*, *dim=None*, *keepdim=False*, ***, *interpolation='linear'*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.quantile()`](torch.quantile.html#torch.quantile)

rad2deg() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.rad2deg()`](torch.rad2deg.html#torch.rad2deg)

rad2deg_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `rad2deg()`

random_(*from=0*, *to=None*, ***, *generator=None*) → [Tensor](../tensors.html#torch.Tensor)

Fills `self` tensor with numbers sampled from the discrete uniform
distribution over `[from, to - 1]`. If not specified, the values are usually
only bounded by `self` tensor's data type. However, for floating point
types, if unspecified, range will be `[0, 2^mantissa]` to ensure that every
value is representable. For example, torch.tensor(1, dtype=torch.double).random_()
will be uniform in `[0, 2^53]`.

ravel() → [Tensor](../tensors.html#torch.Tensor)

see [`torch.ravel()`](torch.ravel.html#torch.ravel)

real

Returns a new tensor containing real values of the `self` tensor for a complex-valued input tensor.
The returned tensor and `self` share the same underlying storage.

Returns `self` if `self` is a real-valued tensor.

Example:

```
>>> x=torch.randn(4, dtype=torch.cfloat)
>>> x
tensor([(0.3100+0.3553j), (-0.5445-0.7896j), (-1.6492-0.0633j), (-0.0638-0.8119j)])
>>> x.real
tensor([ 0.3100, -0.5445, -1.6492, -0.0638])
```

reciprocal() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.reciprocal()`](torch.reciprocal.html#torch.reciprocal)

reciprocal_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `reciprocal()`

record_stream(*stream*)

Marks the tensor as having been used by this stream. When the tensor
is deallocated, ensure the tensor memory is not reused for another tensor
until all work queued on `stream` at the time of deallocation is
complete.

Note

The caching allocator is aware of only the stream where a tensor was
allocated. Due to the awareness, it already correctly manages the life
cycle of tensors on only one stream. But if a tensor is used on a stream
different from the stream of origin, the allocator might reuse the memory
unexpectedly. Calling this method lets the allocator know which streams
have used the tensor.

Warning

This method is most suitable for use cases where you are providing a
function that created a tensor on a side stream, and want users to be able
to make use of the tensor without having to think carefully about stream
safety when making use of them. These safety guarantees come at some
performance and predictability cost (analogous to the tradeoff between GC
and manual memory management), so if you are in a situation where
you manage the full lifetime of your tensors, you may consider instead
manually managing CUDA events so that calling this method is not necessary.
In particular, when you call this method, on later allocations the
allocator will poll the recorded stream to see if all operations have
completed yet; you can potentially race with side stream computation and
non-deterministically reuse or fail to reuse memory for an allocation.

You can safely use tensors allocated on side streams without
`record_stream()`; you must manually ensure that
any non-creation stream uses of a tensor are synced back to the creation
stream before you deallocate the tensor. As the CUDA caching allocator
guarantees that the memory will only be reused with the same creation stream,
this is sufficient to ensure that writes to future reallocations of the
memory will be delayed until non-creation stream uses are done.
(Counterintuitively, you may observe that on the CPU side we have already
reallocated the tensor, even though CUDA kernels on the old tensor are
still in progress. This is fine, because CUDA operations on the new
tensor will appropriately wait for the old operations to complete, as they
are all on the same stream.)

Concretely, this looks like this:

```
with torch.cuda.stream(s0):
 x = torch.zeros(N)

s1.wait_stream(s0)
with torch.cuda.stream(s1):
 y = some_comm_op(x)

... some compute on s0 ...

# synchronize creation stream s0 to side stream s1
# before deallocating x
s0.wait_stream(s1)
del x
```

Note that some discretion is required when deciding when to perform
`s0.wait_stream(s1)`. In particular, if we were to wait immediately
after `some_comm_op`, there wouldn't be any point in having the side
stream; it would be equivalent to have run `some_comm_op` on `s0`.
Instead, the synchronization must be placed at some appropriate, later
point in time where you expect the side stream `s1` to have finished
work. This location is typically identified via profiling, e.g., using
Chrome traces produced
[`torch.autograd.profiler.profile.export_chrome_trace()`](torch.autograd.profiler.profile.export_chrome_trace.html#torch.autograd.profiler.profile.export_chrome_trace). If you
place the wait too early, work on s0 will block until `s1` has finished,
preventing further overlapping of communication and computation. If you
place the wait too late, you will use more memory than is strictly
necessary (as you are keeping `x` live for longer.) For a concrete
example of how this guidance can be applied in practice, see this post:
[FSDP and CUDACachingAllocator](https://dev-discuss.pytorch.org/t/fsdp-cudacachingallocator-an-outsider-newb-perspective/1486).

register_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L655)

Registers a backward hook.

The hook will be called every time a gradient with respect to the
Tensor is computed. The hook should have the following signature:

```
hook(grad) -> Tensor or None
```

The hook should not modify its argument, but it can optionally return
a new gradient which will be used in place of `grad`.

This function returns a handle with a method `handle.remove()`
that removes the hook from the module.

Note

See [Backward Hooks execution](../notes/autograd.html#backward-hooks-execution) for more information on how when this hook
is executed, and how its execution is ordered relative to other hooks.

Example:

```
>>> v = torch.tensor([0., 0., 0.], requires_grad=True)
>>> h = v.register_hook(lambda grad: grad * 2) # double the gradient
>>> v.backward(torch.tensor([1., 2., 3.]))
>>> v.grad

 2
 4
 6
[torch.FloatTensor of size (3,)]

>>> h.remove() # removes the hook
```

register_post_accumulate_grad_hook(*hook*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L705)

Registers a backward hook that runs after grad accumulation.

The hook will be called after all gradients for a tensor have been accumulated,
meaning that the .grad field has been updated on that tensor. The post
accumulate grad hook is ONLY applicable for leaf tensors (tensors without a
.grad_fn field). Registering this hook on a non-leaf tensor will error!

The hook should have the following signature:

```
hook(param: Tensor) -> None
```

Note that, unlike other autograd hooks, this hook operates on the tensor
that requires grad and not the grad itself. The hook can in-place modify
and access its Tensor argument, including its .grad field.

This function returns a handle with a method `handle.remove()`
that removes the hook from the module.

Note

See [Backward Hooks execution](../notes/autograd.html#backward-hooks-execution) for more information on how when this hook
is executed, and how its execution is ordered relative to other hooks. Since
this hook runs during the backward pass, it will run in no_grad mode (unless
create_graph is True). You can use torch.enable_grad() to re-enable autograd
within the hook if you need it.

Example:

```
>>> v = torch.tensor([0., 0., 0.], requires_grad=True)
>>> lr = 0.01
>>> # simulate a simple SGD update
>>> h = v.register_post_accumulate_grad_hook(lambda p: p.add_(p.grad, alpha=-lr))
>>> v.backward(torch.tensor([1., 2., 3.]))
>>> v
tensor([-0.0100, -0.0200, -0.0300], requires_grad=True)

>>> h.remove() # removes the hook
```

remainder(*divisor*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.remainder()`](torch.remainder.html#torch.remainder)

remainder_(*divisor*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `remainder()`

renorm(*p*, *dim*, *maxnorm*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.renorm()`](torch.renorm.html#torch.renorm)

renorm_(*p*, *dim*, *maxnorm*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `renorm()`

repeat(**repeats*) → [Tensor](../tensors.html#torch.Tensor)

Repeats this tensor along the specified dimensions.

Unlike `expand()`, this function copies the tensor's data.

Warning

`repeat()` behaves differently from
[numpy.repeat](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html),
but is more similar to
[numpy.tile](https://numpy.org/doc/stable/reference/generated/numpy.tile.html).
For the operator similar to numpy.repeat, see [`torch.repeat_interleave()`](torch.repeat_interleave.html#torch.repeat_interleave).

Parameters:

**repeat** ([*torch.Size*](../size.html#torch.Size)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*...**,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*of*[*int*](https://docs.python.org/3/library/functions.html#int)) - The number of times to repeat this tensor along each dimension

Example:

```
>>> x = torch.tensor([1, 2, 3])
>>> x.repeat(4, 2)
tensor([[ 1, 2, 3, 1, 2, 3],
 [ 1, 2, 3, 1, 2, 3],
 [ 1, 2, 3, 1, 2, 3],
 [ 1, 2, 3, 1, 2, 3]])
>>> x.repeat(4, 2, 1).size()
torch.Size([4, 2, 3])
```

repeat_interleave(*repeats*, *dim=None*, ***, *output_size=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.repeat_interleave()`](torch.repeat_interleave.html#torch.repeat_interleave).

requires_grad

Is `True` if gradients need to be computed for this Tensor, `False` otherwise.

Note

The fact that gradients need to be computed for a Tensor do not mean that the `grad`
attribute will be populated, see `is_leaf` for more details.

requires_grad_(*requires_grad=True*) → [Tensor](../tensors.html#torch.Tensor)

Change if autograd should record operations on this tensor: sets this tensor's
`requires_grad` attribute in-place. Returns this tensor.

`requires_grad_()`'s main use case is to tell autograd to begin recording
operations on a Tensor `tensor`. If `tensor` has `requires_grad=False`
(because it was obtained through a DataLoader, or required preprocessing or
initialization), `tensor.requires_grad_()` makes it so that autograd will
begin to record operations on `tensor`.

Parameters:

**requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If autograd should record operations on this tensor.
Default: `True`.

Example:

```
>>> # Let's say we want to preprocess some saved weights and use
>>> # the result as new weights.
>>> saved_weights = [0.1, 0.2, 0.3, 0.25]
>>> loaded_weights = torch.tensor(saved_weights)
>>> weights = preprocess(loaded_weights) # some function
>>> weights
tensor([-0.5503, 0.4926, -2.1158, -0.8303])

>>> # Now, start to record operations done to weights
>>> weights.requires_grad_()
>>> out = weights.pow(2).sum()
>>> out.backward()
>>> weights.grad
tensor([-1.1007, 0.9853, -4.2316, -1.6606])
```

reshape(**shape*) → [Tensor](../tensors.html#torch.Tensor)

Returns a tensor with the same data and number of elements as `self`
but with the specified shape. This method returns a view if `shape` is
compatible with the current shape. See [`torch.Tensor.view()`](torch.Tensor.view.html#torch.Tensor.view) on when it is
possible to return a view.

See [`torch.reshape()`](torch.reshape.html#torch.reshape)

Parameters:

**shape** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**ints**or*[*int*](https://docs.python.org/3/library/functions.html#int)*...*) - the desired shape

reshape_as(*other*) → [Tensor](../tensors.html#torch.Tensor)

Returns this tensor as the same shape as `other`.
`self.reshape_as(other)` is equivalent to `self.reshape(other.sizes())`.
This method returns a view if `other.sizes()` is compatible with the current
shape. See [`torch.Tensor.view()`](torch.Tensor.view.html#torch.Tensor.view) on when it is possible to return a view.

Please see `reshape()` for more information about `reshape`.

Parameters:

**other** ([`torch.Tensor`](../tensors.html#torch.Tensor)) - The result tensor has the same shape
as `other`.

resize_(**sizes*, *memory_format=torch.contiguous_format*) → [Tensor](../tensors.html#torch.Tensor)

Resizes `self` tensor to the specified size. If the number of elements is
larger than the current storage size, then the underlying storage is resized
to fit the new number of elements. If the number of elements is smaller, the
underlying storage is not changed. Existing elements are preserved but any new
memory is uninitialized.

Warning

This is a low-level method. The storage is reinterpreted as C-contiguous,
ignoring the current strides (unless the target size equals the current
size, in which case the tensor is left unchanged). For most purposes, you
will instead want to use `view()`, which checks for
contiguity, or `reshape()`, which copies data if needed. To
change the size in-place with custom strides, see `set_()`.

Note

If [`torch.use_deterministic_algorithms()`](torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms) and
[`torch.utils.deterministic.fill_uninitialized_memory`](../deterministic.html#torch.utils.deterministic.fill_uninitialized_memory) are both set to
`True`, new elements are initialized to prevent nondeterministic behavior
from using the result as an input to an operation. Floating point and
complex values are set to NaN, and integer values are set to the maximum
value.

Parameters:

- **sizes** ([*torch.Size*](../size.html#torch.Size)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*...*) - the desired size
- **memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
Tensor. Default: `torch.contiguous_format`. Note that memory format of
`self` is going to be unaffected if `self.size()` matches `sizes`.

Example:

```
>>> x = torch.tensor([[1, 2], [3, 4], [5, 6]])
>>> x.resize_(2, 2)
tensor([[ 1, 2],
 [ 3, 4]])
```

resize_as_(*tensor*, *memory_format=torch.contiguous_format*) → [Tensor](../tensors.html#torch.Tensor)

Resizes the `self` tensor to be the same size as the specified
`tensor`. This is equivalent to `self.resize_(tensor.size())`.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
Tensor. Default: `torch.contiguous_format`. Note that memory format of
`self` is going to be unaffected if `self.size()` matches `tensor.size()`.

resolve_conj() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.resolve_conj()`](torch.resolve_conj.html#torch.resolve_conj)

resolve_neg() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.resolve_neg()`](torch.resolve_neg.html#torch.resolve_neg)

retain_grad() → [None](https://docs.python.org/3/library/constants.html#None)

Enables this Tensor to have their `grad` populated during
`backward()`. This is a no-op for leaf tensors.

retains_grad

Is `True` if this Tensor is non-leaf and its `grad` is enabled to be
populated during `backward()`, `False` otherwise.

roll(*shifts*, *dims*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.roll()`](torch.roll.html#torch.roll)

rot90(*k*, *dims*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.rot90()`](torch.rot90.html#torch.rot90)

round(*decimals=0*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.round()`](torch.round.html#torch.round)

round_(*decimals=0*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `round()`

rsqrt() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.rsqrt()`](torch.rsqrt.html#torch.rsqrt)

rsqrt_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `rsqrt()`

scatter(*dim*, *index*, *src*) → [Tensor](../tensors.html#torch.Tensor)

Out-of-place version of [`torch.Tensor.scatter_()`](torch.Tensor.scatter_.html#torch.Tensor.scatter_)

scatter_(*dim*, *index*, *src*, ***, *reduce=None*) → [Tensor](../tensors.html#torch.Tensor)

Writes all values from the tensor `src` into `self` at the indices
specified in the `index` tensor. For each value in `src`, its output
index is specified by its index in `src` for `dimension != dim` and by
the corresponding value in `index` for `dimension = dim`.

For a 3-D tensor, `self` is updated as:

```
self[index[i][j][k]][j][k] = src[i][j][k] # if dim == 0
self[i][index[i][j][k]][k] = src[i][j][k] # if dim == 1
self[i][j][index[i][j][k]] = src[i][j][k] # if dim == 2
```

This is the reverse operation of the manner described in `gather()`.

It is also required that
`index.size(d) <= src.size(d)` for all dimensions `d`, and that
`index.size(d) <= self.size(d)` for all dimensions `d != dim`.
Note that `input` and `index` do not broadcast against each other for NPUs,
so when running on NPUs, `input` and `index` must have the same number of dimensions.
Standard broadcasting occurs in all other cases.

Moreover, as for `gather()`, the values of `index` must be
between `0` and `self.size(dim) - 1` inclusive.

Warning

When indices are not unique, the behavior is non-deterministic (one of the
values from `src` will be picked arbitrarily) and the gradient will be
incorrect (it will be propagated to all locations in the source that
correspond to the same index)!

Note

The backward pass is implemented only for `src.shape == index.shape`.

Additionally accepts an optional `reduce` argument that allows
specification of an optional reduction operation, which is applied to all
values in the tensor `src` into `self` at the indices
specified in the `index`. For each value in `src`, the reduction
operation is applied to an index in `self` which is specified by
its index in `src` for `dimension != dim` and by the corresponding
value in `index` for `dimension = dim`.

Given a 3-D tensor and reduction using the multiplication operation, `self`
is updated as:

```
self[index[i][j][k]][j][k] *= src[i][j][k] # if dim == 0
self[i][index[i][j][k]][k] *= src[i][j][k] # if dim == 1
self[i][j][index[i][j][k]] *= src[i][j][k] # if dim == 2
```

Reducing with the addition operation is the same as using
[`scatter_add_()`](torch.Tensor.scatter_add_.html#torch.Tensor.scatter_add_).

Warning

The reduce argument with Tensor `src` is deprecated and will be removed in
a future PyTorch release. Please use [`scatter_reduce_()`](torch.Tensor.scatter_reduce_.html#torch.Tensor.scatter_reduce_)
instead for more reduction options.

Parameters:

- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the axis along which to index
- **index** (*LongTensor*) - the indices of elements to scatter, can be either empty
or of the same dimensionality as `src`. When empty, the operation
returns `self` unchanged.
- **src** ([*Tensor*](../tensors.html#torch.Tensor)) - the source element(s) to scatter.

Keyword Arguments:

**reduce** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - reduction operation to apply, can be either
`'add'` or `'multiply'`.

Example:

```
>>> src = torch.arange(1, 11).reshape((2, 5))
>>> src
tensor([[ 1, 2, 3, 4, 5],
 [ 6, 7, 8, 9, 10]])
>>> index = torch.tensor([[0, 1, 2, 0]])
>>> torch.zeros(3, 5, dtype=src.dtype).scatter_(0, index, src)
tensor([[1, 0, 0, 4, 0],
 [0, 2, 0, 0, 0],
 [0, 0, 3, 0, 0]])
>>> index = torch.tensor([[0, 1, 2], [0, 1, 4]])
>>> torch.zeros(3, 5, dtype=src.dtype).scatter_(1, index, src)
tensor([[1, 2, 3, 0, 0],
 [6, 7, 0, 0, 8],
 [0, 0, 0, 0, 0]])

>>> torch.full((2, 4), 2.).scatter_(1, torch.tensor([[2], [3]]),
... 1.23, reduce='multiply')
tensor([[2.0000, 2.0000, 2.4600, 2.0000],
 [2.0000, 2.0000, 2.0000, 2.4600]])
>>> torch.full((2, 4), 2.).scatter_(1, torch.tensor([[2], [3]]),
... 1.23, reduce='add')
tensor([[2.0000, 2.0000, 3.2300, 2.0000],
 [2.0000, 2.0000, 2.0000, 3.2300]])
```

scatter_(*dim*, *index*, *value*, ***, *reduce=None*) → Tensor:

Writes the value from `value` into `self` at the indices
specified in the `index` tensor. This operation is equivalent to the previous version,
with the `src` tensor filled entirely with `value`.

Parameters:

- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the axis along which to index
- **index** (*LongTensor*) - the indices of elements to scatter, can be either empty
or of the same dimensionality as `src`. When empty, the operation
returns `self` unchanged.
- **value** (*Scalar*) - the value to scatter.

Keyword Arguments:

**reduce** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - reduction operation to apply, can be either
`'add'` or `'multiply'`.

Example:

```
>>> index = torch.tensor([[0, 1]])
>>> value = 2
>>> torch.zeros(3, 5).scatter_(0, index, value)
tensor([[2., 0., 0., 0., 0.],
 [0., 2., 0., 0., 0.],
 [0., 0., 0., 0., 0.]])
```

scatter_add(*dim*, *index*, *src*) → [Tensor](../tensors.html#torch.Tensor)

Out-of-place version of [`torch.Tensor.scatter_add_()`](torch.Tensor.scatter_add_.html#torch.Tensor.scatter_add_)

scatter_add_(*dim*, *index*, *src*) → [Tensor](../tensors.html#torch.Tensor)

Adds all values from the tensor `src` into `self` at the indices
specified in the `index` tensor in a similar fashion as
[`scatter_()`](torch.Tensor.scatter_.html#torch.Tensor.scatter_). For each value in `src`, it is added to
an index in `self` which is specified by its index in `src`
for `dimension != dim` and by the corresponding value in `index` for
`dimension = dim`.

For a 3-D tensor, `self` is updated as:

```
self[index[i][j][k]][j][k] += src[i][j][k] # if dim == 0
self[i][index[i][j][k]][k] += src[i][j][k] # if dim == 1
self[i][j][index[i][j][k]] += src[i][j][k] # if dim == 2
```

`self`, `index` and `src` should have same number of
dimensions. It is also required that `index.size(d) <= src.size(d)` for all
dimensions `d`, and that `index.size(d) <= self.size(d)` for all dimensions
`d != dim`. Note that `index` and `src` do not broadcast.
When `index` is empty, we always return the original tensor
without further error checking.

Note

This operation may behave nondeterministically when given tensors on a CUDA device. See [Reproducibility](../notes/randomness.html) for more information.

Note

The backward pass is implemented only for `src.shape == index.shape`.

Parameters:

- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the axis along which to index
- **index** (*LongTensor*) - the indices of elements to scatter and add, can be
either empty or of the same dimensionality as `src`. When empty, the
operation returns `self` unchanged.
- **src** ([*Tensor*](../tensors.html#torch.Tensor)) - the source elements to scatter and add

Example:

```
>>> src = torch.ones((2, 5))
>>> index = torch.tensor([[0, 1, 2, 0, 0]])
>>> torch.zeros(3, 5, dtype=src.dtype).scatter_add_(0, index, src)
tensor([[1., 0., 0., 1., 1.],
 [0., 1., 0., 0., 0.],
 [0., 0., 1., 0., 0.]])
>>> index = torch.tensor([[0, 1, 2, 0, 0], [0, 1, 2, 2, 2]])
>>> torch.zeros(3, 5, dtype=src.dtype).scatter_add_(0, index, src)
tensor([[2., 0., 0., 1., 1.],
 [0., 2., 0., 0., 0.],
 [0., 0., 2., 1., 1.]])
```

scatter_reduce(*dim*, *index*, *src*, *reduce*, ***, *include_self=True*) → [Tensor](../tensors.html#torch.Tensor)

Out-of-place version of [`torch.Tensor.scatter_reduce_()`](torch.Tensor.scatter_reduce_.html#torch.Tensor.scatter_reduce_)

scatter_reduce_(*dim*, *index*, *src*, *reduce*, ***, *include_self=True*) → [Tensor](../tensors.html#torch.Tensor)

Reduces all values from the `src` tensor to the indices specified in
the `index` tensor in the `self` tensor using the applied reduction
defined via the `reduce` argument (`"sum"`, `"prod"`, `"mean"`,
`"amax"`, `"amin"`). For each value in `src`, it is reduced to an
index in `self` which is specified by its index in `src` for
`dimension != dim` and by the corresponding value in `index` for
`dimension = dim`. If `include_self="True"`, the values in the `self`
tensor are included in the reduction.

`self`, `index` and `src` should all have
the same number of dimensions. It is also required that
`index.size(d) <= src.size(d)` for all dimensions `d`, and that
`index.size(d) <= self.size(d)` for all dimensions `d != dim`.
Note that `index` and `src` do not broadcast.

For a 3-D tensor with `reduce="sum"` and `include_self=True` the
output is given as:

```
self[index[i][j][k]][j][k] += src[i][j][k] # if dim == 0
self[i][index[i][j][k]][k] += src[i][j][k] # if dim == 1
self[i][j][index[i][j][k]] += src[i][j][k] # if dim == 2
```

Note

This operation may behave nondeterministically when given tensors on a CUDA device. See [Reproducibility](../notes/randomness.html) for more information.

Note

The backward pass is implemented only for `src.shape == index.shape`.

Warning

This function is in beta and may change in the near future.

Parameters:

- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the axis along which to index
- **index** (*LongTensor*) - the indices of elements to scatter and reduce.
- **src** ([*Tensor*](../tensors.html#torch.Tensor)) - the source elements to scatter and reduce
- **reduce** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - the reduction operation to apply for non-unique indices
(`"sum"`, `"prod"`, `"mean"`, `"amax"`, `"amin"`)
- **include_self** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - whether elements from the `self` tensor are
included in the reduction

Example:

```
>>> src = torch.tensor([1., 2., 3., 4., 5., 6.])
>>> index = torch.tensor([0, 1, 0, 1, 2, 1])
>>> input = torch.tensor([1., 2., 3., 4.])
>>> input.scatter_reduce(0, index, src, reduce="sum")
tensor([5., 14., 8., 4.])
>>> input.scatter_reduce(0, index, src, reduce="sum", include_self=False)
tensor([4., 12., 5., 4.])
>>> input2 = torch.tensor([5., 4., 3., 2.])
>>> input2.scatter_reduce(0, index, src, reduce="amax")
tensor([5., 6., 5., 2.])
>>> input2.scatter_reduce(0, index, src, reduce="amax", include_self=False)
tensor([3., 6., 5., 2.])
```

select(*dim*, *index*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.select()`](torch.select.html#torch.select)

select_scatter(*src*, *dim*, *index*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.select_scatter()`](torch.select_scatter.html#torch.select_scatter)

set_(*source=None*, *storage_offset=0*, *size=None*, *stride=None*) → [Tensor](../tensors.html#torch.Tensor)

Sets the underlying storage, size, and strides. If `source` is a tensor,
`self` tensor will share the same storage and have the same size and
strides as `source`. Changes to elements in one tensor will be reflected
in the other.

If `source` is a `Storage`, the method sets the underlying
storage, offset, size, and stride.

Parameters:

- **source** ([*Tensor*](../tensors.html#torch.Tensor)*or**Storage*) - the tensor or storage to use
- **storage_offset** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the offset in the storage
- **size** ([*torch.Size*](../size.html#torch.Size)*,**optional*) - the desired size. Defaults to the size of the source.
- **stride** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - the desired stride. Defaults to C-contiguous strides.

sgn() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.sgn()`](torch.sgn.html#torch.sgn)

sgn_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `sgn()`

shape

Returns the size of the `self` tensor. Alias for `size`.

See also `Tensor.size()`.

Example:

```
>>> t = torch.empty(3, 4, 5)
>>> t.size()
torch.Size([3, 4, 5])
>>> t.shape
torch.Size([3, 4, 5])
```

share_memory_()[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L836)

Moves the underlying storage to shared memory.

This is a no-op if the underlying storage is already in shared memory
and for CUDA tensors. Tensors in shared memory cannot be resized.

See [`torch.UntypedStorage.share_memory_()`](../storage.html#torch.UntypedStorage.share_memory_) for more details.

short(*memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

`self.short()` is equivalent to `self.to(torch.int16)`. See `to()`.

Parameters:

**memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

sigmoid() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.sigmoid()`](torch.sigmoid.html#torch.sigmoid)

sigmoid_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `sigmoid()`

sign() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.sign()`](torch.sign.html#torch.sign)

sign_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `sign()`

signbit() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.signbit()`](torch.signbit.html#torch.signbit)

sin() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.sin()`](torch.sin.html#torch.sin)

sin_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `sin()`

sinc() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.sinc()`](torch.sinc.html#torch.sinc)

sinc_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `sinc()`

sinh() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.sinh()`](torch.sinh.html#torch.sinh)

sinh_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `sinh()`

size(*dim=None*) → torch.Size or int

Returns the size of the `self` tensor. If `dim` is not specified,
the returned value is a [`torch.Size`](../size.html#torch.Size), a subclass of [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple).
If `dim` is specified, returns an int holding the size of that dimension.

Parameters:

**dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The dimension for which to retrieve the size.

Example:

```
>>> t = torch.empty(3, 4, 5)
>>> t.size()
torch.Size([3, 4, 5])
>>> t.size(dim=1)
4
```

slice_scatter(*src*, *dim=0*, *start=None*, *end=None*, *step=1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.slice_scatter()`](torch.slice_scatter.html#torch.slice_scatter)

slogdet()

See [`torch.slogdet()`](torch.slogdet.html#torch.slogdet)

smm(*mat*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.smm()`](torch.smm.html#torch.smm)

softmax(*dim*) → [Tensor](../tensors.html#torch.Tensor)

Alias for [`torch.nn.functional.softmax()`](torch.nn.functional.softmax.html#torch.nn.functional.softmax).

sort(*dim=-1*, *descending=False*)

See [`torch.sort()`](torch.sort.html#torch.sort)

sparse_dim() → [int](https://docs.python.org/3/library/functions.html#int)

Return the number of sparse dimensions in a [sparse tensor](../sparse.html#sparse-docs) `self`.

Note

Returns `0` if `self` is not a sparse tensor.

See also `Tensor.dense_dim()` and [hybrid tensors](../sparse.html#sparse-hybrid-coo-docs).

sparse_mask(*mask*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new [sparse tensor](../sparse.html#sparse-docs) with values from a
strided tensor `self` filtered by the indices of the sparse
tensor `mask`. The values of `mask` sparse tensor are
ignored. `self` and `mask` tensors must have the same
shape.

Note

The returned sparse tensor might contain duplicate values if `mask`
is not coalesced. It is therefore advisable to pass `mask.coalesce()`
if such behavior is not desired.

Note

The returned sparse tensor has the same indices as the sparse tensor
`mask`, even when the corresponding values in `self` are
zeros.

Parameters:

**mask** ([*Tensor*](../tensors.html#torch.Tensor)) - a sparse tensor whose indices are used as a filter

Example:

```
>>> nse = 5
>>> dims = (5, 5, 2, 2)
>>> I = torch.cat([torch.randint(0, dims[0], size=(nse,)),
... torch.randint(0, dims[1], size=(nse,))], 0).reshape(2, nse)
>>> V = torch.randn(nse, dims[2], dims[3])
>>> S = torch.sparse_coo_tensor(I, V, dims).coalesce()
>>> D = torch.randn(dims)
>>> D.sparse_mask(S)
tensor(indices=tensor([[0, 0, 0, 2],
 [0, 1, 4, 3]]),
 values=tensor([[[ 1.6550, 0.2397],
 [-0.1611, -0.0779]],

 [[ 0.2326, -1.0558],
 [ 1.4711, 1.9678]],

 [[-0.5138, -0.0411],
 [ 1.9417, 0.5158]],

 [[ 0.0793, 0.0036],
 [-0.2569, -0.1055]]]),
 size=(5, 5, 2, 2), nnz=4, layout=torch.sparse_coo)
```

sparse_resize_(*size*, *sparse_dim*, *dense_dim*) → [Tensor](../tensors.html#torch.Tensor)

Resizes `self` [sparse tensor](../sparse.html#sparse-docs) to the desired
size and the number of sparse and dense dimensions.

Note

If the number of specified elements in `self` is zero, then
`size`, `sparse_dim`, and `dense_dim` can be any
size and positive integers such that `len(size) == sparse_dim +
dense_dim`.

If `self` specifies one or more elements, however, then each
dimension in `size` must not be smaller than the corresponding
dimension of `self`, `sparse_dim` must equal the number
of sparse dimensions in `self`, and `dense_dim` must
equal the number of dense dimensions in `self`.

Warning

Throws an error if `self` is not a sparse tensor.

Parameters:

- **size** ([*torch.Size*](../size.html#torch.Size)) - the desired size. If `self` is non-empty
sparse tensor, the desired size cannot be smaller than the
original size.
- **sparse_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the number of sparse dimensions
- **dense_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the number of dense dimensions

sparse_resize_and_clear_(*size*, *sparse_dim*, *dense_dim*) → [Tensor](../tensors.html#torch.Tensor)

Removes all specified elements from a [sparse tensor](../sparse.html#sparse-docs) `self` and resizes `self` to the desired
size and the number of sparse and dense dimensions.

Parameters:

- **size** ([*torch.Size*](../size.html#torch.Size)) - the desired size.
- **sparse_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the number of sparse dimensions
- **dense_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the number of dense dimensions

split(*split_size*, *dim=0*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L1054)

See [`torch.split()`](torch.split.html#torch.split)

sqrt() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.sqrt()`](torch.sqrt.html#torch.sqrt)

sqrt_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `sqrt()`

square() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.square()`](torch.square.html#torch.square)

square_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `square()`

squeeze(*dim=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.squeeze()`](torch.squeeze.html#torch.squeeze)

squeeze_(*dim=None*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `squeeze()`

sspaddmm(*mat1*, *mat2*, ***, *beta=1*, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.sspaddmm()`](torch.sspaddmm.html#torch.sspaddmm)

std(*dim=None*, ***, *correction=1*, *keepdim=False*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.std()`](torch.std.html#torch.std)

stft(*n_fft*, *hop_length=None*, *win_length=None*, *window=None*, *center=True*, *pad_mode='reflect'*, *normalized=False*, *onesided=None*, *return_complex=None*, *align_to_window=None*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L948)

See [`torch.stft()`](torch.stft.html#torch.stft)

Warning

This function changed signature at version 0.4.1. Calling with
the previous signature may cause error or return incorrect result.

storage() → [torch.TypedStorage](../storage.html#torch.TypedStorage)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L290)

Returns the underlying `TypedStorage`.

Warning

`TypedStorage` is deprecated. It will be removed in the future, and
`UntypedStorage` will be the only storage class. To access the
`UntypedStorage` directly, use `Tensor.untyped_storage()`.

storage_offset() → [int](https://docs.python.org/3/library/functions.html#int)

Returns `self` tensor's offset in the underlying storage in terms of
number of storage elements (not bytes).

Example:

```
>>> x = torch.tensor([1, 2, 3, 4, 5])
>>> x.storage_offset()
0
>>> x[3:].storage_offset()
3
```

storage_type() → [type](https://docs.python.org/3/library/functions.html#type)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L1340)

Returns the type of the underlying storage.

stride(*dim*) → tuple or int

Returns the stride of `self` tensor.

Stride is the jump necessary to go from one element to the next one in the
specified dimension `dim`. A tuple of all strides is returned when no
argument is passed in. Otherwise, an integer value is returned as the stride in
the particular dimension `dim`.

Parameters:

**dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the desired dimension in which stride is required

Example:

```
>>> x = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
>>> x.stride()
(5, 1)
>>> x.stride(0)
5
>>> x.stride(-1)
1
```

sub(*other*, ***, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.sub()`](torch.sub.html#torch.sub).

sub_(*other*, ***, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `sub()`

subtract(*other*, ***, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.subtract()`](torch.subtract.html#torch.subtract).

subtract_(*other*, ***, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `subtract()`.

sum(*dim=None*, *keepdim=False*, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.sum()`](torch.sum.html#torch.sum)

sum_to_size(**size*) → [Tensor](../tensors.html#torch.Tensor)

Sum `this` tensor to `size`.
`size` must be broadcastable to `this` tensor size.

Parameters:

**size** ([*int*](https://docs.python.org/3/library/functions.html#int)*...*) - a sequence of integers defining the shape of the output tensor.

svd(*some=True*, *compute_uv=True*)

See [`torch.svd()`](torch.svd.html#torch.svd)

swapaxes(*axis0*, *axis1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.swapaxes()`](torch.swapaxes.html#torch.swapaxes)

swapaxes_(*axis0*, *axis1*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `swapaxes()`

swapdims(*dim0*, *dim1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.swapdims()`](torch.swapdims.html#torch.swapdims)

swapdims_(*dim0*, *dim1*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `swapdims()`

t() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.t()`](torch.t.html#torch.t)

t_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `t()`

take(*indices*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.take()`](torch.take.html#torch.take)

take_along_dim(*indices*, *dim*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.take_along_dim()`](torch.take_along_dim.html#torch.take_along_dim)

tan() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.tan()`](torch.tan.html#torch.tan)

tan_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `tan()`

tanh() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.tanh()`](torch.tanh.html#torch.tanh)

tanh_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `tanh()`

tensor_split(*indices_or_sections*, *dim=0*) → List of Tensors

See [`torch.tensor_split()`](torch.tensor_split.html#torch.tensor_split)

tile(*dims*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.tile()`](torch.tile.html#torch.tile)

to(**args*, ***kwargs*) → [Tensor](../tensors.html#torch.Tensor)

Performs Tensor dtype and/or device conversion. A [`torch.dtype`](../tensor_attributes.html#torch.dtype) and [`torch.device`](../tensor_attributes.html#torch.device) are
inferred from the arguments of `self.to(*args, **kwargs)`.

Note

If the `self` Tensor already
has the correct [`torch.dtype`](../tensor_attributes.html#torch.dtype) and [`torch.device`](../tensor_attributes.html#torch.device), then `self` is returned.
Otherwise, the returned tensor is a copy of `self` with the desired
[`torch.dtype`](../tensor_attributes.html#torch.dtype) and [`torch.device`](../tensor_attributes.html#torch.device).

Note

If `self` requires gradients (`requires_grad=True`) but the target
`dtype` specified is an integer type, the returned tensor will implicitly
set `requires_grad=False`. This is because only tensors with
floating-point or complex dtypes can require gradients.

Here are the ways to call `to`:

to(*dtype*, *non_blocking=False*, *copy=False*, *memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

> Returns a Tensor with the specified `dtype`
> 
> 
> 
> Args:
> 
> memory_format ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional): the desired memory format of
> returned Tensor. Default: `torch.preserve_format`.

Note

According to [C++ type conversion rules](https://en.cppreference.com/w/cpp/language/implicit_conversion.html),
converting floating point value to integer type will truncate the fractional part.
If the truncated value cannot fit into the target type (e.g., casting `torch.inf` to `torch.long`),
the behavior is undefined and the result may vary across platforms.

to(*device=None*, *dtype=None*, *non_blocking=False*, *copy=False*, *memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

> Returns a Tensor with the specified `device` and (optional)
> `dtype`. If `dtype` is `None` it is inferred to be `self.dtype`.
> When `non_blocking` is set to `True`, the function attempts to perform
> the conversion asynchronously with respect to the host, if possible. This
> asynchronous behavior applies to both pinned and pageable memory. However,
> caution is advised when using this feature. For more information, refer to the
> [tutorial on good usage of non_blocking and pin_memory](https://pytorch.org/tutorials/intermediate/pinmem_nonblock.html).
> When `copy` is set, a new Tensor is created even when the Tensor
> already matches the desired conversion.
> 
> 
> 
> Args:
> 
> memory_format ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional): the desired memory format of
> returned Tensor. Default: `torch.preserve_format`.

to(*other*, *non_blocking=False*, *copy=False*) → [Tensor](../tensors.html#torch.Tensor)

> Returns a Tensor with same [`torch.dtype`](../tensor_attributes.html#torch.dtype) and [`torch.device`](../tensor_attributes.html#torch.device) as
> the Tensor `other`.
> When `non_blocking` is set to `True`, the function attempts to perform
> the conversion asynchronously with respect to the host, if possible. This
> asynchronous behavior applies to both pinned and pageable memory. However,
> caution is advised when using this feature. For more information, refer to the
> [tutorial on good usage of non_blocking and pin_memory](https://pytorch.org/tutorials/intermediate/pinmem_nonblock.html).
> When `copy` is set, a new Tensor is created even when the Tensor
> already matches the desired conversion.

Note

When `non_blocking` is `True` and the conversion is issued on
a non-default CUDA stream, the caller is responsible for proper
cross-stream synchronization. See [CUDA streams](../notes/cuda.html#cuda-stream-semantics) for
the required pattern.

Example:

```
>>> tensor = torch.randn(2, 2) # Initially dtype=float32, device=cpu
>>> tensor.to(torch.float64)
tensor([[-0.5044, 0.0005],
 [ 0.3310, -0.0584]], dtype=torch.float64)

>>> cuda0 = torch.device('cuda:0')
>>> tensor.to(cuda0)
tensor([[-0.5044, 0.0005],
 [ 0.3310, -0.0584]], device='cuda:0')

>>> tensor.to(cuda0, dtype=torch.float64)
tensor([[-0.5044, 0.0005],
 [ 0.3310, -0.0584]], dtype=torch.float64, device='cuda:0')

>>> other = torch.randn((), dtype=torch.float64, device=cuda0)
>>> tensor.to(other, non_blocking=True)
tensor([[-0.5044, 0.0005],
 [ 0.3310, -0.0584]], dtype=torch.float64, device='cuda:0')
```

to_mkldnn() → [Tensor](../tensors.html#torch.Tensor)

Returns a copy of the tensor in `torch.mkldnn` layout.

to_padded_tensor(*padding*, *output_size=None*) → [Tensor](../tensors.html#torch.Tensor)

See `to_padded_tensor()`

to_sparse(*sparseDims*) → [Tensor](../tensors.html#torch.Tensor)

Returns a sparse copy of the tensor. PyTorch supports sparse tensors in
[coordinate format](../sparse.html#sparse-coo-docs).

Parameters:

**sparseDims** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the number of sparse dimensions to include in the new sparse tensor

Example:

```
>>> d = torch.tensor([[0, 0, 0], [9, 0, 10], [0, 0, 0]])
>>> d
tensor([[ 0, 0, 0],
 [ 9, 0, 10],
 [ 0, 0, 0]])
>>> d.to_sparse()
tensor(indices=tensor([[1, 1],
 [0, 2]]),
 values=tensor([ 9, 10]),
 size=(3, 3), nnz=2, layout=torch.sparse_coo)
>>> d.to_sparse(1)
tensor(indices=tensor([[1]]),
 values=tensor([[ 9, 0, 10]]),
 size=(3, 3), nnz=1, layout=torch.sparse_coo)
```

to_sparse(***, *layout=None*, *blocksize=None*, *dense_dim=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns a sparse tensor with the specified layout and blocksize. If
the `self` is strided, the number of dense dimensions could be
specified, and a hybrid sparse tensor will be created, with
dense_dim dense dimensions and self.dim() - 2 - dense_dim batch
dimension.

Note

If the `self` layout and blocksize parameters match
with the specified layout and blocksize, return
`self`. Otherwise, return a sparse tensor copy of
`self`.

Parameters:

- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - The desired sparse
layout. One of `torch.sparse_coo`, `torch.sparse_csr`,
`torch.sparse_csc`, `torch.sparse_bsr`, or
`torch.sparse_bsc`. Default: if `None`,
`torch.sparse_coo`.
- **blocksize** (list, tuple, [`torch.Size`](../size.html#torch.Size), optional) - Block size
of the resulting BSR or BSC tensor. For other layouts,
specifying the block size that is not `None` will result in a
RuntimeError exception. A block size must be a tuple of length
two such that its items evenly divide the two sparse dimensions.
- **dense_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Number of dense dimensions of the
resulting CSR, CSC, BSR or BSC tensor. This argument should be
used only if `self` is a strided tensor, and must be a
value between 0 and dimension of `self` tensor minus two.

Example:

```
>>> x = torch.tensor([[1, 0], [0, 0], [2, 3]])
>>> x.to_sparse(layout=torch.sparse_coo)
tensor(indices=tensor([[0, 2, 2],
 [0, 0, 1]]),
 values=tensor([1, 2, 3]),
 size=(3, 2), nnz=3, layout=torch.sparse_coo)
>>> x.to_sparse(layout=torch.sparse_bsr, blocksize=(1, 2))
tensor(crow_indices=tensor([0, 1, 1, 2]),
 col_indices=tensor([0, 0]),
 values=tensor([[[1, 0]],
 [[2, 3]]]), size=(3, 2), nnz=2, layout=torch.sparse_bsr)
>>> x.to_sparse(layout=torch.sparse_bsr, blocksize=(2, 1))
RuntimeError: Tensor size(-2) 3 needs to be divisible by blocksize[0] 2
>>> x.to_sparse(layout=torch.sparse_csr, blocksize=(3, 1))
RuntimeError: to_sparse for Strided to SparseCsr conversion does not use specified blocksize

>>> x = torch.tensor([[[1], [0]], [[0], [0]], [[2], [3]]])
>>> x.to_sparse(layout=torch.sparse_csr, dense_dim=1)
tensor(crow_indices=tensor([0, 1, 1, 3]),
 col_indices=tensor([0, 0, 1]),
 values=tensor([[1],
 [2],
 [3]]), size=(3, 2, 1), nnz=3, layout=torch.sparse_csr)
```

to_sparse_bsc(*blocksize*, *dense_dim*) → [Tensor](../tensors.html#torch.Tensor)

Convert a tensor to a block sparse column (BSC) storage format of
given blocksize. If the `self` is strided, then the number of
dense dimensions could be specified, and a hybrid BSC tensor will be
created, with dense_dim dense dimensions and self.dim() - 2 -
dense_dim batch dimension.

Parameters:

- **blocksize** (list, tuple, [`torch.Size`](../size.html#torch.Size), optional) - Block size
of the resulting BSC tensor. A block size must be a tuple of
length two such that its items evenly divide the two sparse
dimensions.
- **dense_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Number of dense dimensions of the
resulting BSC tensor. This argument should be used only if
`self` is a strided tensor, and must be a value between 0
and dimension of `self` tensor minus two.

Example:

```
>>> dense = torch.randn(10, 10)
>>> sparse = dense.to_sparse_csr()
>>> sparse_bsc = sparse.to_sparse_bsc((5, 5))
>>> sparse_bsc.row_indices()
tensor([0, 1, 0, 1])

>>> dense = torch.zeros(4, 3, 1)
>>> dense[0:2, 0] = dense[0:2, 2] = dense[2:4, 1] = 1
>>> dense.to_sparse_bsc((2, 1), 1)
tensor(ccol_indices=tensor([0, 1, 2, 3]),
 row_indices=tensor([0, 1, 0]),
 values=tensor([[[[1.]],

 [[1.]]],

 [[[1.]],

 [[1.]]],

 [[[1.]],

 [[1.]]]]), size=(4, 3, 1), nnz=3,
 layout=torch.sparse_bsc)
```

to_sparse_bsr(*blocksize*, *dense_dim*) → [Tensor](../tensors.html#torch.Tensor)

Convert a tensor to a block sparse row (BSR) storage format of given
blocksize. If the `self` is strided, then the number of dense
dimensions could be specified, and a hybrid BSR tensor will be
created, with dense_dim dense dimensions and self.dim() - 2 -
dense_dim batch dimension.

Parameters:

- **blocksize** (list, tuple, [`torch.Size`](../size.html#torch.Size), optional) - Block size
of the resulting BSR tensor. A block size must be a tuple of
length two such that its items evenly divide the two sparse
dimensions.
- **dense_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Number of dense dimensions of the
resulting BSR tensor. This argument should be used only if
`self` is a strided tensor, and must be a value between 0
and dimension of `self` tensor minus two.

Example:

```
>>> dense = torch.randn(10, 10)
>>> sparse = dense.to_sparse_csr()
>>> sparse_bsr = sparse.to_sparse_bsr((5, 5))
>>> sparse_bsr.col_indices()
tensor([0, 1, 0, 1])

>>> dense = torch.zeros(4, 3, 1)
>>> dense[0:2, 0] = dense[0:2, 2] = dense[2:4, 1] = 1
>>> dense.to_sparse_bsr((2, 1), 1)
tensor(crow_indices=tensor([0, 2, 3]),
 col_indices=tensor([0, 2, 1]),
 values=tensor([[[[1.]],

 [[1.]]],

 [[[1.]],

 [[1.]]],

 [[[1.]],

 [[1.]]]]), size=(4, 3, 1), nnz=3,
 layout=torch.sparse_bsr)
```

to_sparse_coo()[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L1368)

Convert a tensor to [coordinate format](../sparse.html#sparse-coo-docs).

Examples:

```
>>> dense = torch.randn(5, 5)
>>> sparse = dense.to_sparse_coo()
>>> sparse._nnz()
25
```

to_sparse_csc() → [Tensor](../tensors.html#torch.Tensor)

Convert a tensor to compressed column storage (CSC) format. Except
for strided tensors, only works with 2D tensors. If the `self`
is strided, then the number of dense dimensions could be specified,
and a hybrid CSC tensor will be created, with dense_dim dense
dimensions and self.dim() - 2 - dense_dim batch dimension.

Parameters:

**dense_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Number of dense dimensions of the
resulting CSC tensor. This argument should be used only if
`self` is a strided tensor, and must be a value between 0
and dimension of `self` tensor minus two.

Example:

```
>>> dense = torch.randn(5, 5)
>>> sparse = dense.to_sparse_csc()
>>> sparse._nnz()
25

>>> dense = torch.zeros(3, 3, 1, 1)
>>> dense[0, 0] = dense[1, 2] = dense[2, 1] = 1
>>> dense.to_sparse_csc(dense_dim=2)
tensor(ccol_indices=tensor([0, 1, 2, 3]),
 row_indices=tensor([0, 2, 1]),
 values=tensor([[[1.]],

 [[1.]],

 [[1.]]]), size=(3, 3, 1, 1), nnz=3,
 layout=torch.sparse_csc)
```

to_sparse_csr(*dense_dim=None*) → [Tensor](../tensors.html#torch.Tensor)

Convert a tensor to compressed row storage format (CSR). Except for
strided tensors, only works with 2D tensors. If the `self` is
strided, then the number of dense dimensions could be specified, and a
hybrid CSR tensor will be created, with dense_dim dense dimensions
and self.dim() - 2 - dense_dim batch dimension.

Parameters:

**dense_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Number of dense dimensions of the
resulting CSR tensor. This argument should be used only if
`self` is a strided tensor, and must be a value between 0
and dimension of `self` tensor minus two.

Example:

```
>>> dense = torch.randn(5, 5)
>>> sparse = dense.to_sparse_csr()
>>> sparse._nnz()
25

>>> dense = torch.zeros(3, 3, 1, 1)
>>> dense[0, 0] = dense[1, 2] = dense[2, 1] = 1
>>> dense.to_sparse_csr(dense_dim=2)
tensor(crow_indices=tensor([0, 1, 2, 3]),
 col_indices=tensor([0, 2, 1]),
 values=tensor([[[1.]],

 [[1.]],

 [[1.]]]), size=(3, 3, 1, 1), nnz=3,
 layout=torch.sparse_csr)
```

tolist() → list or number

Returns the tensor as a (nested) list. For scalars, a standard
Python number is returned, just like with `item()`.
Tensors are automatically moved to the CPU first if necessary.

This operation is not differentiable.

Examples:

```
>>> a = torch.randn(2, 2)
>>> a.tolist()
[[0.012766935862600803, 0.5415473580360413],
 [-0.08909505605697632, 0.7729271650314331]]
>>> a[0,0].tolist()
0.012766935862600803
```

topk(*k*, *dim=None*, *largest=True*, *sorted=True*)

See [`torch.topk()`](torch.topk.html#torch.topk)

trace() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.trace()`](torch.trace.html#torch.trace)

transpose(*dim0*, *dim1*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.transpose()`](torch.transpose.html#torch.transpose)

transpose_(*dim0*, *dim1*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `transpose()`

triangular_solve(*A*, *upper=True*, *transpose=False*, *unitriangular=False*)

See [`torch.triangular_solve()`](torch.triangular_solve.html#torch.triangular_solve)

tril(*diagonal=0*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.tril()`](torch.tril.html#torch.tril)

tril_(*diagonal=0*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `tril()`

triu(*diagonal=0*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.triu()`](torch.triu.html#torch.triu)

triu_(*diagonal=0*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `triu()`

true_divide(*value*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.true_divide()`](torch.true_divide.html#torch.true_divide)

true_divide_(*value*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `true_divide_()`

trunc() → [Tensor](../tensors.html#torch.Tensor)

See [`torch.trunc()`](torch.trunc.html#torch.trunc)

trunc_() → [Tensor](../tensors.html#torch.Tensor)

In-place version of `trunc()`

type(*dtype=None*, *non_blocking=False*, ***kwargs*) → str or Tensor

Returns the type if dtype is not provided, else casts this object to
the specified type.

If this is already of the correct type, no copy is performed and the
original object is returned.

Parameters:

- **dtype** ([*dtype*](../tensor_attributes.html#torch.dtype)*or**string*) - The desired type
- **non_blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If `True`, and the source is in pinned memory
and destination is on the GPU or vice versa, the copy is performed
asynchronously with respect to the host. Otherwise, the argument
has no effect.
- ****kwargs** - For compatibility, may contain the key `async` in place of
the `non_blocking` argument. The `async` arg is deprecated.

type_as(*tensor*) → [Tensor](../tensors.html#torch.Tensor)

Returns this tensor cast to the type of the given tensor.

This is a no-op if the tensor is already of the correct type. This is
equivalent to `self.type(tensor.type())`

Parameters:

**tensor** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor which has the desired type

unbind(*dim=0*) → seq

See [`torch.unbind()`](torch.unbind.html#torch.unbind)

unflatten(*dim*, *sizes*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L1353)

See [`torch.unflatten()`](torch.unflatten.html#torch.unflatten).

unfold(*dimension*, *size*, *step*) → [Tensor](../tensors.html#torch.Tensor)

Returns a view of the original tensor which contains all slices of size `size` from
`self` tensor in the dimension `dimension`.

Step between two slices is given by `step`.

If sizedim is the size of dimension `dimension` for `self`, the size of
dimension `dimension` in the returned tensor will be
(sizedim - size) / step + 1.

An additional dimension of size `size` is appended in the returned tensor.

Parameters:

- **dimension** ([*int*](https://docs.python.org/3/library/functions.html#int)) - dimension in which unfolding happens
- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the size of each slice that is unfolded
- **step** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the step between each slice

Example:

```
>>> x = torch.arange(1., 8)
>>> x
tensor([ 1., 2., 3., 4., 5., 6., 7.])
>>> x.unfold(0, 2, 1)
tensor([[ 1., 2.],
 [ 2., 3.],
 [ 3., 4.],
 [ 4., 5.],
 [ 5., 6.],
 [ 6., 7.]])
>>> x.unfold(0, 2, 2)
tensor([[ 1., 2.],
 [ 3., 4.],
 [ 5., 6.]])
```

uniform_(*from=0*, *to=1*, ***, *generator=None*) → [Tensor](../tensors.html#torch.Tensor)

Fills `self` tensor with numbers sampled from the continuous uniform
distribution:

f(x)=1to−fromf(x) = \dfrac{1}{\text{to} - \text{from}}

f(x)=to−from1​

unique(*sorted=True*, *return_inverse=False*, *return_counts=False*, *dim=None*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L1075)

Returns the unique elements of the input tensor.

See [`torch.unique()`](torch.unique.html#torch.unique)

unique_consecutive(*return_inverse=False*, *return_counts=False*, *dim=None*)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/_tensor.py#L1098)

Eliminates all but the first element from every consecutive group of equivalent elements.

See [`torch.unique_consecutive()`](torch.unique_consecutive.html#torch.unique_consecutive)

unsafe_chunk(*chunks*, *dim=0*) → List of Tensors

See `torch.unsafe_chunk()`

unsafe_split(*split_size*, *dim=0*) → List of Tensors

See `torch.unsafe_split()`

unsqueeze(*dim*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.unsqueeze()`](torch.unsqueeze.html#torch.unsqueeze)

unsqueeze_(*dim*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `unsqueeze()`

untyped_storage() → [torch.UntypedStorage](../storage.html#torch.UntypedStorage)

Returns the underlying `UntypedStorage`.

values() → [Tensor](../tensors.html#torch.Tensor)

Return the values tensor of a [sparse COO tensor](../sparse.html#sparse-coo-docs).

Warning

Throws an error if `self` is not a sparse COO tensor.

See also `Tensor.indices()`.

Note

This method can only be called on a coalesced sparse tensor. See
`Tensor.coalesce()` for details.

var(*dim=None*, ***, *correction=1*, *keepdim=False*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.var()`](torch.var.html#torch.var)

vdot(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.vdot()`](torch.vdot.html#torch.vdot)

view(**shape*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the same data as the `self` tensor but of a
different `shape`.

The returned tensor shares the same data and must have the same number
of elements, but may have a different size. For a tensor to be viewed, the new
view size must be compatible with its original size and stride, i.e., each new
view dimension must either be a subspace of an original dimension, or only span
across original dimensions d,d+1,...,d+kd, d+1, \dots, d+kd,d+1,...,d+k that satisfy the following
contiguity-like condition that ∀i=d,...,d+k−1\forall i = d, \dots, d+k-1∀i=d,...,d+k−1,

stride[i]=stride[i+1]×size[i+1]\text{stride}[i] = \text{stride}[i+1] \times \text{size}[i+1]stride[i]=stride[i+1]×size[i+1]

Otherwise, it will not be possible to view `self` tensor as `shape`
without copying it (e.g., via `contiguous()`). When it is unclear whether a
`view()` can be performed, it is advisable to use `reshape()`, which
returns a view if the shapes are compatible, and copies (equivalent to calling
`contiguous()`) otherwise.

Parameters:

**shape** ([*torch.Size*](../size.html#torch.Size)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*...*) - the desired size

Example:

```
>>> x = torch.randn(4, 4)
>>> x.size()
torch.Size([4, 4])
>>> y = x.view(16)
>>> y.size()
torch.Size([16])
>>> z = x.view(-1, 8) # the size -1 is inferred from other dimensions
>>> z.size()
torch.Size([2, 8])

>>> a = torch.randn(1, 2, 3, 4)
>>> a.size()
torch.Size([1, 2, 3, 4])
>>> b = a.transpose(1, 2) # Swaps 2nd and 3rd dimension
>>> b.size()
torch.Size([1, 3, 2, 4])
>>> c = a.view(1, 3, 2, 4) # Does not change tensor layout in memory
>>> c.size()
torch.Size([1, 3, 2, 4])
>>> torch.equal(b, c)
False
```

view(*dtype*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the same data as the `self` tensor but of a
different `dtype`.

If the element size of `dtype` is different than that of `self.dtype`,
then the size of the last dimension of the output will be scaled
proportionally. For instance, if `dtype` element size is twice that of
`self.dtype`, then each pair of elements in the last dimension of
`self` will be combined, and the size of the last dimension of the output
will be half that of `self`. If `dtype` element size is half that
of `self.dtype`, then each element in the last dimension of `self` will
be split in two, and the size of the last dimension of the output will be
double that of `self`. For this to be possible, the following conditions
must be true:

> - `self.dim()` must be greater than 0.
> - `self.stride(-1)` must be 1.

Additionally, if the element size of `dtype` is greater than that of
`self.dtype`, the following conditions must be true as well:

> - `self.size(-1)` must be divisible by the ratio between the element
> sizes of the dtypes.
> - `self.storage_offset()` must be divisible by the ratio between the
> element sizes of the dtypes.
> - The strides of all dimensions, except the last dimension, must be
> divisible by the ratio between the element sizes of the dtypes.

If any of the above conditions are not met, an error is thrown.

Warning

This overload is not supported by TorchScript, and using it in a Torchscript
program will cause undefined behavior.

Parameters:

**dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype)) - the desired dtype

Example:

```
>>> x = torch.randn(4, 4)
>>> x
tensor([[ 0.9482, -0.0310, 1.4999, -0.5316],
 [-0.1520, 0.7472, 0.5617, -0.8649],
 [-2.4724, -0.0334, -0.2976, -0.8499],
 [-0.2109, 1.9913, -0.9607, -0.6123]])
>>> x.dtype
torch.float32

>>> y = x.view(torch.int32)
>>> y
tensor([[ 1064483442, -1124191867, 1069546515, -1089989247],
 [-1105482831, 1061112040, 1057999968, -1084397505],
 [-1071760287, -1123489973, -1097310419, -1084649136],
 [-1101533110, 1073668768, -1082790149, -1088634448]],
 dtype=torch.int32)
>>> y[0, 0] = 1000000000
>>> x
tensor([[ 0.0047, -0.0310, 1.4999, -0.5316],
 [-0.1520, 0.7472, 0.5617, -0.8649],
 [-2.4724, -0.0334, -0.2976, -0.8499],
 [-0.2109, 1.9913, -0.9607, -0.6123]])

>>> x.view(torch.cfloat)
tensor([[ 0.0047-0.0310j, 1.4999-0.5316j],
 [-0.1520+0.7472j, 0.5617-0.8649j],
 [-2.4724-0.0334j, -0.2976-0.8499j],
 [-0.2109+1.9913j, -0.9607-0.6123j]])
>>> x.view(torch.cfloat).size()
torch.Size([4, 2])

>>> x.view(torch.uint8)
tensor([[ 0, 202, 154, 59, 182, 243, 253, 188, 185, 252, 191, 63, 240, 22,
 8, 191],
 [227, 165, 27, 190, 128, 72, 63, 63, 146, 203, 15, 63, 22, 106,
 93, 191],
 [205, 59, 30, 192, 112, 206, 8, 189, 7, 95, 152, 190, 12, 147,
 89, 191],
 [ 43, 246, 87, 190, 235, 226, 254, 63, 111, 240, 117, 191, 177, 191,
 28, 191]], dtype=torch.uint8)
>>> x.view(torch.uint8).size()
torch.Size([4, 16])
```

view_as(*other*) → [Tensor](../tensors.html#torch.Tensor)

View this tensor as the same size as `other`.
`self.view_as(other)` is equivalent to `self.view(other.size())`.

Please see `view()` for more information about `view`.

Parameters:

**other** ([`torch.Tensor`](../tensors.html#torch.Tensor)) - The result tensor has the same size
as `other`.

vsplit(*split_size_or_sections*) → List of Tensors

See [`torch.vsplit()`](torch.vsplit.html#torch.vsplit)

where(*condition*, *y*) → [Tensor](../tensors.html#torch.Tensor)

`self.where(condition, y)` is equivalent to `torch.where(condition, self, y)`.
See [`torch.where()`](torch.where.html#torch.where)

xlogy(*other*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.xlogy()`](torch.xlogy.html#torch.xlogy)

xlogy_(*other*) → [Tensor](../tensors.html#torch.Tensor)

In-place version of `xlogy()`

xpu(*device=None*, *non_blocking=False*, *memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

Returns a copy of this object in XPU memory.

If this object is already in XPU memory and on the correct device,
then no copy is performed and the original object is returned.

Parameters:

- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - The destination XPU device.
Defaults to the current XPU device.
- **non_blocking** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If `True` and the source is in pinned memory,
the copy will be asynchronous with respect to the host.
Otherwise, the argument has no effect. Default: `False`.
- **memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

zero_() → [Tensor](../tensors.html#torch.Tensor)

Fills `self` tensor with zeros.