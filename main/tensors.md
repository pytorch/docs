# torch.Tensor

A `torch.Tensor` is a multi-dimensional matrix containing elements of
a single data type. Please see [torch.dtype](tensor_attributes.html#dtype-doc) for more details about dtype support.

## Initializing and basic operations

A tensor can be constructed from a Python [`list`](https://docs.python.org/3/library/stdtypes.html#list) or sequence using the
[`torch.tensor()`](generated/torch.tensor.html#torch.tensor) constructor:

```
>>> torch.tensor([[1., -1.], [1., -1.]])
tensor([[ 1.0000, -1.0000],
 [ 1.0000, -1.0000]])
>>> torch.tensor(np.array([[1, 2, 3], [4, 5, 6]]))
tensor([[ 1, 2, 3],
 [ 4, 5, 6]])
```

Warning

[`torch.tensor()`](generated/torch.tensor.html#torch.tensor) always copies `data`. If you have a Tensor
`data` and just want to change its `requires_grad` flag, use
[`requires_grad_()`](generated/torch.Tensor.requires_grad_.html#torch.Tensor.requires_grad_) or
[`detach()`](generated/torch.Tensor.detach.html#torch.Tensor.detach) to avoid a copy.
If you have a numpy array and want to avoid a copy, use
[`torch.as_tensor()`](generated/torch.as_tensor.html#torch.as_tensor).

A tensor of specific data type can be constructed by passing a
[`torch.dtype`](tensor_attributes.html#torch.dtype) and/or a [`torch.device`](tensor_attributes.html#torch.device) to a
constructor or tensor creation op:

```
>>> torch.zeros([2, 4], dtype=torch.int32)
tensor([[ 0, 0, 0, 0],
 [ 0, 0, 0, 0]], dtype=torch.int32)
>>> cuda0 = torch.device('cuda:0')
>>> torch.ones([2, 4], dtype=torch.float64, device=cuda0)
tensor([[ 1.0000, 1.0000, 1.0000, 1.0000],
 [ 1.0000, 1.0000, 1.0000, 1.0000]], dtype=torch.float64, device='cuda:0')
```

For more information about building Tensors, see [Creation Ops](torch.html#tensor-creation-ops)

The contents of a tensor can be accessed and modified using Python's indexing
and slicing notation:

```
>>> x = torch.tensor([[1, 2, 3], [4, 5, 6]])
>>> print(x[1][2])
tensor(6)
>>> x[0][1] = 8
>>> print(x)
tensor([[ 1, 8, 3],
 [ 4, 5, 6]])
```

Use [`torch.Tensor.item()`](generated/torch.Tensor.item.html#torch.Tensor.item) to get a Python number from a tensor containing a
single value:

```
>>> x = torch.tensor([[1]])
>>> x
tensor([[ 1]])
>>> x.item()
1
>>> x = torch.tensor(2.5)
>>> x
tensor(2.5000)
>>> x.item()
2.5
```

For more information about indexing, see [Indexing, Slicing, Joining, Mutating Ops](torch.html#indexing-slicing-joining)

A tensor can be created with `requires_grad=True` so that
[`torch.autograd`](autograd.html#module-torch.autograd) records operations on them for automatic differentiation.

```
>>> x = torch.tensor([[1., -1.], [1., 1.]], requires_grad=True)
>>> out = x.pow(2).sum()
>>> out.backward()
>>> x.grad
tensor([[ 2.0000, -2.0000],
 [ 2.0000, 2.0000]])
```

Each tensor has an associated `torch.Storage`, which holds its data.
The tensor class also provides multi-dimensional, [strided](https://en.wikipedia.org/wiki/Stride_of_an_array)
view of a storage and defines numeric operations on it.

Note

For more information on tensor views, see [Tensor Views](tensor_view.html#tensor-view-doc).

Note

For more information on the [`torch.dtype`](tensor_attributes.html#torch.dtype), [`torch.device`](tensor_attributes.html#torch.device), and
[`torch.layout`](tensor_attributes.html#torch.layout) attributes of a `torch.Tensor`, see
[Tensor Attributes](tensor_attributes.html#tensor-attributes-doc).

Note

Methods which mutate a tensor are marked with an underscore suffix.
For example, `torch.FloatTensor.abs_()` computes the absolute value
in-place and returns the modified tensor, while `torch.FloatTensor.abs()`
computes the result in a new tensor.

Note

To change an existing tensor's [`torch.device`](tensor_attributes.html#torch.device) and/or [`torch.dtype`](tensor_attributes.html#torch.dtype), consider using
[`to()`](generated/torch.Tensor.to.html#torch.Tensor.to) method on the tensor.

Warning

Current implementation of `torch.Tensor` introduces memory overhead,
thus it might lead to unexpectedly high memory usage in the applications with many tiny tensors.
If this is your case, consider using one large structure.

## Tensor class reference

*class*torch.Tensor

There are a few main ways to create a tensor, depending on your use case.

- To create a tensor with pre-existing data, use [`torch.tensor()`](generated/torch.tensor.html#torch.tensor).
- To create a tensor with specific size, use `torch.*` tensor creation
ops (see [Creation Ops](torch.html#tensor-creation-ops)).
- To create a tensor with the same size (and similar types) as another tensor,
use `torch.*_like` tensor creation ops
(see [Creation Ops](torch.html#tensor-creation-ops)).
- To create a tensor with similar type but different size as another tensor,
use `tensor.new_*` creation ops.
- There is a legacy constructor `torch.Tensor` whose use is discouraged.
Use [`torch.tensor()`](generated/torch.tensor.html#torch.tensor) instead.

Tensor.__init__(*self*, *data*)

This constructor is deprecated, we recommend using [`torch.tensor()`](generated/torch.tensor.html#torch.tensor) instead.
What this constructor does depends on the type of `data`.

- If `data` is a Tensor, returns an alias to the original Tensor. Unlike
[`torch.tensor()`](generated/torch.tensor.html#torch.tensor), this tracks autograd and will propagate gradients to
the original Tensor. `device` kwarg is not supported for this `data` type.
- If `data` is a sequence or nested sequence, create a tensor of the default
dtype (typically `torch.float32`) whose data is the values in the
sequences, performing coercions if necessary. Notably, this differs from
[`torch.tensor()`](generated/torch.tensor.html#torch.tensor) in that this constructor will always construct a float
tensor, even if the inputs are all integers.
- If `data` is a [`torch.Size`](size.html#torch.Size), returns an empty tensor of that size.

This constructor does not support explicitly specifying `dtype` or `device` of
the returned tensor. We recommend using [`torch.tensor()`](generated/torch.tensor.html#torch.tensor) which provides this
functionality.

Args:

data (array_like): The tensor to construct from.

Keyword args:
device ([`torch.device`](tensor_attributes.html#torch.device), optional): the desired device of returned tensor.

Default: if None, same [`torch.device`](tensor_attributes.html#torch.device) as this tensor.

Tensor.T

Returns a view of this tensor with its dimensions reversed.

If `n` is the number of dimensions in `x`,
`x.T` is equivalent to `x.permute(n-1, n-2, ..., 0)`.

Warning

The use of `Tensor.T()` on tensors of dimension other than 2 to reverse their shape
is deprecated and it will throw an error in a future release. Consider `mT`
to transpose batches of matrices or x.permute(*torch.arange(x.ndim - 1, -1, -1)) to reverse
the dimensions of a tensor.

Tensor.H

Returns a view of a matrix (2-D tensor) conjugated and transposed.

`x.H` is equivalent to `x.transpose(0, 1).conj()` for complex matrices and
`x.transpose(0, 1)` for real matrices.

See also

`mH`: An attribute that also works on batches of matrices.

Tensor.mT

Returns a view of this tensor with the last two dimensions transposed.

`x.mT` is equivalent to `x.transpose(-2, -1)`.

Tensor.mH

Accessing this property is equivalent to calling [`adjoint()`](generated/torch.adjoint.html#torch.adjoint).

| [`Tensor.new_tensor`](generated/torch.Tensor.new_tensor.html#torch.Tensor.new_tensor) | Returns a new Tensor with `data` as the tensor data. |
| --- | --- |
| [`Tensor.new_full`](generated/torch.Tensor.new_full.html#torch.Tensor.new_full) | Returns a Tensor of size `size` filled with `fill_value`. |
| [`Tensor.new_empty`](generated/torch.Tensor.new_empty.html#torch.Tensor.new_empty) | Returns a Tensor of size `size` filled with uninitialized data. |
| [`Tensor.new_ones`](generated/torch.Tensor.new_ones.html#torch.Tensor.new_ones) | Returns a Tensor of size `size` filled with `1`. |
| [`Tensor.new_zeros`](generated/torch.Tensor.new_zeros.html#torch.Tensor.new_zeros) | Returns a Tensor of size `size` filled with `0`. |
| [`Tensor.is_cuda`](generated/torch.Tensor.is_cuda.html#torch.Tensor.is_cuda) | Is `True` if the Tensor is stored on the GPU, `False` otherwise. |
| [`Tensor.is_quantized`](generated/torch.Tensor.is_quantized.html#torch.Tensor.is_quantized) | Is `True` if the Tensor is quantized, `False` otherwise. |
| [`Tensor.is_meta`](generated/torch.Tensor.is_meta.html#torch.Tensor.is_meta) | Is `True` if the Tensor is a meta tensor, `False` otherwise. |
| [`Tensor.device`](generated/torch.Tensor.device.html#torch.Tensor.device) | Is the [`torch.device`](tensor_attributes.html#torch.device) where this Tensor is. |
| [`Tensor.grad`](generated/torch.Tensor.grad.html#torch.Tensor.grad) | This attribute is `None` by default and becomes a Tensor the first time a call to `backward()` computes gradients for `self`. |
| [`Tensor.ndim`](generated/torch.Tensor.ndim.html#torch.Tensor.ndim) | Alias for [`dim()`](generated/torch.Tensor.dim.html#torch.Tensor.dim) |
| [`Tensor.real`](generated/torch.Tensor.real.html#torch.Tensor.real) | Returns a new tensor containing real values of the `self` tensor for a complex-valued input tensor. |
| [`Tensor.imag`](generated/torch.Tensor.imag.html#torch.Tensor.imag) | Returns a new tensor containing imaginary values of the `self` tensor. |
| [`Tensor.nbytes`](generated/torch.Tensor.nbytes.html#torch.Tensor.nbytes) | Returns the number of bytes consumed by the "view" of elements of the Tensor if the Tensor does not use sparse storage layout. |
| [`Tensor.itemsize`](generated/torch.Tensor.itemsize.html#torch.Tensor.itemsize) | Alias for [`element_size()`](generated/torch.Tensor.element_size.html#torch.Tensor.element_size) |
| [`Tensor.abs`](generated/torch.Tensor.abs.html#torch.Tensor.abs) | See [`torch.abs()`](generated/torch.abs.html#torch.abs) |
| [`Tensor.abs_`](generated/torch.Tensor.abs_.html#torch.Tensor.abs_) | In-place version of [`abs()`](generated/torch.Tensor.abs.html#torch.Tensor.abs) |
| [`Tensor.absolute`](generated/torch.Tensor.absolute.html#torch.Tensor.absolute) | Alias for [`abs()`](generated/torch.abs.html#torch.abs) |
| [`Tensor.absolute_`](generated/torch.Tensor.absolute_.html#torch.Tensor.absolute_) | In-place version of [`absolute()`](generated/torch.Tensor.absolute.html#torch.Tensor.absolute) Alias for [`abs_()`](generated/torch.abs_.html#torch.abs_) |
| [`Tensor.acos`](generated/torch.Tensor.acos.html#torch.Tensor.acos) | See [`torch.acos()`](generated/torch.acos.html#torch.acos) |
| [`Tensor.acos_`](generated/torch.Tensor.acos_.html#torch.Tensor.acos_) | In-place version of [`acos()`](generated/torch.Tensor.acos.html#torch.Tensor.acos) |
| [`Tensor.arccos`](generated/torch.Tensor.arccos.html#torch.Tensor.arccos) | See [`torch.arccos()`](generated/torch.arccos.html#torch.arccos) |
| [`Tensor.arccos_`](generated/torch.Tensor.arccos_.html#torch.Tensor.arccos_) | In-place version of [`arccos()`](generated/torch.Tensor.arccos.html#torch.Tensor.arccos) |
| [`Tensor.add`](generated/torch.Tensor.add.html#torch.Tensor.add) | Add a scalar or tensor to `self` tensor. |
| [`Tensor.add_`](generated/torch.Tensor.add_.html#torch.Tensor.add_) | In-place version of [`add()`](generated/torch.Tensor.add.html#torch.Tensor.add) |
| [`Tensor.addbmm`](generated/torch.Tensor.addbmm.html#torch.Tensor.addbmm) | See [`torch.addbmm()`](generated/torch.addbmm.html#torch.addbmm) |
| [`Tensor.addbmm_`](generated/torch.Tensor.addbmm_.html#torch.Tensor.addbmm_) | In-place version of [`addbmm()`](generated/torch.Tensor.addbmm.html#torch.Tensor.addbmm) |
| [`Tensor.addcdiv`](generated/torch.Tensor.addcdiv.html#torch.Tensor.addcdiv) | See [`torch.addcdiv()`](generated/torch.addcdiv.html#torch.addcdiv) |
| [`Tensor.addcdiv_`](generated/torch.Tensor.addcdiv_.html#torch.Tensor.addcdiv_) | In-place version of [`addcdiv()`](generated/torch.Tensor.addcdiv.html#torch.Tensor.addcdiv) |
| [`Tensor.addcmul`](generated/torch.Tensor.addcmul.html#torch.Tensor.addcmul) | See [`torch.addcmul()`](generated/torch.addcmul.html#torch.addcmul) |
| [`Tensor.addcmul_`](generated/torch.Tensor.addcmul_.html#torch.Tensor.addcmul_) | In-place version of [`addcmul()`](generated/torch.Tensor.addcmul.html#torch.Tensor.addcmul) |
| [`Tensor.addmm`](generated/torch.Tensor.addmm.html#torch.Tensor.addmm) | See [`torch.addmm()`](generated/torch.addmm.html#torch.addmm) |
| [`Tensor.addmm_`](generated/torch.Tensor.addmm_.html#torch.Tensor.addmm_) | In-place version of [`addmm()`](generated/torch.Tensor.addmm.html#torch.Tensor.addmm) |
| [`Tensor.sspaddmm`](generated/torch.Tensor.sspaddmm.html#torch.Tensor.sspaddmm) | See [`torch.sspaddmm()`](generated/torch.sspaddmm.html#torch.sspaddmm) |
| [`Tensor.addmv`](generated/torch.Tensor.addmv.html#torch.Tensor.addmv) | See [`torch.addmv()`](generated/torch.addmv.html#torch.addmv) |
| [`Tensor.addmv_`](generated/torch.Tensor.addmv_.html#torch.Tensor.addmv_) | In-place version of [`addmv()`](generated/torch.Tensor.addmv.html#torch.Tensor.addmv) |
| [`Tensor.addr`](generated/torch.Tensor.addr.html#torch.Tensor.addr) | See [`torch.addr()`](generated/torch.addr.html#torch.addr) |
| [`Tensor.addr_`](generated/torch.Tensor.addr_.html#torch.Tensor.addr_) | In-place version of [`addr()`](generated/torch.Tensor.addr.html#torch.Tensor.addr) |
| [`Tensor.adjoint`](generated/torch.Tensor.adjoint.html#torch.Tensor.adjoint) | Alias for [`adjoint()`](generated/torch.adjoint.html#torch.adjoint) |
| [`Tensor.allclose`](generated/torch.Tensor.allclose.html#torch.Tensor.allclose) | See [`torch.allclose()`](generated/torch.allclose.html#torch.allclose) |
| [`Tensor.amax`](generated/torch.Tensor.amax.html#torch.Tensor.amax) | See [`torch.amax()`](generated/torch.amax.html#torch.amax) |
| [`Tensor.amin`](generated/torch.Tensor.amin.html#torch.Tensor.amin) | See [`torch.amin()`](generated/torch.amin.html#torch.amin) |
| [`Tensor.aminmax`](generated/torch.Tensor.aminmax.html#torch.Tensor.aminmax) | See [`torch.aminmax()`](generated/torch.aminmax.html#torch.aminmax) |
| [`Tensor.angle`](generated/torch.Tensor.angle.html#torch.Tensor.angle) | See [`torch.angle()`](generated/torch.angle.html#torch.angle) |
| [`Tensor.apply_`](generated/torch.Tensor.apply_.html#torch.Tensor.apply_) | Applies the function `callable` to each element in the tensor, replacing each element with the value returned by `callable`. |
| [`Tensor.argmax`](generated/torch.Tensor.argmax.html#torch.Tensor.argmax) | See [`torch.argmax()`](generated/torch.argmax.html#torch.argmax) |
| [`Tensor.argmin`](generated/torch.Tensor.argmin.html#torch.Tensor.argmin) | See [`torch.argmin()`](generated/torch.argmin.html#torch.argmin) |
| [`Tensor.argsort`](generated/torch.Tensor.argsort.html#torch.Tensor.argsort) | See [`torch.argsort()`](generated/torch.argsort.html#torch.argsort) |
| [`Tensor.argwhere`](generated/torch.Tensor.argwhere.html#torch.Tensor.argwhere) | See [`torch.argwhere()`](generated/torch.argwhere.html#torch.argwhere) |
| [`Tensor.asin`](generated/torch.Tensor.asin.html#torch.Tensor.asin) | See [`torch.asin()`](generated/torch.asin.html#torch.asin) |
| [`Tensor.asin_`](generated/torch.Tensor.asin_.html#torch.Tensor.asin_) | In-place version of [`asin()`](generated/torch.Tensor.asin.html#torch.Tensor.asin) |
| [`Tensor.arcsin`](generated/torch.Tensor.arcsin.html#torch.Tensor.arcsin) | See [`torch.arcsin()`](generated/torch.arcsin.html#torch.arcsin) |
| [`Tensor.arcsin_`](generated/torch.Tensor.arcsin_.html#torch.Tensor.arcsin_) | In-place version of [`arcsin()`](generated/torch.Tensor.arcsin.html#torch.Tensor.arcsin) |
| [`Tensor.as_strided`](generated/torch.Tensor.as_strided.html#torch.Tensor.as_strided) | See [`torch.as_strided()`](generated/torch.as_strided.html#torch.as_strided) |
| [`Tensor.atan`](generated/torch.Tensor.atan.html#torch.Tensor.atan) | See [`torch.atan()`](generated/torch.atan.html#torch.atan) |
| [`Tensor.atan_`](generated/torch.Tensor.atan_.html#torch.Tensor.atan_) | In-place version of [`atan()`](generated/torch.Tensor.atan.html#torch.Tensor.atan) |
| [`Tensor.arctan`](generated/torch.Tensor.arctan.html#torch.Tensor.arctan) | See [`torch.arctan()`](generated/torch.arctan.html#torch.arctan) |
| [`Tensor.arctan_`](generated/torch.Tensor.arctan_.html#torch.Tensor.arctan_) | In-place version of [`arctan()`](generated/torch.Tensor.arctan.html#torch.Tensor.arctan) |
| [`Tensor.atan2`](generated/torch.Tensor.atan2.html#torch.Tensor.atan2) | See [`torch.atan2()`](generated/torch.atan2.html#torch.atan2) |
| [`Tensor.atan2_`](generated/torch.Tensor.atan2_.html#torch.Tensor.atan2_) | In-place version of [`atan2()`](generated/torch.Tensor.atan2.html#torch.Tensor.atan2) |
| [`Tensor.arctan2`](generated/torch.Tensor.arctan2.html#torch.Tensor.arctan2) | See [`torch.arctan2()`](generated/torch.arctan2.html#torch.arctan2) |
| [`Tensor.arctan2_`](generated/torch.Tensor.arctan2_.html#torch.Tensor.arctan2_) | atan2_(other) -> Tensor |
| [`Tensor.all`](generated/torch.Tensor.all.html#torch.Tensor.all) | See [`torch.all()`](generated/torch.all.html#torch.all) |
| [`Tensor.any`](generated/torch.Tensor.any.html#torch.Tensor.any) | See [`torch.any()`](generated/torch.any.html#torch.any) |
| [`Tensor.backward`](generated/torch.Tensor.backward.html#torch.Tensor.backward) | Computes the gradient of current tensor wrt graph leaves. |
| [`Tensor.baddbmm`](generated/torch.Tensor.baddbmm.html#torch.Tensor.baddbmm) | See [`torch.baddbmm()`](generated/torch.baddbmm.html#torch.baddbmm) |
| [`Tensor.baddbmm_`](generated/torch.Tensor.baddbmm_.html#torch.Tensor.baddbmm_) | In-place version of [`baddbmm()`](generated/torch.Tensor.baddbmm.html#torch.Tensor.baddbmm) |
| [`Tensor.bernoulli`](generated/torch.Tensor.bernoulli.html#torch.Tensor.bernoulli) | Returns a result tensor where each result[i]\texttt{result[i]}result[i] is independently sampled from Bernoulli(self[i])\text{Bernoulli}(\texttt{self[i]})Bernoulli(self[i]). |
| [`Tensor.bernoulli_`](generated/torch.Tensor.bernoulli_.html#torch.Tensor.bernoulli_) | Fills each location of `self` with an independent sample from Bernoulli(p)\text{Bernoulli}(\texttt{p})Bernoulli(p). |
| [`Tensor.bfloat16`](generated/torch.Tensor.bfloat16.html#torch.Tensor.bfloat16) | `self.bfloat16()` is equivalent to `self.to(torch.bfloat16)`. |
| [`Tensor.bincount`](generated/torch.Tensor.bincount.html#torch.Tensor.bincount) | See [`torch.bincount()`](generated/torch.bincount.html#torch.bincount) |
| [`Tensor.bitwise_not`](generated/torch.Tensor.bitwise_not.html#torch.Tensor.bitwise_not) | See [`torch.bitwise_not()`](generated/torch.bitwise_not.html#torch.bitwise_not) |
| [`Tensor.bitwise_not_`](generated/torch.Tensor.bitwise_not_.html#torch.Tensor.bitwise_not_) | In-place version of [`bitwise_not()`](generated/torch.Tensor.bitwise_not.html#torch.Tensor.bitwise_not) |
| [`Tensor.bitwise_and`](generated/torch.Tensor.bitwise_and.html#torch.Tensor.bitwise_and) | See [`torch.bitwise_and()`](generated/torch.bitwise_and.html#torch.bitwise_and) |
| [`Tensor.bitwise_and_`](generated/torch.Tensor.bitwise_and_.html#torch.Tensor.bitwise_and_) | In-place version of [`bitwise_and()`](generated/torch.Tensor.bitwise_and.html#torch.Tensor.bitwise_and) |
| [`Tensor.bitwise_or`](generated/torch.Tensor.bitwise_or.html#torch.Tensor.bitwise_or) | See [`torch.bitwise_or()`](generated/torch.bitwise_or.html#torch.bitwise_or) |
| [`Tensor.bitwise_or_`](generated/torch.Tensor.bitwise_or_.html#torch.Tensor.bitwise_or_) | In-place version of [`bitwise_or()`](generated/torch.Tensor.bitwise_or.html#torch.Tensor.bitwise_or) |
| [`Tensor.bitwise_xor`](generated/torch.Tensor.bitwise_xor.html#torch.Tensor.bitwise_xor) | See [`torch.bitwise_xor()`](generated/torch.bitwise_xor.html#torch.bitwise_xor) |
| [`Tensor.bitwise_xor_`](generated/torch.Tensor.bitwise_xor_.html#torch.Tensor.bitwise_xor_) | In-place version of [`bitwise_xor()`](generated/torch.Tensor.bitwise_xor.html#torch.Tensor.bitwise_xor) |
| [`Tensor.bitwise_left_shift`](generated/torch.Tensor.bitwise_left_shift.html#torch.Tensor.bitwise_left_shift) | See [`torch.bitwise_left_shift()`](generated/torch.bitwise_left_shift.html#torch.bitwise_left_shift) |
| [`Tensor.bitwise_left_shift_`](generated/torch.Tensor.bitwise_left_shift_.html#torch.Tensor.bitwise_left_shift_) | In-place version of [`bitwise_left_shift()`](generated/torch.Tensor.bitwise_left_shift.html#torch.Tensor.bitwise_left_shift) |
| [`Tensor.bitwise_right_shift`](generated/torch.Tensor.bitwise_right_shift.html#torch.Tensor.bitwise_right_shift) | See [`torch.bitwise_right_shift()`](generated/torch.bitwise_right_shift.html#torch.bitwise_right_shift) |
| [`Tensor.bitwise_right_shift_`](generated/torch.Tensor.bitwise_right_shift_.html#torch.Tensor.bitwise_right_shift_) | In-place version of [`bitwise_right_shift()`](generated/torch.Tensor.bitwise_right_shift.html#torch.Tensor.bitwise_right_shift) |
| [`Tensor.bmm`](generated/torch.Tensor.bmm.html#torch.Tensor.bmm) | See [`torch.bmm()`](generated/torch.bmm.html#torch.bmm) |
| [`Tensor.bool`](generated/torch.Tensor.bool.html#torch.Tensor.bool) | `self.bool()` is equivalent to `self.to(torch.bool)`. |
| [`Tensor.byte`](generated/torch.Tensor.byte.html#torch.Tensor.byte) | `self.byte()` is equivalent to `self.to(torch.uint8)`. |
| [`Tensor.broadcast_to`](generated/torch.Tensor.broadcast_to.html#torch.Tensor.broadcast_to) | See [`torch.broadcast_to()`](generated/torch.broadcast_to.html#torch.broadcast_to). |
| [`Tensor.cauchy_`](generated/torch.Tensor.cauchy_.html#torch.Tensor.cauchy_) | Fills the tensor with numbers drawn from the Cauchy distribution: |
| [`Tensor.ceil`](generated/torch.Tensor.ceil.html#torch.Tensor.ceil) | See [`torch.ceil()`](generated/torch.ceil.html#torch.ceil) |
| [`Tensor.ceil_`](generated/torch.Tensor.ceil_.html#torch.Tensor.ceil_) | In-place version of [`ceil()`](generated/torch.Tensor.ceil.html#torch.Tensor.ceil) |
| [`Tensor.char`](generated/torch.Tensor.char.html#torch.Tensor.char) | `self.char()` is equivalent to `self.to(torch.int8)`. |
| [`Tensor.cholesky`](generated/torch.Tensor.cholesky.html#torch.Tensor.cholesky) | See [`torch.cholesky()`](generated/torch.cholesky.html#torch.cholesky) |
| [`Tensor.cholesky_inverse`](generated/torch.Tensor.cholesky_inverse.html#torch.Tensor.cholesky_inverse) | See [`torch.cholesky_inverse()`](generated/torch.cholesky_inverse.html#torch.cholesky_inverse) |
| [`Tensor.cholesky_solve`](generated/torch.Tensor.cholesky_solve.html#torch.Tensor.cholesky_solve) | See [`torch.cholesky_solve()`](generated/torch.cholesky_solve.html#torch.cholesky_solve) |
| [`Tensor.chunk`](generated/torch.Tensor.chunk.html#torch.Tensor.chunk) | See [`torch.chunk()`](generated/torch.chunk.html#torch.chunk) |
| [`Tensor.clamp`](generated/torch.Tensor.clamp.html#torch.Tensor.clamp) | See [`torch.clamp()`](generated/torch.clamp.html#torch.clamp) |
| [`Tensor.clamp_`](generated/torch.Tensor.clamp_.html#torch.Tensor.clamp_) | In-place version of [`clamp()`](generated/torch.Tensor.clamp.html#torch.Tensor.clamp) |
| [`Tensor.clip`](generated/torch.Tensor.clip.html#torch.Tensor.clip) | Alias for [`clamp()`](generated/torch.Tensor.clamp.html#torch.Tensor.clamp). |
| [`Tensor.clip_`](generated/torch.Tensor.clip_.html#torch.Tensor.clip_) | Alias for [`clamp_()`](generated/torch.Tensor.clamp_.html#torch.Tensor.clamp_). |
| [`Tensor.clone`](generated/torch.Tensor.clone.html#torch.Tensor.clone) | See [`torch.clone()`](generated/torch.clone.html#torch.clone) |
| [`Tensor.contiguous`](generated/torch.Tensor.contiguous.html#torch.Tensor.contiguous) | Returns a contiguous in memory tensor containing the same data as `self` tensor. |
| [`Tensor.copy_`](generated/torch.Tensor.copy_.html#torch.Tensor.copy_) | Copies the elements from `src` into `self` tensor and returns `self`. |
| [`Tensor.conj`](generated/torch.Tensor.conj.html#torch.Tensor.conj) | See [`torch.conj()`](generated/torch.conj.html#torch.conj) |
| [`Tensor.conj_physical`](generated/torch.Tensor.conj_physical.html#torch.Tensor.conj_physical) | See [`torch.conj_physical()`](generated/torch.conj_physical.html#torch.conj_physical) |
| [`Tensor.conj_physical_`](generated/torch.Tensor.conj_physical_.html#torch.Tensor.conj_physical_) | In-place version of [`conj_physical()`](generated/torch.Tensor.conj_physical.html#torch.Tensor.conj_physical) |
| [`Tensor.resolve_conj`](generated/torch.Tensor.resolve_conj.html#torch.Tensor.resolve_conj) | See [`torch.resolve_conj()`](generated/torch.resolve_conj.html#torch.resolve_conj) |
| [`Tensor.resolve_neg`](generated/torch.Tensor.resolve_neg.html#torch.Tensor.resolve_neg) | See [`torch.resolve_neg()`](generated/torch.resolve_neg.html#torch.resolve_neg) |
| [`Tensor.copysign`](generated/torch.Tensor.copysign.html#torch.Tensor.copysign) | See [`torch.copysign()`](generated/torch.copysign.html#torch.copysign) |
| [`Tensor.copysign_`](generated/torch.Tensor.copysign_.html#torch.Tensor.copysign_) | In-place version of [`copysign()`](generated/torch.Tensor.copysign.html#torch.Tensor.copysign) |
| [`Tensor.cos`](generated/torch.Tensor.cos.html#torch.Tensor.cos) | See [`torch.cos()`](generated/torch.cos.html#torch.cos) |
| [`Tensor.cos_`](generated/torch.Tensor.cos_.html#torch.Tensor.cos_) | In-place version of [`cos()`](generated/torch.Tensor.cos.html#torch.Tensor.cos) |
| [`Tensor.cosh`](generated/torch.Tensor.cosh.html#torch.Tensor.cosh) | See [`torch.cosh()`](generated/torch.cosh.html#torch.cosh) |
| [`Tensor.cosh_`](generated/torch.Tensor.cosh_.html#torch.Tensor.cosh_) | In-place version of [`cosh()`](generated/torch.Tensor.cosh.html#torch.Tensor.cosh) |
| [`Tensor.corrcoef`](generated/torch.Tensor.corrcoef.html#torch.Tensor.corrcoef) | See [`torch.corrcoef()`](generated/torch.corrcoef.html#torch.corrcoef) |
| [`Tensor.count_nonzero`](generated/torch.Tensor.count_nonzero.html#torch.Tensor.count_nonzero) | See [`torch.count_nonzero()`](generated/torch.count_nonzero.html#torch.count_nonzero) |
| [`Tensor.cov`](generated/torch.Tensor.cov.html#torch.Tensor.cov) | See [`torch.cov()`](generated/torch.cov.html#torch.cov) |
| [`Tensor.acosh`](generated/torch.Tensor.acosh.html#torch.Tensor.acosh) | See [`torch.acosh()`](generated/torch.acosh.html#torch.acosh) |
| [`Tensor.acosh_`](generated/torch.Tensor.acosh_.html#torch.Tensor.acosh_) | In-place version of [`acosh()`](generated/torch.Tensor.acosh.html#torch.Tensor.acosh) |
| [`Tensor.arccosh`](generated/torch.Tensor.arccosh.html#torch.Tensor.arccosh) | acosh() -> Tensor |
| [`Tensor.arccosh_`](generated/torch.Tensor.arccosh_.html#torch.Tensor.arccosh_) | acosh_() -> Tensor |
| [`Tensor.cpu`](generated/torch.Tensor.cpu.html#torch.Tensor.cpu) | Returns a copy of this object in CPU memory. |
| [`Tensor.cross`](generated/torch.Tensor.cross.html#torch.Tensor.cross) | See [`torch.cross()`](generated/torch.cross.html#torch.cross) |
| [`Tensor.cuda`](generated/torch.Tensor.cuda.html#torch.Tensor.cuda) | Returns a copy of this object in CUDA memory. |
| [`Tensor.logcumsumexp`](generated/torch.Tensor.logcumsumexp.html#torch.Tensor.logcumsumexp) | See [`torch.logcumsumexp()`](generated/torch.logcumsumexp.html#torch.logcumsumexp) |
| [`Tensor.cummax`](generated/torch.Tensor.cummax.html#torch.Tensor.cummax) | See [`torch.cummax()`](generated/torch.cummax.html#torch.cummax) |
| [`Tensor.cummin`](generated/torch.Tensor.cummin.html#torch.Tensor.cummin) | See [`torch.cummin()`](generated/torch.cummin.html#torch.cummin) |
| [`Tensor.cumprod`](generated/torch.Tensor.cumprod.html#torch.Tensor.cumprod) | See [`torch.cumprod()`](generated/torch.cumprod.html#torch.cumprod) |
| [`Tensor.cumprod_`](generated/torch.Tensor.cumprod_.html#torch.Tensor.cumprod_) | In-place version of [`cumprod()`](generated/torch.Tensor.cumprod.html#torch.Tensor.cumprod) |
| [`Tensor.cumsum`](generated/torch.Tensor.cumsum.html#torch.Tensor.cumsum) | See [`torch.cumsum()`](generated/torch.cumsum.html#torch.cumsum) |
| [`Tensor.cumsum_`](generated/torch.Tensor.cumsum_.html#torch.Tensor.cumsum_) | In-place version of [`cumsum()`](generated/torch.Tensor.cumsum.html#torch.Tensor.cumsum) |
| [`Tensor.chalf`](generated/torch.Tensor.chalf.html#torch.Tensor.chalf) | `self.chalf()` is equivalent to `self.to(torch.complex32)`. |
| [`Tensor.cfloat`](generated/torch.Tensor.cfloat.html#torch.Tensor.cfloat) | `self.cfloat()` is equivalent to `self.to(torch.complex64)`. |
| [`Tensor.cdouble`](generated/torch.Tensor.cdouble.html#torch.Tensor.cdouble) | `self.cdouble()` is equivalent to `self.to(torch.complex128)`. |
| [`Tensor.const_data_ptr`](generated/torch.Tensor.const_data_ptr.html#torch.Tensor.const_data_ptr) | Returns the address of the first element of `self` tensor. |
| [`Tensor.data_ptr`](generated/torch.Tensor.data_ptr.html#torch.Tensor.data_ptr) | Returns the address of the first element of `self` tensor. |
| [`Tensor.deg2rad`](generated/torch.Tensor.deg2rad.html#torch.Tensor.deg2rad) | See [`torch.deg2rad()`](generated/torch.deg2rad.html#torch.deg2rad) |
| [`Tensor.dequantize`](generated/torch.Tensor.dequantize.html#torch.Tensor.dequantize) | Given a quantized Tensor, dequantize it and return the dequantized float Tensor. |
| [`Tensor.det`](generated/torch.Tensor.det.html#torch.Tensor.det) | See [`torch.det()`](generated/torch.det.html#torch.det) |
| [`Tensor.dense_dim`](generated/torch.Tensor.dense_dim.html#torch.Tensor.dense_dim) | Return the number of dense dimensions in a [sparse tensor](sparse.html#sparse-docs) `self`. |
| [`Tensor.detach`](generated/torch.Tensor.detach.html#torch.Tensor.detach) | Returns a new Tensor, detached from the current graph. |
| [`Tensor.detach_`](generated/torch.Tensor.detach_.html#torch.Tensor.detach_) | Detaches the Tensor from the graph that created it, making it a leaf. |
| [`Tensor.diag`](generated/torch.Tensor.diag.html#torch.Tensor.diag) | See [`torch.diag()`](generated/torch.diag.html#torch.diag) |
| [`Tensor.diag_embed`](generated/torch.Tensor.diag_embed.html#torch.Tensor.diag_embed) | See [`torch.diag_embed()`](generated/torch.diag_embed.html#torch.diag_embed) |
| [`Tensor.diagflat`](generated/torch.Tensor.diagflat.html#torch.Tensor.diagflat) | See [`torch.diagflat()`](generated/torch.diagflat.html#torch.diagflat) |
| [`Tensor.diagonal`](generated/torch.Tensor.diagonal.html#torch.Tensor.diagonal) | See [`torch.diagonal()`](generated/torch.diagonal.html#torch.diagonal) |
| [`Tensor.diagonal_scatter`](generated/torch.Tensor.diagonal_scatter.html#torch.Tensor.diagonal_scatter) | See [`torch.diagonal_scatter()`](generated/torch.diagonal_scatter.html#torch.diagonal_scatter) |
| [`Tensor.fill_diagonal_`](generated/torch.Tensor.fill_diagonal_.html#torch.Tensor.fill_diagonal_) | Fill the main diagonal of a tensor that has at least 2-dimensions. |
| [`Tensor.fmax`](generated/torch.Tensor.fmax.html#torch.Tensor.fmax) | See [`torch.fmax()`](generated/torch.fmax.html#torch.fmax) |
| [`Tensor.fmin`](generated/torch.Tensor.fmin.html#torch.Tensor.fmin) | See [`torch.fmin()`](generated/torch.fmin.html#torch.fmin) |
| [`Tensor.diff`](generated/torch.Tensor.diff.html#torch.Tensor.diff) | See [`torch.diff()`](generated/torch.diff.html#torch.diff) |
| [`Tensor.digamma`](generated/torch.Tensor.digamma.html#torch.Tensor.digamma) | See [`torch.digamma()`](generated/torch.digamma.html#torch.digamma) |
| [`Tensor.digamma_`](generated/torch.Tensor.digamma_.html#torch.Tensor.digamma_) | In-place version of [`digamma()`](generated/torch.Tensor.digamma.html#torch.Tensor.digamma) |
| [`Tensor.dim`](generated/torch.Tensor.dim.html#torch.Tensor.dim) | Returns the number of dimensions of `self` tensor. |
| [`Tensor.dim_order`](generated/torch.Tensor.dim_order.html#torch.Tensor.dim_order) | Returns the uniquely determined tuple of int describing the dim order or physical layout of `self`. |
| [`Tensor.dist`](generated/torch.Tensor.dist.html#torch.Tensor.dist) | See [`torch.dist()`](generated/torch.dist.html#torch.dist) |
| [`Tensor.div`](generated/torch.Tensor.div.html#torch.Tensor.div) | See [`torch.div()`](generated/torch.div.html#torch.div) |
| [`Tensor.div_`](generated/torch.Tensor.div_.html#torch.Tensor.div_) | In-place version of [`div()`](generated/torch.Tensor.div.html#torch.Tensor.div) |
| [`Tensor.divide`](generated/torch.Tensor.divide.html#torch.Tensor.divide) | See [`torch.divide()`](generated/torch.divide.html#torch.divide) |
| [`Tensor.divide_`](generated/torch.Tensor.divide_.html#torch.Tensor.divide_) | In-place version of [`divide()`](generated/torch.Tensor.divide.html#torch.Tensor.divide) |
| [`Tensor.dot`](generated/torch.Tensor.dot.html#torch.Tensor.dot) | See [`torch.dot()`](generated/torch.dot.html#torch.dot) |
| [`Tensor.double`](generated/torch.Tensor.double.html#torch.Tensor.double) | `self.double()` is equivalent to `self.to(torch.float64)`. |
| [`Tensor.dsplit`](generated/torch.Tensor.dsplit.html#torch.Tensor.dsplit) | See [`torch.dsplit()`](generated/torch.dsplit.html#torch.dsplit) |
| [`Tensor.element_size`](generated/torch.Tensor.element_size.html#torch.Tensor.element_size) | Returns the size in bytes of an individual element. |
| [`Tensor.eq`](generated/torch.Tensor.eq.html#torch.Tensor.eq) | See [`torch.eq()`](generated/torch.eq.html#torch.eq) |
| [`Tensor.eq_`](generated/torch.Tensor.eq_.html#torch.Tensor.eq_) | In-place version of [`eq()`](generated/torch.Tensor.eq.html#torch.Tensor.eq) |
| [`Tensor.equal`](generated/torch.Tensor.equal.html#torch.Tensor.equal) | See [`torch.equal()`](generated/torch.equal.html#torch.equal) |
| [`Tensor.erf`](generated/torch.Tensor.erf.html#torch.Tensor.erf) | See [`torch.erf()`](generated/torch.erf.html#torch.erf) |
| [`Tensor.erf_`](generated/torch.Tensor.erf_.html#torch.Tensor.erf_) | In-place version of [`erf()`](generated/torch.Tensor.erf.html#torch.Tensor.erf) |
| [`Tensor.erfc`](generated/torch.Tensor.erfc.html#torch.Tensor.erfc) | See [`torch.erfc()`](generated/torch.erfc.html#torch.erfc) |
| [`Tensor.erfc_`](generated/torch.Tensor.erfc_.html#torch.Tensor.erfc_) | In-place version of [`erfc()`](generated/torch.Tensor.erfc.html#torch.Tensor.erfc) |
| [`Tensor.erfinv`](generated/torch.Tensor.erfinv.html#torch.Tensor.erfinv) | See [`torch.erfinv()`](generated/torch.erfinv.html#torch.erfinv) |
| [`Tensor.erfinv_`](generated/torch.Tensor.erfinv_.html#torch.Tensor.erfinv_) | In-place version of [`erfinv()`](generated/torch.Tensor.erfinv.html#torch.Tensor.erfinv) |
| [`Tensor.exp`](generated/torch.Tensor.exp.html#torch.Tensor.exp) | See [`torch.exp()`](generated/torch.exp.html#torch.exp) |
| [`Tensor.exp_`](generated/torch.Tensor.exp_.html#torch.Tensor.exp_) | In-place version of [`exp()`](generated/torch.Tensor.exp.html#torch.Tensor.exp) |
| [`Tensor.expm1`](generated/torch.Tensor.expm1.html#torch.Tensor.expm1) | See [`torch.expm1()`](generated/torch.expm1.html#torch.expm1) |
| [`Tensor.expm1_`](generated/torch.Tensor.expm1_.html#torch.Tensor.expm1_) | In-place version of [`expm1()`](generated/torch.Tensor.expm1.html#torch.Tensor.expm1) |
| [`Tensor.expand`](generated/torch.Tensor.expand.html#torch.Tensor.expand) | Returns a new view of the `self` tensor with singleton dimensions expanded to a larger size. |
| [`Tensor.expand_as`](generated/torch.Tensor.expand_as.html#torch.Tensor.expand_as) | Expand this tensor to the same size as `other`. |
| [`Tensor.exponential_`](generated/torch.Tensor.exponential_.html#torch.Tensor.exponential_) | Fills `self` tensor with elements drawn from the PDF (probability density function): |
| [`Tensor.fix`](generated/torch.Tensor.fix.html#torch.Tensor.fix) | See [`torch.fix()`](generated/torch.fix.html#torch.fix). |
| [`Tensor.fix_`](generated/torch.Tensor.fix_.html#torch.Tensor.fix_) | In-place version of [`fix()`](generated/torch.Tensor.fix.html#torch.Tensor.fix) |
| [`Tensor.fill_`](generated/torch.Tensor.fill_.html#torch.Tensor.fill_) | Fills `self` tensor with the specified value. |
| [`Tensor.flatten`](generated/torch.Tensor.flatten.html#torch.Tensor.flatten) | See [`torch.flatten()`](generated/torch.flatten.html#torch.flatten) |
| [`Tensor.flip`](generated/torch.Tensor.flip.html#torch.Tensor.flip) | See [`torch.flip()`](generated/torch.flip.html#torch.flip) |
| [`Tensor.fliplr`](generated/torch.Tensor.fliplr.html#torch.Tensor.fliplr) | See [`torch.fliplr()`](generated/torch.fliplr.html#torch.fliplr) |
| [`Tensor.flipud`](generated/torch.Tensor.flipud.html#torch.Tensor.flipud) | See [`torch.flipud()`](generated/torch.flipud.html#torch.flipud) |
| [`Tensor.float`](generated/torch.Tensor.float.html#torch.Tensor.float) | `self.float()` is equivalent to `self.to(torch.float32)`. |
| [`Tensor.float_power`](generated/torch.Tensor.float_power.html#torch.Tensor.float_power) | See [`torch.float_power()`](generated/torch.float_power.html#torch.float_power) |
| [`Tensor.float_power_`](generated/torch.Tensor.float_power_.html#torch.Tensor.float_power_) | In-place version of [`float_power()`](generated/torch.Tensor.float_power.html#torch.Tensor.float_power) |
| [`Tensor.floor`](generated/torch.Tensor.floor.html#torch.Tensor.floor) | See [`torch.floor()`](generated/torch.floor.html#torch.floor) |
| [`Tensor.floor_`](generated/torch.Tensor.floor_.html#torch.Tensor.floor_) | In-place version of [`floor()`](generated/torch.Tensor.floor.html#torch.Tensor.floor) |
| [`Tensor.floor_divide`](generated/torch.Tensor.floor_divide.html#torch.Tensor.floor_divide) | See [`torch.floor_divide()`](generated/torch.floor_divide.html#torch.floor_divide) |
| [`Tensor.floor_divide_`](generated/torch.Tensor.floor_divide_.html#torch.Tensor.floor_divide_) | In-place version of [`floor_divide()`](generated/torch.Tensor.floor_divide.html#torch.Tensor.floor_divide) |
| [`Tensor.fmod`](generated/torch.Tensor.fmod.html#torch.Tensor.fmod) | See [`torch.fmod()`](generated/torch.fmod.html#torch.fmod) |
| [`Tensor.fmod_`](generated/torch.Tensor.fmod_.html#torch.Tensor.fmod_) | In-place version of [`fmod()`](generated/torch.Tensor.fmod.html#torch.Tensor.fmod) |
| [`Tensor.frac`](generated/torch.Tensor.frac.html#torch.Tensor.frac) | See [`torch.frac()`](generated/torch.frac.html#torch.frac) |
| [`Tensor.frac_`](generated/torch.Tensor.frac_.html#torch.Tensor.frac_) | In-place version of [`frac()`](generated/torch.Tensor.frac.html#torch.Tensor.frac) |
| [`Tensor.frexp`](generated/torch.Tensor.frexp.html#torch.Tensor.frexp) | See [`torch.frexp()`](generated/torch.frexp.html#torch.frexp) |
| [`Tensor.gather`](generated/torch.Tensor.gather.html#torch.Tensor.gather) | See [`torch.gather()`](generated/torch.gather.html#torch.gather) |
| [`Tensor.gcd`](generated/torch.Tensor.gcd.html#torch.Tensor.gcd) | See [`torch.gcd()`](generated/torch.gcd.html#torch.gcd) |
| [`Tensor.gcd_`](generated/torch.Tensor.gcd_.html#torch.Tensor.gcd_) | In-place version of [`gcd()`](generated/torch.Tensor.gcd.html#torch.Tensor.gcd) |
| [`Tensor.ge`](generated/torch.Tensor.ge.html#torch.Tensor.ge) | See [`torch.ge()`](generated/torch.ge.html#torch.ge). |
| [`Tensor.ge_`](generated/torch.Tensor.ge_.html#torch.Tensor.ge_) | In-place version of [`ge()`](generated/torch.Tensor.ge.html#torch.Tensor.ge). |
| [`Tensor.greater_equal`](generated/torch.Tensor.greater_equal.html#torch.Tensor.greater_equal) | See [`torch.greater_equal()`](generated/torch.greater_equal.html#torch.greater_equal). |
| [`Tensor.greater_equal_`](generated/torch.Tensor.greater_equal_.html#torch.Tensor.greater_equal_) | In-place version of [`greater_equal()`](generated/torch.Tensor.greater_equal.html#torch.Tensor.greater_equal). |
| [`Tensor.geometric_`](generated/torch.Tensor.geometric_.html#torch.Tensor.geometric_) | Fills `self` tensor with elements drawn from the geometric distribution: |
| [`Tensor.geqrf`](generated/torch.Tensor.geqrf.html#torch.Tensor.geqrf) | See [`torch.geqrf()`](generated/torch.geqrf.html#torch.geqrf) |
| [`Tensor.ger`](generated/torch.Tensor.ger.html#torch.Tensor.ger) | See [`torch.ger()`](generated/torch.ger.html#torch.ger) |
| [`Tensor.get_device`](generated/torch.Tensor.get_device.html#torch.Tensor.get_device) | For CUDA tensors, this function returns the device ordinal of the GPU on which the tensor resides. |
| [`Tensor.gt`](generated/torch.Tensor.gt.html#torch.Tensor.gt) | See [`torch.gt()`](generated/torch.gt.html#torch.gt). |
| [`Tensor.gt_`](generated/torch.Tensor.gt_.html#torch.Tensor.gt_) | In-place version of [`gt()`](generated/torch.Tensor.gt.html#torch.Tensor.gt). |
| [`Tensor.greater`](generated/torch.Tensor.greater.html#torch.Tensor.greater) | See [`torch.greater()`](generated/torch.greater.html#torch.greater). |
| [`Tensor.greater_`](generated/torch.Tensor.greater_.html#torch.Tensor.greater_) | In-place version of [`greater()`](generated/torch.Tensor.greater.html#torch.Tensor.greater). |
| [`Tensor.half`](generated/torch.Tensor.half.html#torch.Tensor.half) | `self.half()` is equivalent to `self.to(torch.float16)`. |
| [`Tensor.hardshrink`](generated/torch.Tensor.hardshrink.html#torch.Tensor.hardshrink) | See [`torch.nn.functional.hardshrink()`](generated/torch.nn.functional.hardshrink.html#torch.nn.functional.hardshrink) |
| [`Tensor.heaviside`](generated/torch.Tensor.heaviside.html#torch.Tensor.heaviside) | See [`torch.heaviside()`](generated/torch.heaviside.html#torch.heaviside) |
| [`Tensor.histc`](generated/torch.Tensor.histc.html#torch.Tensor.histc) | See [`torch.histc()`](generated/torch.histc.html#torch.histc) |
| [`Tensor.histogram`](generated/torch.Tensor.histogram.html#torch.Tensor.histogram) | See [`torch.histogram()`](generated/torch.histogram.html#torch.histogram) |
| [`Tensor.hsplit`](generated/torch.Tensor.hsplit.html#torch.Tensor.hsplit) | See [`torch.hsplit()`](generated/torch.hsplit.html#torch.hsplit) |
| [`Tensor.hypot`](generated/torch.Tensor.hypot.html#torch.Tensor.hypot) | See [`torch.hypot()`](generated/torch.hypot.html#torch.hypot) |
| [`Tensor.hypot_`](generated/torch.Tensor.hypot_.html#torch.Tensor.hypot_) | In-place version of [`hypot()`](generated/torch.Tensor.hypot.html#torch.Tensor.hypot) |
| [`Tensor.i0`](generated/torch.Tensor.i0.html#torch.Tensor.i0) | See [`torch.i0()`](generated/torch.i0.html#torch.i0) |
| [`Tensor.i0_`](generated/torch.Tensor.i0_.html#torch.Tensor.i0_) | In-place version of [`i0()`](generated/torch.Tensor.i0.html#torch.Tensor.i0) |
| [`Tensor.igamma`](generated/torch.Tensor.igamma.html#torch.Tensor.igamma) | See [`torch.igamma()`](generated/torch.igamma.html#torch.igamma) |
| [`Tensor.igamma_`](generated/torch.Tensor.igamma_.html#torch.Tensor.igamma_) | In-place version of [`igamma()`](generated/torch.Tensor.igamma.html#torch.Tensor.igamma) |
| [`Tensor.igammac`](generated/torch.Tensor.igammac.html#torch.Tensor.igammac) | See [`torch.igammac()`](generated/torch.igammac.html#torch.igammac) |
| [`Tensor.igammac_`](generated/torch.Tensor.igammac_.html#torch.Tensor.igammac_) | In-place version of [`igammac()`](generated/torch.Tensor.igammac.html#torch.Tensor.igammac) |
| [`Tensor.index_add_`](generated/torch.Tensor.index_add_.html#torch.Tensor.index_add_) | Accumulate the elements of `alpha` times `source` into the `self` tensor by adding to the indices in the order given in `index`. |
| [`Tensor.index_add`](generated/torch.Tensor.index_add.html#torch.Tensor.index_add) | Out-of-place version of [`torch.Tensor.index_add_()`](generated/torch.Tensor.index_add_.html#torch.Tensor.index_add_). |
| [`Tensor.index_copy_`](generated/torch.Tensor.index_copy_.html#torch.Tensor.index_copy_) | Copies the elements of [`tensor`](generated/torch.tensor.html#torch.tensor) into the `self` tensor by selecting the indices in the order given in `index`. |
| [`Tensor.index_copy`](generated/torch.Tensor.index_copy.html#torch.Tensor.index_copy) | Out-of-place version of [`torch.Tensor.index_copy_()`](generated/torch.Tensor.index_copy_.html#torch.Tensor.index_copy_). |
| [`Tensor.index_fill_`](generated/torch.Tensor.index_fill_.html#torch.Tensor.index_fill_) | Fills the elements of the `self` tensor with value `value` by selecting the indices in the order given in `index`. |
| [`Tensor.index_fill`](generated/torch.Tensor.index_fill.html#torch.Tensor.index_fill) | Out-of-place version of [`torch.Tensor.index_fill_()`](generated/torch.Tensor.index_fill_.html#torch.Tensor.index_fill_). |
| [`Tensor.index_put_`](generated/torch.Tensor.index_put_.html#torch.Tensor.index_put_) | Puts values from the tensor `values` into the tensor `self` using the indices specified in `indices` (which is a tuple of Tensors). |
| [`Tensor.index_put`](generated/torch.Tensor.index_put.html#torch.Tensor.index_put) | Out-place version of [`index_put_()`](generated/torch.Tensor.index_put_.html#torch.Tensor.index_put_). |
| [`Tensor.index_reduce_`](generated/torch.Tensor.index_reduce_.html#torch.Tensor.index_reduce_) | Accumulate the elements of `source` into the `self` tensor by accumulating to the indices in the order given in `index` using the reduction given by the `reduce` argument. |
| [`Tensor.index_reduce`](generated/torch.Tensor.index_reduce.html#torch.Tensor.index_reduce) | |
| [`Tensor.index_select`](generated/torch.Tensor.index_select.html#torch.Tensor.index_select) | See [`torch.index_select()`](generated/torch.index_select.html#torch.index_select) |
| [`Tensor.indices`](generated/torch.Tensor.indices.html#torch.Tensor.indices) | Return the indices tensor of a [sparse COO tensor](sparse.html#sparse-coo-docs). |
| [`Tensor.inner`](generated/torch.Tensor.inner.html#torch.Tensor.inner) | See [`torch.inner()`](generated/torch.inner.html#torch.inner). |
| [`Tensor.int`](generated/torch.Tensor.int.html#torch.Tensor.int) | `self.int()` is equivalent to `self.to(torch.int32)`. |
| [`Tensor.int_repr`](generated/torch.Tensor.int_repr.html#torch.Tensor.int_repr) | Given a quantized Tensor, `self.int_repr()` returns a CPU Tensor with uint8_t as data type that stores the underlying uint8_t values of the given Tensor. |
| [`Tensor.inverse`](generated/torch.Tensor.inverse.html#torch.Tensor.inverse) | See [`torch.inverse()`](generated/torch.inverse.html#torch.inverse) |
| [`Tensor.isclose`](generated/torch.Tensor.isclose.html#torch.Tensor.isclose) | See [`torch.isclose()`](generated/torch.isclose.html#torch.isclose) |
| [`Tensor.isfinite`](generated/torch.Tensor.isfinite.html#torch.Tensor.isfinite) | See [`torch.isfinite()`](generated/torch.isfinite.html#torch.isfinite) |
| [`Tensor.isinf`](generated/torch.Tensor.isinf.html#torch.Tensor.isinf) | See [`torch.isinf()`](generated/torch.isinf.html#torch.isinf) |
| [`Tensor.isposinf`](generated/torch.Tensor.isposinf.html#torch.Tensor.isposinf) | See [`torch.isposinf()`](generated/torch.isposinf.html#torch.isposinf) |
| [`Tensor.isneginf`](generated/torch.Tensor.isneginf.html#torch.Tensor.isneginf) | See [`torch.isneginf()`](generated/torch.isneginf.html#torch.isneginf) |
| [`Tensor.isnan`](generated/torch.Tensor.isnan.html#torch.Tensor.isnan) | See [`torch.isnan()`](generated/torch.isnan.html#torch.isnan) |
| [`Tensor.is_contiguous`](generated/torch.Tensor.is_contiguous.html#torch.Tensor.is_contiguous) | Returns True if `self` tensor is contiguous in memory in the order specified by memory format. |
| [`Tensor.is_complex`](generated/torch.Tensor.is_complex.html#torch.Tensor.is_complex) | Returns True if the data type of `self` is a complex data type. |
| [`Tensor.is_conj`](generated/torch.Tensor.is_conj.html#torch.Tensor.is_conj) | Returns True if the conjugate bit of `self` is set to true. |
| [`Tensor.is_floating_point`](generated/torch.Tensor.is_floating_point.html#torch.Tensor.is_floating_point) | Returns True if the data type of `self` is a floating point data type. |
| [`Tensor.is_inference`](generated/torch.Tensor.is_inference.html#torch.Tensor.is_inference) | See [`torch.is_inference()`](generated/torch.is_inference.html#torch.is_inference) |
| [`Tensor.is_leaf`](generated/torch.Tensor.is_leaf.html#torch.Tensor.is_leaf) | All Tensors that have `requires_grad` which is `False` will be leaf Tensors by convention. |
| [`Tensor.is_pinned`](generated/torch.Tensor.is_pinned.html#torch.Tensor.is_pinned) | Returns true if this tensor resides in pinned memory. |
| [`Tensor.is_set_to`](generated/torch.Tensor.is_set_to.html#torch.Tensor.is_set_to) | Returns True if both tensors are pointing to the exact same memory (same storage, offset, size and stride). |
| [`Tensor.is_shared`](generated/torch.Tensor.is_shared.html#torch.Tensor.is_shared) | Checks if tensor is in shared memory. |
| [`Tensor.is_signed`](generated/torch.Tensor.is_signed.html#torch.Tensor.is_signed) | Returns True if the data type of `self` is a signed data type. |
| [`Tensor.is_sparse`](generated/torch.Tensor.is_sparse.html#torch.Tensor.is_sparse) | Is `True` if the Tensor uses sparse COO storage layout, `False` otherwise. |
| [`Tensor.istft`](generated/torch.Tensor.istft.html#torch.Tensor.istft) | See [`torch.istft()`](generated/torch.istft.html#torch.istft) |
| [`Tensor.isreal`](generated/torch.Tensor.isreal.html#torch.Tensor.isreal) | See [`torch.isreal()`](generated/torch.isreal.html#torch.isreal) |
| [`Tensor.item`](generated/torch.Tensor.item.html#torch.Tensor.item) | Returns the value of this tensor as a standard Python number. |
| [`Tensor.kthvalue`](generated/torch.Tensor.kthvalue.html#torch.Tensor.kthvalue) | See [`torch.kthvalue()`](generated/torch.kthvalue.html#torch.kthvalue) |
| [`Tensor.lcm`](generated/torch.Tensor.lcm.html#torch.Tensor.lcm) | See [`torch.lcm()`](generated/torch.lcm.html#torch.lcm) |
| [`Tensor.lcm_`](generated/torch.Tensor.lcm_.html#torch.Tensor.lcm_) | In-place version of [`lcm()`](generated/torch.Tensor.lcm.html#torch.Tensor.lcm) |
| [`Tensor.ldexp`](generated/torch.Tensor.ldexp.html#torch.Tensor.ldexp) | See [`torch.ldexp()`](generated/torch.ldexp.html#torch.ldexp) |
| [`Tensor.ldexp_`](generated/torch.Tensor.ldexp_.html#torch.Tensor.ldexp_) | In-place version of [`ldexp()`](generated/torch.Tensor.ldexp.html#torch.Tensor.ldexp) |
| [`Tensor.le`](generated/torch.Tensor.le.html#torch.Tensor.le) | See [`torch.le()`](generated/torch.le.html#torch.le). |
| [`Tensor.le_`](generated/torch.Tensor.le_.html#torch.Tensor.le_) | In-place version of [`le()`](generated/torch.Tensor.le.html#torch.Tensor.le). |
| [`Tensor.less_equal`](generated/torch.Tensor.less_equal.html#torch.Tensor.less_equal) | See [`torch.less_equal()`](generated/torch.less_equal.html#torch.less_equal). |
| [`Tensor.less_equal_`](generated/torch.Tensor.less_equal_.html#torch.Tensor.less_equal_) | In-place version of [`less_equal()`](generated/torch.Tensor.less_equal.html#torch.Tensor.less_equal). |
| [`Tensor.lerp`](generated/torch.Tensor.lerp.html#torch.Tensor.lerp) | See [`torch.lerp()`](generated/torch.lerp.html#torch.lerp) |
| [`Tensor.lerp_`](generated/torch.Tensor.lerp_.html#torch.Tensor.lerp_) | In-place version of [`lerp()`](generated/torch.Tensor.lerp.html#torch.Tensor.lerp) |
| [`Tensor.lgamma`](generated/torch.Tensor.lgamma.html#torch.Tensor.lgamma) | See [`torch.lgamma()`](generated/torch.lgamma.html#torch.lgamma) |
| [`Tensor.lgamma_`](generated/torch.Tensor.lgamma_.html#torch.Tensor.lgamma_) | In-place version of [`lgamma()`](generated/torch.Tensor.lgamma.html#torch.Tensor.lgamma) |
| [`Tensor.log`](generated/torch.Tensor.log.html#torch.Tensor.log) | See [`torch.log()`](generated/torch.log.html#torch.log) |
| [`Tensor.log_`](generated/torch.Tensor.log_.html#torch.Tensor.log_) | In-place version of [`log()`](generated/torch.Tensor.log.html#torch.Tensor.log) |
| [`Tensor.logdet`](generated/torch.Tensor.logdet.html#torch.Tensor.logdet) | See [`torch.logdet()`](generated/torch.logdet.html#torch.logdet) |
| [`Tensor.log10`](generated/torch.Tensor.log10.html#torch.Tensor.log10) | See [`torch.log10()`](generated/torch.log10.html#torch.log10) |
| [`Tensor.log10_`](generated/torch.Tensor.log10_.html#torch.Tensor.log10_) | In-place version of [`log10()`](generated/torch.Tensor.log10.html#torch.Tensor.log10) |
| [`Tensor.log1p`](generated/torch.Tensor.log1p.html#torch.Tensor.log1p) | See [`torch.log1p()`](generated/torch.log1p.html#torch.log1p) |
| [`Tensor.log1p_`](generated/torch.Tensor.log1p_.html#torch.Tensor.log1p_) | In-place version of [`log1p()`](generated/torch.Tensor.log1p.html#torch.Tensor.log1p) |
| [`Tensor.log2`](generated/torch.Tensor.log2.html#torch.Tensor.log2) | See [`torch.log2()`](generated/torch.log2.html#torch.log2) |
| [`Tensor.log2_`](generated/torch.Tensor.log2_.html#torch.Tensor.log2_) | In-place version of [`log2()`](generated/torch.Tensor.log2.html#torch.Tensor.log2) |
| [`Tensor.log_normal_`](generated/torch.Tensor.log_normal_.html#torch.Tensor.log_normal_) | Fills `self` tensor with numbers samples from the log-normal distribution parameterized by the given mean μ\muμ and standard deviation σ\sigmaσ. |
| [`Tensor.logaddexp`](generated/torch.Tensor.logaddexp.html#torch.Tensor.logaddexp) | See [`torch.logaddexp()`](generated/torch.logaddexp.html#torch.logaddexp) |
| [`Tensor.logaddexp2`](generated/torch.Tensor.logaddexp2.html#torch.Tensor.logaddexp2) | See [`torch.logaddexp2()`](generated/torch.logaddexp2.html#torch.logaddexp2) |
| [`Tensor.logsumexp`](generated/torch.Tensor.logsumexp.html#torch.Tensor.logsumexp) | See [`torch.logsumexp()`](generated/torch.logsumexp.html#torch.logsumexp) |
| [`Tensor.logical_and`](generated/torch.Tensor.logical_and.html#torch.Tensor.logical_and) | See [`torch.logical_and()`](generated/torch.logical_and.html#torch.logical_and) |
| [`Tensor.logical_and_`](generated/torch.Tensor.logical_and_.html#torch.Tensor.logical_and_) | In-place version of [`logical_and()`](generated/torch.Tensor.logical_and.html#torch.Tensor.logical_and) |
| [`Tensor.logical_not`](generated/torch.Tensor.logical_not.html#torch.Tensor.logical_not) | See [`torch.logical_not()`](generated/torch.logical_not.html#torch.logical_not) |
| [`Tensor.logical_not_`](generated/torch.Tensor.logical_not_.html#torch.Tensor.logical_not_) | In-place version of [`logical_not()`](generated/torch.Tensor.logical_not.html#torch.Tensor.logical_not) |
| [`Tensor.logical_or`](generated/torch.Tensor.logical_or.html#torch.Tensor.logical_or) | See [`torch.logical_or()`](generated/torch.logical_or.html#torch.logical_or) |
| [`Tensor.logical_or_`](generated/torch.Tensor.logical_or_.html#torch.Tensor.logical_or_) | In-place version of [`logical_or()`](generated/torch.Tensor.logical_or.html#torch.Tensor.logical_or) |
| [`Tensor.logical_xor`](generated/torch.Tensor.logical_xor.html#torch.Tensor.logical_xor) | See [`torch.logical_xor()`](generated/torch.logical_xor.html#torch.logical_xor) |
| [`Tensor.logical_xor_`](generated/torch.Tensor.logical_xor_.html#torch.Tensor.logical_xor_) | In-place version of [`logical_xor()`](generated/torch.Tensor.logical_xor.html#torch.Tensor.logical_xor) |
| [`Tensor.logit`](generated/torch.Tensor.logit.html#torch.Tensor.logit) | See [`torch.logit()`](generated/torch.logit.html#torch.logit) |
| [`Tensor.logit_`](generated/torch.Tensor.logit_.html#torch.Tensor.logit_) | In-place version of [`logit()`](generated/torch.Tensor.logit.html#torch.Tensor.logit) |
| [`Tensor.long`](generated/torch.Tensor.long.html#torch.Tensor.long) | `self.long()` is equivalent to `self.to(torch.int64)`. |
| [`Tensor.lt`](generated/torch.Tensor.lt.html#torch.Tensor.lt) | See [`torch.lt()`](generated/torch.lt.html#torch.lt). |
| [`Tensor.lt_`](generated/torch.Tensor.lt_.html#torch.Tensor.lt_) | In-place version of [`lt()`](generated/torch.Tensor.lt.html#torch.Tensor.lt). |
| [`Tensor.less`](generated/torch.Tensor.less.html#torch.Tensor.less) | lt(other) -> Tensor |
| [`Tensor.less_`](generated/torch.Tensor.less_.html#torch.Tensor.less_) | In-place version of [`less()`](generated/torch.Tensor.less.html#torch.Tensor.less). |
| [`Tensor.lu`](generated/torch.Tensor.lu.html#torch.Tensor.lu) | See [`torch.lu()`](generated/torch.lu.html#torch.lu) |
| [`Tensor.lu_solve`](generated/torch.Tensor.lu_solve.html#torch.Tensor.lu_solve) | See [`torch.lu_solve()`](generated/torch.lu_solve.html#torch.lu_solve) |
| [`Tensor.as_subclass`](generated/torch.Tensor.as_subclass.html#torch.Tensor.as_subclass) | Makes a `cls` instance with the same data pointer as `self`. |
| [`Tensor.map_`](generated/torch.Tensor.map_.html#torch.Tensor.map_) | Applies `callable` for each element in `self` tensor and the given [`tensor`](generated/torch.tensor.html#torch.tensor) and stores the results in `self` tensor. |
| [`Tensor.masked_scatter_`](generated/torch.Tensor.masked_scatter_.html#torch.Tensor.masked_scatter_) | Copies elements from `source` into `self` tensor at positions where the `mask` is True. |
| [`Tensor.masked_scatter`](generated/torch.Tensor.masked_scatter.html#torch.Tensor.masked_scatter) | Out-of-place version of [`torch.Tensor.masked_scatter_()`](generated/torch.Tensor.masked_scatter_.html#torch.Tensor.masked_scatter_) |
| [`Tensor.masked_fill_`](generated/torch.Tensor.masked_fill_.html#torch.Tensor.masked_fill_) | Fills elements of `self` tensor with `value` where `mask` is True. |
| [`Tensor.masked_fill`](generated/torch.Tensor.masked_fill.html#torch.Tensor.masked_fill) | Out-of-place version of [`torch.Tensor.masked_fill_()`](generated/torch.Tensor.masked_fill_.html#torch.Tensor.masked_fill_) |
| [`Tensor.masked_select`](generated/torch.Tensor.masked_select.html#torch.Tensor.masked_select) | See [`torch.masked_select()`](generated/torch.masked_select.html#torch.masked_select) |
| [`Tensor.matmul`](generated/torch.Tensor.matmul.html#torch.Tensor.matmul) | See [`torch.matmul()`](generated/torch.matmul.html#torch.matmul) |
| [`Tensor.matrix_power`](generated/torch.Tensor.matrix_power.html#torch.Tensor.matrix_power) | Note [`matrix_power()`](generated/torch.Tensor.matrix_power.html#torch.Tensor.matrix_power) is deprecated, use [`torch.linalg.matrix_power()`](generated/torch.linalg.matrix_power.html#torch.linalg.matrix_power) instead. |
| [`Tensor.matrix_exp`](generated/torch.Tensor.matrix_exp.html#torch.Tensor.matrix_exp) | See [`torch.matrix_exp()`](generated/torch.matrix_exp.html#torch.matrix_exp) |
| [`Tensor.max`](generated/torch.Tensor.max.html#torch.Tensor.max) | See [`torch.max()`](generated/torch.max.html#torch.max) |
| [`Tensor.maximum`](generated/torch.Tensor.maximum.html#torch.Tensor.maximum) | See [`torch.maximum()`](generated/torch.maximum.html#torch.maximum) |
| [`Tensor.mean`](generated/torch.Tensor.mean.html#torch.Tensor.mean) | See [`torch.mean()`](generated/torch.mean.html#torch.mean) |
| [`Tensor.module_load`](generated/torch.Tensor.module_load.html#torch.Tensor.module_load) | Defines how to transform `other` when loading it into `self` in [`load_state_dict()`](generated/torch.nn.Module.html#torch.nn.Module.load_state_dict). |
| [`Tensor.nanmean`](generated/torch.Tensor.nanmean.html#torch.Tensor.nanmean) | See [`torch.nanmean()`](generated/torch.nanmean.html#torch.nanmean) |
| [`Tensor.median`](generated/torch.Tensor.median.html#torch.Tensor.median) | See [`torch.median()`](generated/torch.median.html#torch.median) |
| [`Tensor.nanmedian`](generated/torch.Tensor.nanmedian.html#torch.Tensor.nanmedian) | See [`torch.nanmedian()`](generated/torch.nanmedian.html#torch.nanmedian) |
| [`Tensor.min`](generated/torch.Tensor.min.html#torch.Tensor.min) | See [`torch.min()`](generated/torch.min.html#torch.min) |
| [`Tensor.minimum`](generated/torch.Tensor.minimum.html#torch.Tensor.minimum) | See [`torch.minimum()`](generated/torch.minimum.html#torch.minimum) |
| [`Tensor.mm`](generated/torch.Tensor.mm.html#torch.Tensor.mm) | See [`torch.mm()`](generated/torch.mm.html#torch.mm) |
| [`Tensor.smm`](generated/torch.Tensor.smm.html#torch.Tensor.smm) | See [`torch.smm()`](generated/torch.smm.html#torch.smm) |
| [`Tensor.mode`](generated/torch.Tensor.mode.html#torch.Tensor.mode) | See [`torch.mode()`](generated/torch.mode.html#torch.mode) |
| [`Tensor.movedim`](generated/torch.Tensor.movedim.html#torch.Tensor.movedim) | See [`torch.movedim()`](generated/torch.movedim.html#torch.movedim) |
| [`Tensor.moveaxis`](generated/torch.Tensor.moveaxis.html#torch.Tensor.moveaxis) | See [`torch.moveaxis()`](generated/torch.moveaxis.html#torch.moveaxis) |
| [`Tensor.msort`](generated/torch.Tensor.msort.html#torch.Tensor.msort) | See [`torch.msort()`](generated/torch.msort.html#torch.msort) |
| [`Tensor.mul`](generated/torch.Tensor.mul.html#torch.Tensor.mul) | See [`torch.mul()`](generated/torch.mul.html#torch.mul). |
| [`Tensor.mul_`](generated/torch.Tensor.mul_.html#torch.Tensor.mul_) | In-place version of [`mul()`](generated/torch.Tensor.mul.html#torch.Tensor.mul). |
| [`Tensor.multiply`](generated/torch.Tensor.multiply.html#torch.Tensor.multiply) | See [`torch.multiply()`](generated/torch.multiply.html#torch.multiply). |
| [`Tensor.multiply_`](generated/torch.Tensor.multiply_.html#torch.Tensor.multiply_) | In-place version of [`multiply()`](generated/torch.Tensor.multiply.html#torch.Tensor.multiply). |
| [`Tensor.multinomial`](generated/torch.Tensor.multinomial.html#torch.Tensor.multinomial) | See [`torch.multinomial()`](generated/torch.multinomial.html#torch.multinomial) |
| [`Tensor.mv`](generated/torch.Tensor.mv.html#torch.Tensor.mv) | See [`torch.mv()`](generated/torch.mv.html#torch.mv) |
| [`Tensor.mvlgamma`](generated/torch.Tensor.mvlgamma.html#torch.Tensor.mvlgamma) | See [`torch.mvlgamma()`](generated/torch.mvlgamma.html#torch.mvlgamma) |
| [`Tensor.mvlgamma_`](generated/torch.Tensor.mvlgamma_.html#torch.Tensor.mvlgamma_) | In-place version of [`mvlgamma()`](generated/torch.Tensor.mvlgamma.html#torch.Tensor.mvlgamma) |
| [`Tensor.nansum`](generated/torch.Tensor.nansum.html#torch.Tensor.nansum) | See [`torch.nansum()`](generated/torch.nansum.html#torch.nansum) |
| [`Tensor.narrow`](generated/torch.Tensor.narrow.html#torch.Tensor.narrow) | See [`torch.narrow()`](generated/torch.narrow.html#torch.narrow). |
| [`Tensor.narrow_copy`](generated/torch.Tensor.narrow_copy.html#torch.Tensor.narrow_copy) | See [`torch.narrow_copy()`](generated/torch.narrow_copy.html#torch.narrow_copy). |
| [`Tensor.ndimension`](generated/torch.Tensor.ndimension.html#torch.Tensor.ndimension) | Alias for [`dim()`](generated/torch.Tensor.dim.html#torch.Tensor.dim) |
| [`Tensor.nan_to_num`](generated/torch.Tensor.nan_to_num.html#torch.Tensor.nan_to_num) | See [`torch.nan_to_num()`](generated/torch.nan_to_num.html#torch.nan_to_num). |
| [`Tensor.nan_to_num_`](generated/torch.Tensor.nan_to_num_.html#torch.Tensor.nan_to_num_) | In-place version of [`nan_to_num()`](generated/torch.Tensor.nan_to_num.html#torch.Tensor.nan_to_num). |
| [`Tensor.ne`](generated/torch.Tensor.ne.html#torch.Tensor.ne) | See [`torch.ne()`](generated/torch.ne.html#torch.ne). |
| [`Tensor.ne_`](generated/torch.Tensor.ne_.html#torch.Tensor.ne_) | In-place version of [`ne()`](generated/torch.Tensor.ne.html#torch.Tensor.ne). |
| [`Tensor.not_equal`](generated/torch.Tensor.not_equal.html#torch.Tensor.not_equal) | See [`torch.not_equal()`](generated/torch.not_equal.html#torch.not_equal). |
| [`Tensor.not_equal_`](generated/torch.Tensor.not_equal_.html#torch.Tensor.not_equal_) | In-place version of [`not_equal()`](generated/torch.Tensor.not_equal.html#torch.Tensor.not_equal). |
| [`Tensor.neg`](generated/torch.Tensor.neg.html#torch.Tensor.neg) | See [`torch.neg()`](generated/torch.neg.html#torch.neg) |
| [`Tensor.neg_`](generated/torch.Tensor.neg_.html#torch.Tensor.neg_) | In-place version of [`neg()`](generated/torch.Tensor.neg.html#torch.Tensor.neg) |
| [`Tensor.negative`](generated/torch.Tensor.negative.html#torch.Tensor.negative) | See [`torch.negative()`](generated/torch.negative.html#torch.negative) |
| [`Tensor.negative_`](generated/torch.Tensor.negative_.html#torch.Tensor.negative_) | In-place version of [`negative()`](generated/torch.Tensor.negative.html#torch.Tensor.negative) |
| [`Tensor.nelement`](generated/torch.Tensor.nelement.html#torch.Tensor.nelement) | Alias for [`numel()`](generated/torch.Tensor.numel.html#torch.Tensor.numel) |
| [`Tensor.nextafter`](generated/torch.Tensor.nextafter.html#torch.Tensor.nextafter) | See [`torch.nextafter()`](generated/torch.nextafter.html#torch.nextafter) |
| [`Tensor.nextafter_`](generated/torch.Tensor.nextafter_.html#torch.Tensor.nextafter_) | In-place version of [`nextafter()`](generated/torch.Tensor.nextafter.html#torch.Tensor.nextafter) |
| [`Tensor.nonzero`](generated/torch.Tensor.nonzero.html#torch.Tensor.nonzero) | See [`torch.nonzero()`](generated/torch.nonzero.html#torch.nonzero) |
| [`Tensor.norm`](generated/torch.Tensor.norm.html#torch.Tensor.norm) | See [`torch.linalg.norm()`](generated/torch.linalg.norm.html#torch.linalg.norm) |
| [`Tensor.normal_`](generated/torch.Tensor.normal_.html#torch.Tensor.normal_) | Fills `self` tensor with elements samples from the normal distribution parameterized by [`mean`](generated/torch.mean.html#torch.mean) and [`std`](generated/torch.std.html#torch.std). |
| [`Tensor.numel`](generated/torch.Tensor.numel.html#torch.Tensor.numel) | See [`torch.numel()`](generated/torch.numel.html#torch.numel) |
| [`Tensor.numpy`](generated/torch.Tensor.numpy.html#torch.Tensor.numpy) | Returns the tensor as a NumPy `ndarray`. |
| [`Tensor.orgqr`](generated/torch.Tensor.orgqr.html#torch.Tensor.orgqr) | See [`torch.orgqr()`](generated/torch.orgqr.html#torch.orgqr) |
| [`Tensor.ormqr`](generated/torch.Tensor.ormqr.html#torch.Tensor.ormqr) | See [`torch.ormqr()`](generated/torch.ormqr.html#torch.ormqr) |
| [`Tensor.outer`](generated/torch.Tensor.outer.html#torch.Tensor.outer) | See [`torch.outer()`](generated/torch.outer.html#torch.outer). |
| [`Tensor.permute`](generated/torch.Tensor.permute.html#torch.Tensor.permute) | Returns a view of the tensor with its dimensions permuted. |
| [`Tensor.pin_memory`](generated/torch.Tensor.pin_memory.html#torch.Tensor.pin_memory) | Copies the tensor to pinned memory, if it's not already pinned. |
| [`Tensor.pinverse`](generated/torch.Tensor.pinverse.html#torch.Tensor.pinverse) | See [`torch.pinverse()`](generated/torch.pinverse.html#torch.pinverse) |
| [`Tensor.polygamma`](generated/torch.Tensor.polygamma.html#torch.Tensor.polygamma) | See [`torch.polygamma()`](generated/torch.polygamma.html#torch.polygamma) |
| [`Tensor.polygamma_`](generated/torch.Tensor.polygamma_.html#torch.Tensor.polygamma_) | In-place version of [`polygamma()`](generated/torch.Tensor.polygamma.html#torch.Tensor.polygamma) |
| [`Tensor.positive`](generated/torch.Tensor.positive.html#torch.Tensor.positive) | See [`torch.positive()`](generated/torch.positive.html#torch.positive) |
| [`Tensor.pow`](generated/torch.Tensor.pow.html#torch.Tensor.pow) | See [`torch.pow()`](generated/torch.pow.html#torch.pow) |
| [`Tensor.pow_`](generated/torch.Tensor.pow_.html#torch.Tensor.pow_) | In-place version of [`pow()`](generated/torch.Tensor.pow.html#torch.Tensor.pow) |
| [`Tensor.prod`](generated/torch.Tensor.prod.html#torch.Tensor.prod) | See [`torch.prod()`](generated/torch.prod.html#torch.prod) |
| [`Tensor.put_`](generated/torch.Tensor.put_.html#torch.Tensor.put_) | Copies the elements from `source` into the positions specified by `index`. |
| [`Tensor.qr`](generated/torch.Tensor.qr.html#torch.Tensor.qr) | See [`torch.qr()`](generated/torch.qr.html#torch.qr) |
| [`Tensor.qscheme`](generated/torch.Tensor.qscheme.html#torch.Tensor.qscheme) | Returns the quantization scheme of a given QTensor. |
| [`Tensor.quantile`](generated/torch.Tensor.quantile.html#torch.Tensor.quantile) | See [`torch.quantile()`](generated/torch.quantile.html#torch.quantile) |
| [`Tensor.nanquantile`](generated/torch.Tensor.nanquantile.html#torch.Tensor.nanquantile) | See [`torch.nanquantile()`](generated/torch.nanquantile.html#torch.nanquantile) |
| [`Tensor.q_scale`](generated/torch.Tensor.q_scale.html#torch.Tensor.q_scale) | Given a Tensor quantized by linear(affine) quantization, returns the scale of the underlying quantizer(). |
| [`Tensor.q_zero_point`](generated/torch.Tensor.q_zero_point.html#torch.Tensor.q_zero_point) | Given a Tensor quantized by linear(affine) quantization, returns the zero_point of the underlying quantizer(). |
| [`Tensor.q_per_channel_scales`](generated/torch.Tensor.q_per_channel_scales.html#torch.Tensor.q_per_channel_scales) | Given a Tensor quantized by linear (affine) per-channel quantization, returns a Tensor of scales of the underlying quantizer. |
| [`Tensor.q_per_channel_zero_points`](generated/torch.Tensor.q_per_channel_zero_points.html#torch.Tensor.q_per_channel_zero_points) | Given a Tensor quantized by linear (affine) per-channel quantization, returns a tensor of zero_points of the underlying quantizer. |
| [`Tensor.q_per_channel_axis`](generated/torch.Tensor.q_per_channel_axis.html#torch.Tensor.q_per_channel_axis) | Given a Tensor quantized by linear (affine) per-channel quantization, returns the index of dimension on which per-channel quantization is applied. |
| [`Tensor.rad2deg`](generated/torch.Tensor.rad2deg.html#torch.Tensor.rad2deg) | See [`torch.rad2deg()`](generated/torch.rad2deg.html#torch.rad2deg) |
| [`Tensor.random_`](generated/torch.Tensor.random_.html#torch.Tensor.random_) | Fills `self` tensor with numbers sampled from the discrete uniform distribution over `[from, to - 1]`. |
| [`Tensor.ravel`](generated/torch.Tensor.ravel.html#torch.Tensor.ravel) | see [`torch.ravel()`](generated/torch.ravel.html#torch.ravel) |
| [`Tensor.reciprocal`](generated/torch.Tensor.reciprocal.html#torch.Tensor.reciprocal) | See [`torch.reciprocal()`](generated/torch.reciprocal.html#torch.reciprocal) |
| [`Tensor.reciprocal_`](generated/torch.Tensor.reciprocal_.html#torch.Tensor.reciprocal_) | In-place version of [`reciprocal()`](generated/torch.Tensor.reciprocal.html#torch.Tensor.reciprocal) |
| [`Tensor.record_stream`](generated/torch.Tensor.record_stream.html#torch.Tensor.record_stream) | Marks the tensor as having been used by this stream. |
| [`Tensor.register_hook`](generated/torch.Tensor.register_hook.html#torch.Tensor.register_hook) | Registers a backward hook. |
| [`Tensor.register_post_accumulate_grad_hook`](generated/torch.Tensor.register_post_accumulate_grad_hook.html#torch.Tensor.register_post_accumulate_grad_hook) | Registers a backward hook that runs after grad accumulation. |
| [`Tensor.remainder`](generated/torch.Tensor.remainder.html#torch.Tensor.remainder) | See [`torch.remainder()`](generated/torch.remainder.html#torch.remainder) |
| [`Tensor.remainder_`](generated/torch.Tensor.remainder_.html#torch.Tensor.remainder_) | In-place version of [`remainder()`](generated/torch.Tensor.remainder.html#torch.Tensor.remainder) |
| [`Tensor.renorm`](generated/torch.Tensor.renorm.html#torch.Tensor.renorm) | See [`torch.renorm()`](generated/torch.renorm.html#torch.renorm) |
| [`Tensor.renorm_`](generated/torch.Tensor.renorm_.html#torch.Tensor.renorm_) | In-place version of [`renorm()`](generated/torch.Tensor.renorm.html#torch.Tensor.renorm) |
| [`Tensor.repeat`](generated/torch.Tensor.repeat.html#torch.Tensor.repeat) | Repeats this tensor along the specified dimensions. |
| [`Tensor.repeat_interleave`](generated/torch.Tensor.repeat_interleave.html#torch.Tensor.repeat_interleave) | See [`torch.repeat_interleave()`](generated/torch.repeat_interleave.html#torch.repeat_interleave). |
| [`Tensor.requires_grad`](generated/torch.Tensor.requires_grad.html#torch.Tensor.requires_grad) | Is `True` if gradients need to be computed for this Tensor, `False` otherwise. |
| [`Tensor.requires_grad_`](generated/torch.Tensor.requires_grad_.html#torch.Tensor.requires_grad_) | Change if autograd should record operations on this tensor: sets this tensor's `requires_grad` attribute in-place. |
| [`Tensor.reshape`](generated/torch.Tensor.reshape.html#torch.Tensor.reshape) | Returns a tensor with the same data and number of elements as `self` but with the specified shape. |
| [`Tensor.reshape_as`](generated/torch.Tensor.reshape_as.html#torch.Tensor.reshape_as) | Returns this tensor as the same shape as `other`. |
| [`Tensor.resize_`](generated/torch.Tensor.resize_.html#torch.Tensor.resize_) | Resizes `self` tensor to the specified size. |
| [`Tensor.resize_as_`](generated/torch.Tensor.resize_as_.html#torch.Tensor.resize_as_) | Resizes the `self` tensor to be the same size as the specified [`tensor`](generated/torch.tensor.html#torch.tensor). |
| [`Tensor.retain_grad`](generated/torch.Tensor.retain_grad.html#torch.Tensor.retain_grad) | Enables this Tensor to have their `grad` populated during `backward()`. |
| [`Tensor.retains_grad`](generated/torch.Tensor.retains_grad.html#torch.Tensor.retains_grad) | Is `True` if this Tensor is non-leaf and its `grad` is enabled to be populated during `backward()`, `False` otherwise. |
| [`Tensor.roll`](generated/torch.Tensor.roll.html#torch.Tensor.roll) | See [`torch.roll()`](generated/torch.roll.html#torch.roll) |
| [`Tensor.rot90`](generated/torch.Tensor.rot90.html#torch.Tensor.rot90) | See [`torch.rot90()`](generated/torch.rot90.html#torch.rot90) |
| [`Tensor.round`](generated/torch.Tensor.round.html#torch.Tensor.round) | See [`torch.round()`](generated/torch.round.html#torch.round) |
| [`Tensor.round_`](generated/torch.Tensor.round_.html#torch.Tensor.round_) | In-place version of [`round()`](generated/torch.Tensor.round.html#torch.Tensor.round) |
| [`Tensor.rsqrt`](generated/torch.Tensor.rsqrt.html#torch.Tensor.rsqrt) | See [`torch.rsqrt()`](generated/torch.rsqrt.html#torch.rsqrt) |
| [`Tensor.rsqrt_`](generated/torch.Tensor.rsqrt_.html#torch.Tensor.rsqrt_) | In-place version of [`rsqrt()`](generated/torch.Tensor.rsqrt.html#torch.Tensor.rsqrt) |
| [`Tensor.scatter`](generated/torch.Tensor.scatter.html#torch.Tensor.scatter) | Out-of-place version of [`torch.Tensor.scatter_()`](generated/torch.Tensor.scatter_.html#torch.Tensor.scatter_) |
| [`Tensor.scatter_`](generated/torch.Tensor.scatter_.html#torch.Tensor.scatter_) | Writes all values from the tensor `src` into `self` at the indices specified in the `index` tensor. |
| [`Tensor.scatter_add_`](generated/torch.Tensor.scatter_add_.html#torch.Tensor.scatter_add_) | Adds all values from the tensor `src` into `self` at the indices specified in the `index` tensor in a similar fashion as [`scatter_()`](generated/torch.Tensor.scatter_.html#torch.Tensor.scatter_). |
| [`Tensor.scatter_add`](generated/torch.Tensor.scatter_add.html#torch.Tensor.scatter_add) | Out-of-place version of [`torch.Tensor.scatter_add_()`](generated/torch.Tensor.scatter_add_.html#torch.Tensor.scatter_add_) |
| [`Tensor.scatter_reduce_`](generated/torch.Tensor.scatter_reduce_.html#torch.Tensor.scatter_reduce_) | Reduces all values from the `src` tensor to the indices specified in the `index` tensor in the `self` tensor using the applied reduction defined via the `reduce` argument (`"sum"`, `"prod"`, `"mean"`, `"amax"`, `"amin"`). |
| [`Tensor.scatter_reduce`](generated/torch.Tensor.scatter_reduce.html#torch.Tensor.scatter_reduce) | Out-of-place version of [`torch.Tensor.scatter_reduce_()`](generated/torch.Tensor.scatter_reduce_.html#torch.Tensor.scatter_reduce_) |
| [`Tensor.select`](generated/torch.Tensor.select.html#torch.Tensor.select) | See [`torch.select()`](generated/torch.select.html#torch.select) |
| [`Tensor.select_scatter`](generated/torch.Tensor.select_scatter.html#torch.Tensor.select_scatter) | See [`torch.select_scatter()`](generated/torch.select_scatter.html#torch.select_scatter) |
| [`Tensor.set_`](generated/torch.Tensor.set_.html#torch.Tensor.set_) | Sets the underlying storage, size, and strides. |
| [`Tensor.share_memory_`](generated/torch.Tensor.share_memory_.html#torch.Tensor.share_memory_) | Moves the underlying storage to shared memory. |
| [`Tensor.short`](generated/torch.Tensor.short.html#torch.Tensor.short) | `self.short()` is equivalent to `self.to(torch.int16)`. |
| [`Tensor.sigmoid`](generated/torch.Tensor.sigmoid.html#torch.Tensor.sigmoid) | See [`torch.sigmoid()`](generated/torch.sigmoid.html#torch.sigmoid) |
| [`Tensor.sigmoid_`](generated/torch.Tensor.sigmoid_.html#torch.Tensor.sigmoid_) | In-place version of [`sigmoid()`](generated/torch.Tensor.sigmoid.html#torch.Tensor.sigmoid) |
| [`Tensor.sign`](generated/torch.Tensor.sign.html#torch.Tensor.sign) | See [`torch.sign()`](generated/torch.sign.html#torch.sign) |
| [`Tensor.sign_`](generated/torch.Tensor.sign_.html#torch.Tensor.sign_) | In-place version of [`sign()`](generated/torch.Tensor.sign.html#torch.Tensor.sign) |
| [`Tensor.signbit`](generated/torch.Tensor.signbit.html#torch.Tensor.signbit) | See [`torch.signbit()`](generated/torch.signbit.html#torch.signbit) |
| [`Tensor.sgn`](generated/torch.Tensor.sgn.html#torch.Tensor.sgn) | See [`torch.sgn()`](generated/torch.sgn.html#torch.sgn) |
| [`Tensor.sgn_`](generated/torch.Tensor.sgn_.html#torch.Tensor.sgn_) | In-place version of [`sgn()`](generated/torch.Tensor.sgn.html#torch.Tensor.sgn) |
| [`Tensor.sin`](generated/torch.Tensor.sin.html#torch.Tensor.sin) | See [`torch.sin()`](generated/torch.sin.html#torch.sin) |
| [`Tensor.sin_`](generated/torch.Tensor.sin_.html#torch.Tensor.sin_) | In-place version of [`sin()`](generated/torch.Tensor.sin.html#torch.Tensor.sin) |
| [`Tensor.sinc`](generated/torch.Tensor.sinc.html#torch.Tensor.sinc) | See [`torch.sinc()`](generated/torch.sinc.html#torch.sinc) |
| [`Tensor.sinc_`](generated/torch.Tensor.sinc_.html#torch.Tensor.sinc_) | In-place version of [`sinc()`](generated/torch.Tensor.sinc.html#torch.Tensor.sinc) |
| [`Tensor.sinh`](generated/torch.Tensor.sinh.html#torch.Tensor.sinh) | See [`torch.sinh()`](generated/torch.sinh.html#torch.sinh) |
| [`Tensor.sinh_`](generated/torch.Tensor.sinh_.html#torch.Tensor.sinh_) | In-place version of [`sinh()`](generated/torch.Tensor.sinh.html#torch.Tensor.sinh) |
| [`Tensor.asinh`](generated/torch.Tensor.asinh.html#torch.Tensor.asinh) | See [`torch.asinh()`](generated/torch.asinh.html#torch.asinh) |
| [`Tensor.asinh_`](generated/torch.Tensor.asinh_.html#torch.Tensor.asinh_) | In-place version of [`asinh()`](generated/torch.Tensor.asinh.html#torch.Tensor.asinh) |
| [`Tensor.arcsinh`](generated/torch.Tensor.arcsinh.html#torch.Tensor.arcsinh) | See [`torch.arcsinh()`](generated/torch.arcsinh.html#torch.arcsinh) |
| [`Tensor.arcsinh_`](generated/torch.Tensor.arcsinh_.html#torch.Tensor.arcsinh_) | In-place version of [`arcsinh()`](generated/torch.Tensor.arcsinh.html#torch.Tensor.arcsinh) |
| [`Tensor.shape`](generated/torch.Tensor.shape.html#torch.Tensor.shape) | Returns the size of the `self` tensor. |
| [`Tensor.size`](generated/torch.Tensor.size.html#torch.Tensor.size) | Returns the size of the `self` tensor. |
| [`Tensor.slogdet`](generated/torch.Tensor.slogdet.html#torch.Tensor.slogdet) | See [`torch.slogdet()`](generated/torch.slogdet.html#torch.slogdet) |
| [`Tensor.slice_scatter`](generated/torch.Tensor.slice_scatter.html#torch.Tensor.slice_scatter) | See [`torch.slice_scatter()`](generated/torch.slice_scatter.html#torch.slice_scatter) |
| [`Tensor.softmax`](generated/torch.Tensor.softmax.html#torch.Tensor.softmax) | Alias for [`torch.nn.functional.softmax()`](generated/torch.nn.functional.softmax.html#torch.nn.functional.softmax). |
| [`Tensor.sort`](generated/torch.Tensor.sort.html#torch.Tensor.sort) | See [`torch.sort()`](generated/torch.sort.html#torch.sort) |
| [`Tensor.split`](generated/torch.Tensor.split.html#torch.Tensor.split) | See [`torch.split()`](generated/torch.split.html#torch.split) |
| [`Tensor.sparse_mask`](generated/torch.Tensor.sparse_mask.html#torch.Tensor.sparse_mask) | Returns a new [sparse tensor](sparse.html#sparse-docs) with values from a strided tensor `self` filtered by the indices of the sparse tensor `mask`. |
| [`Tensor.sparse_dim`](generated/torch.Tensor.sparse_dim.html#torch.Tensor.sparse_dim) | Return the number of sparse dimensions in a [sparse tensor](sparse.html#sparse-docs) `self`. |
| [`Tensor.sqrt`](generated/torch.Tensor.sqrt.html#torch.Tensor.sqrt) | See [`torch.sqrt()`](generated/torch.sqrt.html#torch.sqrt) |
| [`Tensor.sqrt_`](generated/torch.Tensor.sqrt_.html#torch.Tensor.sqrt_) | In-place version of [`sqrt()`](generated/torch.Tensor.sqrt.html#torch.Tensor.sqrt) |
| [`Tensor.square`](generated/torch.Tensor.square.html#torch.Tensor.square) | See [`torch.square()`](generated/torch.square.html#torch.square) |
| [`Tensor.square_`](generated/torch.Tensor.square_.html#torch.Tensor.square_) | In-place version of [`square()`](generated/torch.Tensor.square.html#torch.Tensor.square) |
| [`Tensor.squeeze`](generated/torch.Tensor.squeeze.html#torch.Tensor.squeeze) | See [`torch.squeeze()`](generated/torch.squeeze.html#torch.squeeze) |
| [`Tensor.squeeze_`](generated/torch.Tensor.squeeze_.html#torch.Tensor.squeeze_) | In-place version of [`squeeze()`](generated/torch.Tensor.squeeze.html#torch.Tensor.squeeze) |
| [`Tensor.std`](generated/torch.Tensor.std.html#torch.Tensor.std) | See [`torch.std()`](generated/torch.std.html#torch.std) |
| [`Tensor.stft`](generated/torch.Tensor.stft.html#torch.Tensor.stft) | See [`torch.stft()`](generated/torch.stft.html#torch.stft) |
| [`Tensor.storage`](generated/torch.Tensor.storage.html#torch.Tensor.storage) | Returns the underlying [`TypedStorage`](storage.html#torch.TypedStorage). |
| [`Tensor.untyped_storage`](generated/torch.Tensor.untyped_storage.html#torch.Tensor.untyped_storage) | Returns the underlying [`UntypedStorage`](storage.html#torch.UntypedStorage). |
| [`Tensor.storage_offset`](generated/torch.Tensor.storage_offset.html#torch.Tensor.storage_offset) | Returns `self` tensor's offset in the underlying storage in terms of number of storage elements (not bytes). |
| [`Tensor.storage_type`](generated/torch.Tensor.storage_type.html#torch.Tensor.storage_type) | Returns the type of the underlying storage. |
| [`Tensor.stride`](generated/torch.Tensor.stride.html#torch.Tensor.stride) | Returns the stride of `self` tensor. |
| [`Tensor.sub`](generated/torch.Tensor.sub.html#torch.Tensor.sub) | See [`torch.sub()`](generated/torch.sub.html#torch.sub). |
| [`Tensor.sub_`](generated/torch.Tensor.sub_.html#torch.Tensor.sub_) | In-place version of [`sub()`](generated/torch.Tensor.sub.html#torch.Tensor.sub) |
| [`Tensor.subtract`](generated/torch.Tensor.subtract.html#torch.Tensor.subtract) | See [`torch.subtract()`](generated/torch.subtract.html#torch.subtract). |
| [`Tensor.subtract_`](generated/torch.Tensor.subtract_.html#torch.Tensor.subtract_) | In-place version of [`subtract()`](generated/torch.Tensor.subtract.html#torch.Tensor.subtract). |
| [`Tensor.sum`](generated/torch.Tensor.sum.html#torch.Tensor.sum) | See [`torch.sum()`](generated/torch.sum.html#torch.sum) |
| [`Tensor.sum_to_size`](generated/torch.Tensor.sum_to_size.html#torch.Tensor.sum_to_size) | Sum `this` tensor to `size`. |
| [`Tensor.svd`](generated/torch.Tensor.svd.html#torch.Tensor.svd) | See [`torch.svd()`](generated/torch.svd.html#torch.svd) |
| [`Tensor.swapaxes`](generated/torch.Tensor.swapaxes.html#torch.Tensor.swapaxes) | See [`torch.swapaxes()`](generated/torch.swapaxes.html#torch.swapaxes) |
| [`Tensor.swapdims`](generated/torch.Tensor.swapdims.html#torch.Tensor.swapdims) | See [`torch.swapdims()`](generated/torch.swapdims.html#torch.swapdims) |
| [`Tensor.t`](generated/torch.Tensor.t.html#torch.Tensor.t) | See [`torch.t()`](generated/torch.t.html#torch.t) |
| [`Tensor.t_`](generated/torch.Tensor.t_.html#torch.Tensor.t_) | In-place version of [`t()`](generated/torch.Tensor.t.html#torch.Tensor.t) |
| [`Tensor.tensor_split`](generated/torch.Tensor.tensor_split.html#torch.Tensor.tensor_split) | See [`torch.tensor_split()`](generated/torch.tensor_split.html#torch.tensor_split) |
| [`Tensor.tile`](generated/torch.Tensor.tile.html#torch.Tensor.tile) | See [`torch.tile()`](generated/torch.tile.html#torch.tile) |
| [`Tensor.to`](generated/torch.Tensor.to.html#torch.Tensor.to) | Performs Tensor dtype and/or device conversion. |
| [`Tensor.to_mkldnn`](generated/torch.Tensor.to_mkldnn.html#torch.Tensor.to_mkldnn) | Returns a copy of the tensor in `torch.mkldnn` layout. |
| [`Tensor.take`](generated/torch.Tensor.take.html#torch.Tensor.take) | See [`torch.take()`](generated/torch.take.html#torch.take) |
| [`Tensor.take_along_dim`](generated/torch.Tensor.take_along_dim.html#torch.Tensor.take_along_dim) | See [`torch.take_along_dim()`](generated/torch.take_along_dim.html#torch.take_along_dim) |
| [`Tensor.tan`](generated/torch.Tensor.tan.html#torch.Tensor.tan) | See [`torch.tan()`](generated/torch.tan.html#torch.tan) |
| [`Tensor.tan_`](generated/torch.Tensor.tan_.html#torch.Tensor.tan_) | In-place version of [`tan()`](generated/torch.Tensor.tan.html#torch.Tensor.tan) |
| [`Tensor.tanh`](generated/torch.Tensor.tanh.html#torch.Tensor.tanh) | See [`torch.tanh()`](generated/torch.tanh.html#torch.tanh) |
| [`Tensor.tanh_`](generated/torch.Tensor.tanh_.html#torch.Tensor.tanh_) | In-place version of [`tanh()`](generated/torch.Tensor.tanh.html#torch.Tensor.tanh) |
| [`Tensor.atanh`](generated/torch.Tensor.atanh.html#torch.Tensor.atanh) | See [`torch.atanh()`](generated/torch.atanh.html#torch.atanh) |
| [`Tensor.atanh_`](generated/torch.Tensor.atanh_.html#torch.Tensor.atanh_) | In-place version of [`atanh()`](generated/torch.Tensor.atanh.html#torch.Tensor.atanh) |
| [`Tensor.arctanh`](generated/torch.Tensor.arctanh.html#torch.Tensor.arctanh) | See [`torch.arctanh()`](generated/torch.arctanh.html#torch.arctanh) |
| [`Tensor.arctanh_`](generated/torch.Tensor.arctanh_.html#torch.Tensor.arctanh_) | In-place version of [`arctanh()`](generated/torch.Tensor.arctanh.html#torch.Tensor.arctanh) |
| [`Tensor.tolist`](generated/torch.Tensor.tolist.html#torch.Tensor.tolist) | Returns the tensor as a (nested) list. |
| [`Tensor.topk`](generated/torch.Tensor.topk.html#torch.Tensor.topk) | See [`torch.topk()`](generated/torch.topk.html#torch.topk) |
| [`Tensor.to_dense`](generated/torch.Tensor.to_dense.html#torch.Tensor.to_dense) | Creates a strided copy of `self` if `self` is not a strided tensor, otherwise returns `self`. |
| [`Tensor.to_sparse`](generated/torch.Tensor.to_sparse.html#torch.Tensor.to_sparse) | Returns a sparse copy of the tensor. |
| [`Tensor.to_sparse_csr`](generated/torch.Tensor.to_sparse_csr.html#torch.Tensor.to_sparse_csr) | Convert a tensor to compressed row storage format (CSR). |
| [`Tensor.to_sparse_csc`](generated/torch.Tensor.to_sparse_csc.html#torch.Tensor.to_sparse_csc) | Convert a tensor to compressed column storage (CSC) format. |
| [`Tensor.to_sparse_bsr`](generated/torch.Tensor.to_sparse_bsr.html#torch.Tensor.to_sparse_bsr) | Convert a tensor to a block sparse row (BSR) storage format of given blocksize. |
| [`Tensor.to_sparse_bsc`](generated/torch.Tensor.to_sparse_bsc.html#torch.Tensor.to_sparse_bsc) | Convert a tensor to a block sparse column (BSC) storage format of given blocksize. |
| [`Tensor.trace`](generated/torch.Tensor.trace.html#torch.Tensor.trace) | See [`torch.trace()`](generated/torch.trace.html#torch.trace) |
| [`Tensor.transpose`](generated/torch.Tensor.transpose.html#torch.Tensor.transpose) | See [`torch.transpose()`](generated/torch.transpose.html#torch.transpose) |
| [`Tensor.transpose_`](generated/torch.Tensor.transpose_.html#torch.Tensor.transpose_) | In-place version of [`transpose()`](generated/torch.Tensor.transpose.html#torch.Tensor.transpose) |
| [`Tensor.triangular_solve`](generated/torch.Tensor.triangular_solve.html#torch.Tensor.triangular_solve) | See [`torch.triangular_solve()`](generated/torch.triangular_solve.html#torch.triangular_solve) |
| [`Tensor.tril`](generated/torch.Tensor.tril.html#torch.Tensor.tril) | See [`torch.tril()`](generated/torch.tril.html#torch.tril) |
| [`Tensor.tril_`](generated/torch.Tensor.tril_.html#torch.Tensor.tril_) | In-place version of [`tril()`](generated/torch.Tensor.tril.html#torch.Tensor.tril) |
| [`Tensor.triu`](generated/torch.Tensor.triu.html#torch.Tensor.triu) | See [`torch.triu()`](generated/torch.triu.html#torch.triu) |
| [`Tensor.triu_`](generated/torch.Tensor.triu_.html#torch.Tensor.triu_) | In-place version of [`triu()`](generated/torch.Tensor.triu.html#torch.Tensor.triu) |
| [`Tensor.true_divide`](generated/torch.Tensor.true_divide.html#torch.Tensor.true_divide) | See [`torch.true_divide()`](generated/torch.true_divide.html#torch.true_divide) |
| [`Tensor.true_divide_`](generated/torch.Tensor.true_divide_.html#torch.Tensor.true_divide_) | In-place version of [`true_divide_()`](generated/torch.Tensor.true_divide_.html#torch.Tensor.true_divide_) |
| [`Tensor.trunc`](generated/torch.Tensor.trunc.html#torch.Tensor.trunc) | See [`torch.trunc()`](generated/torch.trunc.html#torch.trunc) |
| [`Tensor.trunc_`](generated/torch.Tensor.trunc_.html#torch.Tensor.trunc_) | In-place version of [`trunc()`](generated/torch.Tensor.trunc.html#torch.Tensor.trunc) |
| [`Tensor.type`](generated/torch.Tensor.type.html#torch.Tensor.type) | Returns the type if dtype is not provided, else casts this object to the specified type. |
| [`Tensor.type_as`](generated/torch.Tensor.type_as.html#torch.Tensor.type_as) | Returns this tensor cast to the type of the given tensor. |
| [`Tensor.unbind`](generated/torch.Tensor.unbind.html#torch.Tensor.unbind) | See [`torch.unbind()`](generated/torch.unbind.html#torch.unbind) |
| [`Tensor.unflatten`](generated/torch.Tensor.unflatten.html#torch.Tensor.unflatten) | See [`torch.unflatten()`](generated/torch.unflatten.html#torch.unflatten). |
| [`Tensor.unfold`](generated/torch.Tensor.unfold.html#torch.Tensor.unfold) | Returns a view of the original tensor which contains all slices of size `size` from `self` tensor in the dimension `dimension`. |
| [`Tensor.uniform_`](generated/torch.Tensor.uniform_.html#torch.Tensor.uniform_) | Fills `self` tensor with numbers sampled from the continuous uniform distribution: |
| [`Tensor.unique`](generated/torch.Tensor.unique.html#torch.Tensor.unique) | Returns the unique elements of the input tensor. |
| [`Tensor.unique_consecutive`](generated/torch.Tensor.unique_consecutive.html#torch.Tensor.unique_consecutive) | Eliminates all but the first element from every consecutive group of equivalent elements. |
| [`Tensor.unsqueeze`](generated/torch.Tensor.unsqueeze.html#torch.Tensor.unsqueeze) | See [`torch.unsqueeze()`](generated/torch.unsqueeze.html#torch.unsqueeze) |
| [`Tensor.unsqueeze_`](generated/torch.Tensor.unsqueeze_.html#torch.Tensor.unsqueeze_) | In-place version of [`unsqueeze()`](generated/torch.Tensor.unsqueeze.html#torch.Tensor.unsqueeze) |
| [`Tensor.values`](generated/torch.Tensor.values.html#torch.Tensor.values) | Return the values tensor of a [sparse COO tensor](sparse.html#sparse-coo-docs). |
| [`Tensor.var`](generated/torch.Tensor.var.html#torch.Tensor.var) | See [`torch.var()`](generated/torch.var.html#torch.var) |
| [`Tensor.vdot`](generated/torch.Tensor.vdot.html#torch.Tensor.vdot) | See [`torch.vdot()`](generated/torch.vdot.html#torch.vdot) |
| [`Tensor.view`](generated/torch.Tensor.view.html#torch.Tensor.view) | Returns a new tensor with the same data as the `self` tensor but of a different `shape`. |
| [`Tensor.view_as`](generated/torch.Tensor.view_as.html#torch.Tensor.view_as) | View this tensor as the same size as `other`. |
| [`Tensor.vsplit`](generated/torch.Tensor.vsplit.html#torch.Tensor.vsplit) | See [`torch.vsplit()`](generated/torch.vsplit.html#torch.vsplit) |
| [`Tensor.where`](generated/torch.Tensor.where.html#torch.Tensor.where) | `self.where(condition, y)` is equivalent to `torch.where(condition, self, y)`. |
| [`Tensor.xlogy`](generated/torch.Tensor.xlogy.html#torch.Tensor.xlogy) | See [`torch.xlogy()`](generated/torch.xlogy.html#torch.xlogy) |
| [`Tensor.xlogy_`](generated/torch.Tensor.xlogy_.html#torch.Tensor.xlogy_) | In-place version of [`xlogy()`](generated/torch.Tensor.xlogy.html#torch.Tensor.xlogy) |
| [`Tensor.xpu`](generated/torch.Tensor.xpu.html#torch.Tensor.xpu) | Returns a copy of this object in XPU memory. |
| [`Tensor.zero_`](generated/torch.Tensor.zero_.html#torch.Tensor.zero_) | Fills `self` tensor with zeros. |