# Named Tensors operator coverage

Please read [Named Tensors](named_tensor.html#named-tensors-doc) first for an introduction to named tensors.

This document is a reference for *name inference*, a process that defines how
named tensors:

1. use names to provide additional automatic runtime correctness checks
2. propagate names from input tensors to output tensors

Below is a list of all operations that are supported with named tensors
and their associated name inference rules.

If you don't see an operation listed here, but it would help your use case, please
[search if an issue has already been filed](https://github.com/pytorch/pytorch/issues?q=is%3Aopen+is%3Aissue+label%3A%22module%3A+named+tensor%22) and if not, [file one](https://github.com/pytorch/pytorch/issues/new/choose).

Warning

The named tensor API is experimental and subject to change.

| API | Name inference rule |
| --- | --- |
| [`Tensor.abs()`](generated/torch.Tensor.abs.html#torch.Tensor.abs), [`torch.abs()`](generated/torch.abs.html#torch.abs) | Keeps input names |
| [`Tensor.abs_()`](generated/torch.Tensor.abs_.html#torch.Tensor.abs_) | Keeps input names |
| [`Tensor.acos()`](generated/torch.Tensor.acos.html#torch.Tensor.acos), [`torch.acos()`](generated/torch.acos.html#torch.acos) | Keeps input names |
| [`Tensor.acos_()`](generated/torch.Tensor.acos_.html#torch.Tensor.acos_) | Keeps input names |
| [`Tensor.add()`](generated/torch.Tensor.add.html#torch.Tensor.add), [`torch.add()`](generated/torch.add.html#torch.add) | Unifies names from inputs |
| [`Tensor.add_()`](generated/torch.Tensor.add_.html#torch.Tensor.add_) | Unifies names from inputs |
| [`Tensor.addmm()`](generated/torch.Tensor.addmm.html#torch.Tensor.addmm), [`torch.addmm()`](generated/torch.addmm.html#torch.addmm) | Contracts away dims |
| [`Tensor.addmm_()`](generated/torch.Tensor.addmm_.html#torch.Tensor.addmm_) | Contracts away dims |
| [`Tensor.addmv()`](generated/torch.Tensor.addmv.html#torch.Tensor.addmv), [`torch.addmv()`](generated/torch.addmv.html#torch.addmv) | Contracts away dims |
| [`Tensor.addmv_()`](generated/torch.Tensor.addmv_.html#torch.Tensor.addmv_) | Contracts away dims |
| [`Tensor.align_as()`](named_tensor.html#torch.Tensor.align_as) | See documentation |
| [`Tensor.align_to()`](named_tensor.html#torch.Tensor.align_to) | See documentation |
| [`Tensor.all()`](generated/torch.Tensor.all.html#torch.Tensor.all), [`torch.all()`](generated/torch.all.html#torch.all) | None |
| [`Tensor.any()`](generated/torch.Tensor.any.html#torch.Tensor.any), [`torch.any()`](generated/torch.any.html#torch.any) | None |
| [`Tensor.asin()`](generated/torch.Tensor.asin.html#torch.Tensor.asin), [`torch.asin()`](generated/torch.asin.html#torch.asin) | Keeps input names |
| [`Tensor.asin_()`](generated/torch.Tensor.asin_.html#torch.Tensor.asin_) | Keeps input names |
| [`Tensor.atan()`](generated/torch.Tensor.atan.html#torch.Tensor.atan), [`torch.atan()`](generated/torch.atan.html#torch.atan) | Keeps input names |
| [`Tensor.atan2()`](generated/torch.Tensor.atan2.html#torch.Tensor.atan2), [`torch.atan2()`](generated/torch.atan2.html#torch.atan2) | Unifies names from inputs |
| [`Tensor.atan2_()`](generated/torch.Tensor.atan2_.html#torch.Tensor.atan2_) | Unifies names from inputs |
| [`Tensor.atan_()`](generated/torch.Tensor.atan_.html#torch.Tensor.atan_) | Keeps input names |
| [`Tensor.bernoulli()`](generated/torch.Tensor.bernoulli.html#torch.Tensor.bernoulli), [`torch.bernoulli()`](generated/torch.bernoulli.html#torch.bernoulli) | Keeps input names |
| [`Tensor.bernoulli_()`](generated/torch.Tensor.bernoulli_.html#torch.Tensor.bernoulli_) | None |
| [`Tensor.bfloat16()`](generated/torch.Tensor.bfloat16.html#torch.Tensor.bfloat16) | Keeps input names |
| [`Tensor.bitwise_not()`](generated/torch.Tensor.bitwise_not.html#torch.Tensor.bitwise_not), [`torch.bitwise_not()`](generated/torch.bitwise_not.html#torch.bitwise_not) | Keeps input names |
| [`Tensor.bitwise_not_()`](generated/torch.Tensor.bitwise_not_.html#torch.Tensor.bitwise_not_) | None |
| [`Tensor.bmm()`](generated/torch.Tensor.bmm.html#torch.Tensor.bmm), [`torch.bmm()`](generated/torch.bmm.html#torch.bmm) | Contracts away dims |
| [`Tensor.bool()`](generated/torch.Tensor.bool.html#torch.Tensor.bool) | Keeps input names |
| [`Tensor.byte()`](generated/torch.Tensor.byte.html#torch.Tensor.byte) | Keeps input names |
| [`torch.cat()`](generated/torch.cat.html#torch.cat) | Unifies names from inputs |
| [`Tensor.cauchy_()`](generated/torch.Tensor.cauchy_.html#torch.Tensor.cauchy_) | None |
| [`Tensor.ceil()`](generated/torch.Tensor.ceil.html#torch.Tensor.ceil), [`torch.ceil()`](generated/torch.ceil.html#torch.ceil) | Keeps input names |
| [`Tensor.ceil_()`](generated/torch.Tensor.ceil_.html#torch.Tensor.ceil_) | None |
| [`Tensor.char()`](generated/torch.Tensor.char.html#torch.Tensor.char) | Keeps input names |
| [`Tensor.chunk()`](generated/torch.Tensor.chunk.html#torch.Tensor.chunk), [`torch.chunk()`](generated/torch.chunk.html#torch.chunk) | Keeps input names |
| [`Tensor.clamp()`](generated/torch.Tensor.clamp.html#torch.Tensor.clamp), [`torch.clamp()`](generated/torch.clamp.html#torch.clamp) | Keeps input names |
| [`Tensor.clamp_()`](generated/torch.Tensor.clamp_.html#torch.Tensor.clamp_) | None |
| [`Tensor.copy_()`](generated/torch.Tensor.copy_.html#torch.Tensor.copy_) | out function and in-place variants |
| [`Tensor.cos()`](generated/torch.Tensor.cos.html#torch.Tensor.cos), [`torch.cos()`](generated/torch.cos.html#torch.cos) | Keeps input names |
| [`Tensor.cos_()`](generated/torch.Tensor.cos_.html#torch.Tensor.cos_) | None |
| [`Tensor.cosh()`](generated/torch.Tensor.cosh.html#torch.Tensor.cosh), [`torch.cosh()`](generated/torch.cosh.html#torch.cosh) | Keeps input names |
| [`Tensor.cosh_()`](generated/torch.Tensor.cosh_.html#torch.Tensor.cosh_) | None |
| [`Tensor.acosh()`](generated/torch.Tensor.acosh.html#torch.Tensor.acosh), [`torch.acosh()`](generated/torch.acosh.html#torch.acosh) | Keeps input names |
| [`Tensor.acosh_()`](generated/torch.Tensor.acosh_.html#torch.Tensor.acosh_) | None |
| [`Tensor.cpu()`](generated/torch.Tensor.cpu.html#torch.Tensor.cpu) | Keeps input names |
| [`Tensor.cuda()`](generated/torch.Tensor.cuda.html#torch.Tensor.cuda) | Keeps input names |
| [`Tensor.cumprod()`](generated/torch.Tensor.cumprod.html#torch.Tensor.cumprod), [`torch.cumprod()`](generated/torch.cumprod.html#torch.cumprod) | Keeps input names |
| [`Tensor.cumsum()`](generated/torch.Tensor.cumsum.html#torch.Tensor.cumsum), [`torch.cumsum()`](generated/torch.cumsum.html#torch.cumsum) | Keeps input names |
| [`Tensor.data_ptr()`](generated/torch.Tensor.data_ptr.html#torch.Tensor.data_ptr) | None |
| [`Tensor.deg2rad()`](generated/torch.Tensor.deg2rad.html#torch.Tensor.deg2rad), [`torch.deg2rad()`](generated/torch.deg2rad.html#torch.deg2rad) | Keeps input names |
| `Tensor.deg2rad_()` | None |
| [`Tensor.detach()`](generated/torch.Tensor.detach.html#torch.Tensor.detach), [`torch.detach()`](generated/torch.detach.html#torch.detach) | Keeps input names |
| [`Tensor.detach_()`](generated/torch.Tensor.detach_.html#torch.Tensor.detach_) | None |
| [`Tensor.device`](generated/torch.Tensor.device.html#torch.Tensor.device), [`torch.device()`](tensor_attributes.html#torch.device) | None |
| [`Tensor.digamma()`](generated/torch.Tensor.digamma.html#torch.Tensor.digamma), [`torch.digamma()`](generated/torch.digamma.html#torch.digamma) | Keeps input names |
| [`Tensor.digamma_()`](generated/torch.Tensor.digamma_.html#torch.Tensor.digamma_) | None |
| [`Tensor.dim()`](generated/torch.Tensor.dim.html#torch.Tensor.dim) | None |
| [`Tensor.div()`](generated/torch.Tensor.div.html#torch.Tensor.div), [`torch.div()`](generated/torch.div.html#torch.div) | Unifies names from inputs |
| [`Tensor.div_()`](generated/torch.Tensor.div_.html#torch.Tensor.div_) | Unifies names from inputs |
| [`Tensor.dot()`](generated/torch.Tensor.dot.html#torch.Tensor.dot), [`torch.dot()`](generated/torch.dot.html#torch.dot) | None |
| [`Tensor.double()`](generated/torch.Tensor.double.html#torch.Tensor.double) | Keeps input names |
| [`Tensor.element_size()`](generated/torch.Tensor.element_size.html#torch.Tensor.element_size) | None |
| [`torch.empty()`](generated/torch.empty.html#torch.empty) | Factory functions |
| [`torch.empty_like()`](generated/torch.empty_like.html#torch.empty_like) | Factory functions |
| [`Tensor.eq()`](generated/torch.Tensor.eq.html#torch.Tensor.eq), [`torch.eq()`](generated/torch.eq.html#torch.eq) | Unifies names from inputs |
| [`Tensor.erf()`](generated/torch.Tensor.erf.html#torch.Tensor.erf), [`torch.erf()`](generated/torch.erf.html#torch.erf) | Keeps input names |
| [`Tensor.erf_()`](generated/torch.Tensor.erf_.html#torch.Tensor.erf_) | None |
| [`Tensor.erfc()`](generated/torch.Tensor.erfc.html#torch.Tensor.erfc), [`torch.erfc()`](generated/torch.erfc.html#torch.erfc) | Keeps input names |
| [`Tensor.erfc_()`](generated/torch.Tensor.erfc_.html#torch.Tensor.erfc_) | None |
| [`Tensor.erfinv()`](generated/torch.Tensor.erfinv.html#torch.Tensor.erfinv), [`torch.erfinv()`](generated/torch.erfinv.html#torch.erfinv) | Keeps input names |
| [`Tensor.erfinv_()`](generated/torch.Tensor.erfinv_.html#torch.Tensor.erfinv_) | None |
| [`Tensor.exp()`](generated/torch.Tensor.exp.html#torch.Tensor.exp), [`torch.exp()`](generated/torch.exp.html#torch.exp) | Keeps input names |
| [`Tensor.exp_()`](generated/torch.Tensor.exp_.html#torch.Tensor.exp_) | None |
| [`Tensor.expand()`](generated/torch.Tensor.expand.html#torch.Tensor.expand) | Keeps input names |
| [`Tensor.expm1()`](generated/torch.Tensor.expm1.html#torch.Tensor.expm1), [`torch.expm1()`](generated/torch.expm1.html#torch.expm1) | Keeps input names |
| [`Tensor.expm1_()`](generated/torch.Tensor.expm1_.html#torch.Tensor.expm1_) | None |
| [`Tensor.exponential_()`](generated/torch.Tensor.exponential_.html#torch.Tensor.exponential_) | None |
| [`Tensor.fill_()`](generated/torch.Tensor.fill_.html#torch.Tensor.fill_) | None |
| [`Tensor.flatten()`](generated/torch.Tensor.flatten.html#torch.Tensor.flatten), [`torch.flatten()`](generated/torch.flatten.html#torch.flatten) | See documentation |
| [`Tensor.float()`](generated/torch.Tensor.float.html#torch.Tensor.float) | Keeps input names |
| [`Tensor.floor()`](generated/torch.Tensor.floor.html#torch.Tensor.floor), [`torch.floor()`](generated/torch.floor.html#torch.floor) | Keeps input names |
| [`Tensor.floor_()`](generated/torch.Tensor.floor_.html#torch.Tensor.floor_) | None |
| [`Tensor.frac()`](generated/torch.Tensor.frac.html#torch.Tensor.frac), [`torch.frac()`](generated/torch.frac.html#torch.frac) | Keeps input names |
| [`Tensor.frac_()`](generated/torch.Tensor.frac_.html#torch.Tensor.frac_) | None |
| [`Tensor.ge()`](generated/torch.Tensor.ge.html#torch.Tensor.ge), [`torch.ge()`](generated/torch.ge.html#torch.ge) | Unifies names from inputs |
| [`Tensor.get_device()`](generated/torch.Tensor.get_device.html#torch.Tensor.get_device), [`torch.get_device()`](generated/torch.get_device.html#torch.get_device) | None |
| [`Tensor.grad`](generated/torch.Tensor.grad.html#torch.Tensor.grad) | None |
| [`Tensor.gt()`](generated/torch.Tensor.gt.html#torch.Tensor.gt), [`torch.gt()`](generated/torch.gt.html#torch.gt) | Unifies names from inputs |
| [`Tensor.half()`](generated/torch.Tensor.half.html#torch.Tensor.half) | Keeps input names |
| `Tensor.has_names()` | See documentation |
| [`Tensor.index_fill()`](generated/torch.Tensor.index_fill.html#torch.Tensor.index_fill), `torch.index_fill()` | Keeps input names |
| [`Tensor.index_fill_()`](generated/torch.Tensor.index_fill_.html#torch.Tensor.index_fill_) | None |
| [`Tensor.int()`](generated/torch.Tensor.int.html#torch.Tensor.int) | Keeps input names |
| [`Tensor.is_contiguous()`](generated/torch.Tensor.is_contiguous.html#torch.Tensor.is_contiguous) | None |
| [`Tensor.is_cuda`](generated/torch.Tensor.is_cuda.html#torch.Tensor.is_cuda) | None |
| [`Tensor.is_floating_point()`](generated/torch.Tensor.is_floating_point.html#torch.Tensor.is_floating_point), [`torch.is_floating_point()`](generated/torch.is_floating_point.html#torch.is_floating_point) | None |
| [`Tensor.is_leaf`](generated/torch.Tensor.is_leaf.html#torch.Tensor.is_leaf) | None |
| [`Tensor.is_pinned()`](generated/torch.Tensor.is_pinned.html#torch.Tensor.is_pinned) | None |
| [`Tensor.is_shared()`](generated/torch.Tensor.is_shared.html#torch.Tensor.is_shared) | None |
| [`Tensor.is_signed()`](generated/torch.Tensor.is_signed.html#torch.Tensor.is_signed), [`torch.is_signed()`](generated/torch.is_signed.html#torch.is_signed) | None |
| [`Tensor.is_sparse`](generated/torch.Tensor.is_sparse.html#torch.Tensor.is_sparse) | None |
| [`Tensor.is_sparse_csr`](generated/torch.Tensor.is_sparse_csr.html#torch.Tensor.is_sparse_csr) | None |
| [`torch.is_tensor()`](generated/torch.is_tensor.html#torch.is_tensor) | None |
| [`Tensor.item()`](generated/torch.Tensor.item.html#torch.Tensor.item) | None |
| [`Tensor.itemsize`](generated/torch.Tensor.itemsize.html#torch.Tensor.itemsize) | None |
| [`Tensor.kthvalue()`](generated/torch.Tensor.kthvalue.html#torch.Tensor.kthvalue), [`torch.kthvalue()`](generated/torch.kthvalue.html#torch.kthvalue) | Removes dimensions |
| [`Tensor.le()`](generated/torch.Tensor.le.html#torch.Tensor.le), [`torch.le()`](generated/torch.le.html#torch.le) | Unifies names from inputs |
| [`Tensor.log()`](generated/torch.Tensor.log.html#torch.Tensor.log), [`torch.log()`](generated/torch.log.html#torch.log) | Keeps input names |
| [`Tensor.log10()`](generated/torch.Tensor.log10.html#torch.Tensor.log10), [`torch.log10()`](generated/torch.log10.html#torch.log10) | Keeps input names |
| [`Tensor.log10_()`](generated/torch.Tensor.log10_.html#torch.Tensor.log10_) | None |
| [`Tensor.log1p()`](generated/torch.Tensor.log1p.html#torch.Tensor.log1p), [`torch.log1p()`](generated/torch.log1p.html#torch.log1p) | Keeps input names |
| [`Tensor.log1p_()`](generated/torch.Tensor.log1p_.html#torch.Tensor.log1p_) | None |
| [`Tensor.log2()`](generated/torch.Tensor.log2.html#torch.Tensor.log2), [`torch.log2()`](generated/torch.log2.html#torch.log2) | Keeps input names |
| [`Tensor.log2_()`](generated/torch.Tensor.log2_.html#torch.Tensor.log2_) | None |
| [`Tensor.log_()`](generated/torch.Tensor.log_.html#torch.Tensor.log_) | None |
| [`Tensor.log_normal_()`](generated/torch.Tensor.log_normal_.html#torch.Tensor.log_normal_) | None |
| [`Tensor.logical_not()`](generated/torch.Tensor.logical_not.html#torch.Tensor.logical_not), [`torch.logical_not()`](generated/torch.logical_not.html#torch.logical_not) | Keeps input names |
| [`Tensor.logical_not_()`](generated/torch.Tensor.logical_not_.html#torch.Tensor.logical_not_) | None |
| [`Tensor.logsumexp()`](generated/torch.Tensor.logsumexp.html#torch.Tensor.logsumexp), [`torch.logsumexp()`](generated/torch.logsumexp.html#torch.logsumexp) | Removes dimensions |
| [`Tensor.long()`](generated/torch.Tensor.long.html#torch.Tensor.long) | Keeps input names |
| [`Tensor.lt()`](generated/torch.Tensor.lt.html#torch.Tensor.lt), [`torch.lt()`](generated/torch.lt.html#torch.lt) | Unifies names from inputs |
| [`torch.manual_seed()`](generated/torch.manual_seed.html#torch.manual_seed) | None |
| [`Tensor.masked_fill()`](generated/torch.Tensor.masked_fill.html#torch.Tensor.masked_fill), [`torch.masked_fill()`](generated/torch.masked_fill.html#torch.masked_fill) | Keeps input names |
| [`Tensor.masked_fill_()`](generated/torch.Tensor.masked_fill_.html#torch.Tensor.masked_fill_) | None |
| [`Tensor.masked_select()`](generated/torch.Tensor.masked_select.html#torch.Tensor.masked_select), [`torch.masked_select()`](generated/torch.masked_select.html#torch.masked_select) | Aligns mask up to input and then unifies_names_from_input_tensors |
| [`Tensor.matmul()`](generated/torch.Tensor.matmul.html#torch.Tensor.matmul), [`torch.matmul()`](generated/torch.matmul.html#torch.matmul) | Contracts away dims |
| [`Tensor.mean()`](generated/torch.Tensor.mean.html#torch.Tensor.mean), [`torch.mean()`](generated/torch.mean.html#torch.mean) | Removes dimensions |
| [`Tensor.median()`](generated/torch.Tensor.median.html#torch.Tensor.median), [`torch.median()`](generated/torch.median.html#torch.median) | Removes dimensions |
| [`Tensor.nanmedian()`](generated/torch.Tensor.nanmedian.html#torch.Tensor.nanmedian), [`torch.nanmedian()`](generated/torch.nanmedian.html#torch.nanmedian) | Removes dimensions |
| [`Tensor.mm()`](generated/torch.Tensor.mm.html#torch.Tensor.mm), [`torch.mm()`](generated/torch.mm.html#torch.mm) | Contracts away dims |
| [`Tensor.mode()`](generated/torch.Tensor.mode.html#torch.Tensor.mode), [`torch.mode()`](generated/torch.mode.html#torch.mode) | Removes dimensions |
| [`Tensor.mul()`](generated/torch.Tensor.mul.html#torch.Tensor.mul), [`torch.mul()`](generated/torch.mul.html#torch.mul) | Unifies names from inputs |
| [`Tensor.mul_()`](generated/torch.Tensor.mul_.html#torch.Tensor.mul_) | Unifies names from inputs |
| [`Tensor.mv()`](generated/torch.Tensor.mv.html#torch.Tensor.mv), [`torch.mv()`](generated/torch.mv.html#torch.mv) | Contracts away dims |
| [`Tensor.names`](named_tensor.html#torch.Tensor.names) | See documentation |
| [`Tensor.narrow()`](generated/torch.Tensor.narrow.html#torch.Tensor.narrow), [`torch.narrow()`](generated/torch.narrow.html#torch.narrow) | Keeps input names |
| [`Tensor.nbytes`](generated/torch.Tensor.nbytes.html#torch.Tensor.nbytes) | None |
| [`Tensor.ndim`](generated/torch.Tensor.ndim.html#torch.Tensor.ndim) | None |
| [`Tensor.ndimension()`](generated/torch.Tensor.ndimension.html#torch.Tensor.ndimension) | None |
| [`Tensor.ne()`](generated/torch.Tensor.ne.html#torch.Tensor.ne), [`torch.ne()`](generated/torch.ne.html#torch.ne) | Unifies names from inputs |
| [`Tensor.neg()`](generated/torch.Tensor.neg.html#torch.Tensor.neg), [`torch.neg()`](generated/torch.neg.html#torch.neg) | Keeps input names |
| [`Tensor.neg_()`](generated/torch.Tensor.neg_.html#torch.Tensor.neg_) | None |
| [`torch.normal()`](generated/torch.normal.html#torch.normal) | Keeps input names |
| [`Tensor.normal_()`](generated/torch.Tensor.normal_.html#torch.Tensor.normal_) | None |
| [`Tensor.numel()`](generated/torch.Tensor.numel.html#torch.Tensor.numel), [`torch.numel()`](generated/torch.numel.html#torch.numel) | None |
| [`torch.ones()`](generated/torch.ones.html#torch.ones) | Factory functions |
| [`Tensor.pow()`](generated/torch.Tensor.pow.html#torch.Tensor.pow), [`torch.pow()`](generated/torch.pow.html#torch.pow) | Unifies names from inputs |
| [`Tensor.pow_()`](generated/torch.Tensor.pow_.html#torch.Tensor.pow_) | None |
| [`Tensor.prod()`](generated/torch.Tensor.prod.html#torch.Tensor.prod), [`torch.prod()`](generated/torch.prod.html#torch.prod) | Removes dimensions |
| [`Tensor.rad2deg()`](generated/torch.Tensor.rad2deg.html#torch.Tensor.rad2deg), [`torch.rad2deg()`](generated/torch.rad2deg.html#torch.rad2deg) | Keeps input names |
| `Tensor.rad2deg_()` | None |
| [`torch.rand()`](generated/torch.rand.html#torch.rand) | Factory functions |
| [`torch.rand()`](generated/torch.rand.html#torch.rand) | Factory functions |
| [`torch.randn()`](generated/torch.randn.html#torch.randn) | Factory functions |
| [`torch.randn()`](generated/torch.randn.html#torch.randn) | Factory functions |
| [`Tensor.random_()`](generated/torch.Tensor.random_.html#torch.Tensor.random_) | None |
| [`Tensor.reciprocal()`](generated/torch.Tensor.reciprocal.html#torch.Tensor.reciprocal), [`torch.reciprocal()`](generated/torch.reciprocal.html#torch.reciprocal) | Keeps input names |
| [`Tensor.reciprocal_()`](generated/torch.Tensor.reciprocal_.html#torch.Tensor.reciprocal_) | None |
| [`Tensor.refine_names()`](named_tensor.html#torch.Tensor.refine_names) | See documentation |
| [`Tensor.register_hook()`](generated/torch.Tensor.register_hook.html#torch.Tensor.register_hook) | None |
| [`Tensor.register_post_accumulate_grad_hook()`](generated/torch.Tensor.register_post_accumulate_grad_hook.html#torch.Tensor.register_post_accumulate_grad_hook) | None |
| [`Tensor.rename()`](named_tensor.html#torch.Tensor.rename) | See documentation |
| [`Tensor.rename_()`](named_tensor.html#torch.Tensor.rename_) | See documentation |
| [`Tensor.requires_grad`](generated/torch.Tensor.requires_grad.html#torch.Tensor.requires_grad) | None |
| [`Tensor.requires_grad_()`](generated/torch.Tensor.requires_grad_.html#torch.Tensor.requires_grad_) | None |
| [`Tensor.resize_()`](generated/torch.Tensor.resize_.html#torch.Tensor.resize_) | Only allow resizes that do not change shape |
| [`Tensor.resize_as_()`](generated/torch.Tensor.resize_as_.html#torch.Tensor.resize_as_) | Only allow resizes that do not change shape |
| [`Tensor.round()`](generated/torch.Tensor.round.html#torch.Tensor.round), [`torch.round()`](generated/torch.round.html#torch.round) | Keeps input names |
| [`Tensor.round_()`](generated/torch.Tensor.round_.html#torch.Tensor.round_) | None |
| [`Tensor.rsqrt()`](generated/torch.Tensor.rsqrt.html#torch.Tensor.rsqrt), [`torch.rsqrt()`](generated/torch.rsqrt.html#torch.rsqrt) | Keeps input names |
| [`Tensor.rsqrt_()`](generated/torch.Tensor.rsqrt_.html#torch.Tensor.rsqrt_) | None |
| [`Tensor.select()`](generated/torch.Tensor.select.html#torch.Tensor.select), [`torch.select()`](generated/torch.select.html#torch.select) | Removes dimensions |
| [`Tensor.short()`](generated/torch.Tensor.short.html#torch.Tensor.short) | Keeps input names |
| [`Tensor.sigmoid()`](generated/torch.Tensor.sigmoid.html#torch.Tensor.sigmoid), [`torch.sigmoid()`](generated/torch.sigmoid.html#torch.sigmoid) | Keeps input names |
| [`Tensor.sigmoid_()`](generated/torch.Tensor.sigmoid_.html#torch.Tensor.sigmoid_) | None |
| [`Tensor.sign()`](generated/torch.Tensor.sign.html#torch.Tensor.sign), [`torch.sign()`](generated/torch.sign.html#torch.sign) | Keeps input names |
| [`Tensor.sign_()`](generated/torch.Tensor.sign_.html#torch.Tensor.sign_) | None |
| [`Tensor.sgn()`](generated/torch.Tensor.sgn.html#torch.Tensor.sgn), [`torch.sgn()`](generated/torch.sgn.html#torch.sgn) | Keeps input names |
| [`Tensor.sgn_()`](generated/torch.Tensor.sgn_.html#torch.Tensor.sgn_) | None |
| [`Tensor.sin()`](generated/torch.Tensor.sin.html#torch.Tensor.sin), [`torch.sin()`](generated/torch.sin.html#torch.sin) | Keeps input names |
| [`Tensor.sin_()`](generated/torch.Tensor.sin_.html#torch.Tensor.sin_) | None |
| [`Tensor.sinh()`](generated/torch.Tensor.sinh.html#torch.Tensor.sinh), [`torch.sinh()`](generated/torch.sinh.html#torch.sinh) | Keeps input names |
| [`Tensor.sinh_()`](generated/torch.Tensor.sinh_.html#torch.Tensor.sinh_) | None |
| [`Tensor.asinh()`](generated/torch.Tensor.asinh.html#torch.Tensor.asinh), [`torch.asinh()`](generated/torch.asinh.html#torch.asinh) | Keeps input names |
| [`Tensor.asinh_()`](generated/torch.Tensor.asinh_.html#torch.Tensor.asinh_) | None |
| [`Tensor.size()`](generated/torch.Tensor.size.html#torch.Tensor.size) | None |
| [`Tensor.softmax()`](generated/torch.Tensor.softmax.html#torch.Tensor.softmax), [`torch.softmax()`](generated/torch.softmax.html#torch.softmax) | Keeps input names |
| [`Tensor.split()`](generated/torch.Tensor.split.html#torch.Tensor.split), [`torch.split()`](generated/torch.split.html#torch.split) | Keeps input names |
| [`Tensor.sqrt()`](generated/torch.Tensor.sqrt.html#torch.Tensor.sqrt), [`torch.sqrt()`](generated/torch.sqrt.html#torch.sqrt) | Keeps input names |
| [`Tensor.sqrt_()`](generated/torch.Tensor.sqrt_.html#torch.Tensor.sqrt_) | None |
| [`Tensor.squeeze()`](generated/torch.Tensor.squeeze.html#torch.Tensor.squeeze), [`torch.squeeze()`](generated/torch.squeeze.html#torch.squeeze) | Removes dimensions |
| [`Tensor.std()`](generated/torch.Tensor.std.html#torch.Tensor.std), [`torch.std()`](generated/torch.std.html#torch.std) | Removes dimensions |
| [`torch.std_mean()`](generated/torch.std_mean.html#torch.std_mean) | Removes dimensions |
| [`Tensor.stride()`](generated/torch.Tensor.stride.html#torch.Tensor.stride) | None |
| [`Tensor.sub()`](generated/torch.Tensor.sub.html#torch.Tensor.sub), [`torch.sub()`](generated/torch.sub.html#torch.sub) | Unifies names from inputs |
| [`Tensor.sub_()`](generated/torch.Tensor.sub_.html#torch.Tensor.sub_) | Unifies names from inputs |
| [`Tensor.sum()`](generated/torch.Tensor.sum.html#torch.Tensor.sum), [`torch.sum()`](generated/torch.sum.html#torch.sum) | Removes dimensions |
| [`Tensor.tan()`](generated/torch.Tensor.tan.html#torch.Tensor.tan), [`torch.tan()`](generated/torch.tan.html#torch.tan) | Keeps input names |
| [`Tensor.tan_()`](generated/torch.Tensor.tan_.html#torch.Tensor.tan_) | None |
| [`Tensor.tanh()`](generated/torch.Tensor.tanh.html#torch.Tensor.tanh), [`torch.tanh()`](generated/torch.tanh.html#torch.tanh) | Keeps input names |
| [`Tensor.tanh_()`](generated/torch.Tensor.tanh_.html#torch.Tensor.tanh_) | None |
| [`Tensor.atanh()`](generated/torch.Tensor.atanh.html#torch.Tensor.atanh), [`torch.atanh()`](generated/torch.atanh.html#torch.atanh) | Keeps input names |
| [`Tensor.atanh_()`](generated/torch.Tensor.atanh_.html#torch.Tensor.atanh_) | None |
| [`torch.tensor()`](generated/torch.tensor.html#torch.tensor) | Factory functions |
| [`Tensor.to()`](generated/torch.Tensor.to.html#torch.Tensor.to) | Keeps input names |
| [`Tensor.topk()`](generated/torch.Tensor.topk.html#torch.Tensor.topk), [`torch.topk()`](generated/torch.topk.html#torch.topk) | Removes dimensions |
| [`Tensor.transpose()`](generated/torch.Tensor.transpose.html#torch.Tensor.transpose), [`torch.transpose()`](generated/torch.transpose.html#torch.transpose) | Permutes dimensions |
| [`Tensor.trunc()`](generated/torch.Tensor.trunc.html#torch.Tensor.trunc), [`torch.trunc()`](generated/torch.trunc.html#torch.trunc) | Keeps input names |
| [`Tensor.trunc_()`](generated/torch.Tensor.trunc_.html#torch.Tensor.trunc_) | None |
| [`Tensor.type()`](generated/torch.Tensor.type.html#torch.Tensor.type) | None |
| [`Tensor.type_as()`](generated/torch.Tensor.type_as.html#torch.Tensor.type_as) | Keeps input names |
| [`Tensor.unbind()`](generated/torch.Tensor.unbind.html#torch.Tensor.unbind), [`torch.unbind()`](generated/torch.unbind.html#torch.unbind) | Removes dimensions |
| [`Tensor.unflatten()`](generated/torch.Tensor.unflatten.html#torch.Tensor.unflatten) | See documentation |
| [`Tensor.uniform_()`](generated/torch.Tensor.uniform_.html#torch.Tensor.uniform_) | None |
| [`Tensor.var()`](generated/torch.Tensor.var.html#torch.Tensor.var), [`torch.var()`](generated/torch.var.html#torch.var) | Removes dimensions |
| [`torch.var_mean()`](generated/torch.var_mean.html#torch.var_mean) | Removes dimensions |
| [`Tensor.zero_()`](generated/torch.Tensor.zero_.html#torch.Tensor.zero_) | None |
| [`torch.zeros()`](generated/torch.zeros.html#torch.zeros) | Factory functions |

## Keeps input names

All pointwise unary functions follow this rule as well as some other unary functions.

- Check names: None
- Propagate names: input tensor's names are propagated to the output.

```
>>> x = torch.randn(3, 3, names=('N', 'C'))
>>> x.abs().names
('N', 'C')
```

## Removes dimensions

All reduction ops like [`sum()`](generated/torch.Tensor.sum.html#torch.Tensor.sum) remove dimensions by reducing
over the desired dimensions. Other operations like [`select()`](generated/torch.Tensor.select.html#torch.Tensor.select) and
[`squeeze()`](generated/torch.Tensor.squeeze.html#torch.Tensor.squeeze) remove dimensions.

Wherever one can pass an integer dimension index to an operator, one can also pass
a dimension name. Functions that take lists of dimension indices can also take in a
list of dimension names.

- Check names: If `dim` or `dims` is passed in as a list of names,
check that those names exist in `self`.
- Propagate names: If the dimensions of the input tensor specified by `dim`
or `dims` are not present in the output tensor, then the corresponding names
of those dimensions do not appear in `output.names`.

```
>>> x = torch.randn(1, 3, 3, 3, names=('N', 'C', 'H', 'W'))
>>> x.squeeze('N').names
('C', 'H', 'W')

>>> x = torch.randn(3, 3, 3, 3, names=('N', 'C', 'H', 'W'))
>>> x.sum(['N', 'C']).names
('H', 'W')

# Reduction ops with keepdim=True don't actually remove dimensions.
>>> x = torch.randn(3, 3, 3, 3, names=('N', 'C', 'H', 'W'))
>>> x.sum(['N', 'C'], keepdim=True).names
('N', 'C', 'H', 'W')
```

## Unifies names from inputs

All binary arithmetic ops follow this rule. Operations that broadcast still
broadcast positionally from the right to preserve compatibility with unnamed
tensors. To perform explicit broadcasting by names, use [`Tensor.align_as()`](named_tensor.html#torch.Tensor.align_as).

- Check names: All names must match positionally from the right. i.e., in
`tensor + other`, `match(tensor.names[i], other.names[i])` must be true for all
`i` in `(-min(tensor.dim(), other.dim()) + 1, -1]`.
- Check names: Furthermore, all named dimensions must be aligned from the right.
During matching, if we match a named dimension `A` with an unnamed dimension
`None`, then `A` must not appear in the tensor with the unnamed dimension.
- Propagate names: unify pairs of names from the right from both tensors to
produce output names.

For example,

```
# tensor: Tensor[ N, None]
# other: Tensor[None, C]
>>> tensor = torch.randn(3, 3, names=('N', None))
>>> other = torch.randn(3, 3, names=(None, 'C'))
>>> (tensor + other).names
('N', 'C')
```

Check names:

- `match(tensor.names[-1], other.names[-1])` is `True`
- `match(tensor.names[-2], tensor.names[-2])` is `True`
- Because we matched `None` in [`tensor`](generated/torch.tensor.html#torch.tensor) with `'C'`,
check to make sure `'C'` doesn't exist in [`tensor`](generated/torch.tensor.html#torch.tensor) (it does not).
- Check to make sure `'N'` doesn't exists in `other` (it does not).

Finally, the output names are computed with
`[unify('N', None), unify(None, 'C')] = ['N', 'C']`

More examples:

```
# Dimensions don't match from the right:
# tensor: Tensor[N, C]
# other: Tensor[ N]
>>> tensor = torch.randn(3, 3, names=('N', 'C'))
>>> other = torch.randn(3, names=('N',))
>>> (tensor + other).names
RuntimeError: Error when attempting to broadcast dims ['N', 'C'] and dims
['N']: dim 'C' and dim 'N' are at the same position from the right but do
not match.

# Dimensions aren't aligned when matching tensor.names[-1] and other.names[-1]:
# tensor: Tensor[N, None]
# other: Tensor[ N]
>>> tensor = torch.randn(3, 3, names=('N', None))
>>> other = torch.randn(3, names=('N',))
>>> (tensor + other).names
RuntimeError: Misaligned dims when attempting to broadcast dims ['N'] and
dims ['N', None]: dim 'N' appears in a different position from the right
across both lists.
```

Note

In both of the last examples, it is possible to align the tensors by names
and then perform the addition. Use [`Tensor.align_as()`](named_tensor.html#torch.Tensor.align_as) to align
tensors by name or [`Tensor.align_to()`](named_tensor.html#torch.Tensor.align_to) to align tensors to a custom
dimension ordering.

## Permutes dimensions

Some operations, like [`Tensor.t()`](generated/torch.Tensor.t.html#torch.Tensor.t), permute the order of dimensions. Dimension names
are attached to individual dimensions so they get permuted as well.

If the operator takes in positional index `dim`, it is also able to take a dimension
name as `dim`.

- Check names: If `dim` is passed as a name, check that it exists in the tensor.
- Propagate names: Permute dimension names in the same way as the dimensions that are
being permuted.

```
>>> x = torch.randn(3, 3, names=('N', 'C'))
>>> x.transpose('N', 'C').names
('C', 'N')
```

## Contracts away dims

Matrix multiply functions follow some variant of this. Let's go through
[`torch.mm()`](generated/torch.mm.html#torch.mm) first and then generalize the rule for batch matrix multiplication.

For `torch.mm(tensor, other)`:

- Check names: None
- Propagate names: result names are `(tensor.names[-2], other.names[-1])`.

```
>>> x = torch.randn(3, 3, names=('N', 'D'))
>>> y = torch.randn(3, 3, names=('in', 'out'))
>>> x.mm(y).names
('N', 'out')
```

Inherently, a matrix multiplication performs a dot product over two dimensions,
collapsing them. When two tensors are matrix-multiplied, the contracted dimensions
disappear and do not show up in the output tensor.

[`torch.mv()`](generated/torch.mv.html#torch.mv), [`torch.dot()`](generated/torch.dot.html#torch.dot) work in a similar way: name inference does not
check input names and removes the dimensions that are involved in the dot product:

```
>>> x = torch.randn(3, 3, names=('N', 'D'))
>>> y = torch.randn(3, names=('something',))
>>> x.mv(y).names
('N',)
```

Now, let's take a look at `torch.matmul(tensor, other)`. Assume that `tensor.dim() >= 2`
and `other.dim() >= 2`.

- Check names: Check that the batch dimensions of the inputs are aligned and broadcastable.
See Unifies names from inputs for what it means for the inputs to be aligned.
- Propagate names: result names are obtained by unifying the batch dimensions and removing
the contracted dimensions:
`unify(tensor.names[:-2], other.names[:-2]) + (tensor.names[-2], other.names[-1])`.

Examples:

```
# Batch matrix multiply of matrices Tensor['C', 'D'] and Tensor['E', 'F'].
# 'A', 'B' are batch dimensions.
>>> x = torch.randn(3, 3, 3, 3, names=('A', 'B', 'C', 'D'))
>>> y = torch.randn(3, 3, 3, names=('B', 'E', 'F'))
>>> torch.matmul(x, y).names
('A', 'B', 'C', 'F')
```

Finally, there are fused `add` versions of many matmul functions. i.e., [`addmm()`](generated/torch.addmm.html#torch.addmm)
and [`addmv()`](generated/torch.addmv.html#torch.addmv). These are treated as composing name inference for i.e. [`mm()`](generated/torch.mm.html#torch.mm) and
name inference for [`add()`](generated/torch.add.html#torch.add).

## Factory functions

Factory functions now take a new `names` argument that associates a name
with each dimension.

```
>>> torch.zeros(2, 3, names=('N', 'C'))
tensor([[0., 0., 0.],
 [0., 0., 0.]], names=('N', 'C'))
```

## out function and in-place variants

A tensor specified as an `out=` tensor has the following behavior:

- If it has no named dimensions, then the names computed from the operation
get propagated to it.
- If it has any named dimensions, then the names computed from the operation
must be exactly equal to the existing names. Otherwise, the operation errors.

All in-place methods modify inputs to have names equal to the computed names
from name inference. For example:

```
>>> x = torch.randn(3, 3)
>>> y = torch.randn(3, 3, names=('N', 'C'))
>>> x.names
(None, None)

>>> x += y
>>> x.names
('N', 'C')
```