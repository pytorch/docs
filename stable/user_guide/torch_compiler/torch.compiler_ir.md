# IRs

PyTorch 2.0 offers two set of IRs for backends to interface with: Core Aten IR and Prims IR.

## Core Aten IR

Core aten ops is the core subset of aten operators that can be used to compose other operators.
Core aten IR is fully functional, and there is no `inplace` or `_out` variants in this opset.
In contrast to Prims IR, core aten ops reuses the existing aten ops in "native_functions.yaml",
and it doesn't further decompose ops into explicit type promotion and broadcasting ops.
This opset is designed to serve as the functional IR to interface with backends.

Warning

This opset is still under active development, more ops will be added in the future.

| Operator | Schema |
| --- | --- |
| `aten._adaptive_avg_pool2d` | _adaptive_avg_pool2d(Tensor self, SymInt[2] output_size) -> Tensor |
| `aten._adaptive_avg_pool2d_backward` | _adaptive_avg_pool2d_backward(Tensor grad_output, Tensor self) -> Tensor |
| `aten._adaptive_avg_pool3d` | _adaptive_avg_pool3d(Tensor self, SymInt[3] output_size) -> Tensor |
| `aten._cdist_forward` | _cdist_forward(Tensor x1, Tensor x2, float p, int? compute_mode) -> Tensor |
| `aten._embedding_bag` | _embedding_bag(Tensor weight, Tensor indices, Tensor offsets, bool scale_grad_by_freq=False, int mode=0, bool sparse=False, Tensor? per_sample_weights=None, bool include_last_offset=False, int padding_idx=-1) -> (Tensor, Tensor, Tensor, Tensor) |
| `aten._fft_c2r` | _fft_c2r(Tensor self, int[] dim, int normalization, SymInt last_dim_size) -> Tensor |
| `aten._fft_r2c` | _fft_r2c(Tensor self, int[] dim, int normalization, bool onesided) -> Tensor |
| `aten._local_scalar_dense` | _local_scalar_dense(Tensor self) -> Scalar |
| `aten._log_softmax` | _log_softmax(Tensor self, int dim, bool half_to_float) -> Tensor |
| `aten._native_batch_norm_legit` | _native_batch_norm_legit(Tensor input, Tensor? weight, Tensor? bias, Tensor(a!) running_mean, Tensor(b!) running_var, bool training, float momentum, float eps) -> (Tensor, Tensor, Tensor) |
| `aten._native_batch_norm_legit.no_stats` | _native_batch_norm_legit.no_stats(Tensor input, Tensor? weight, Tensor? bias, bool training, float momentum, float eps) -> (Tensor, Tensor, Tensor) |
| `aten._native_batch_norm_legit_no_training` | _native_batch_norm_legit_no_training(Tensor input, Tensor? weight, Tensor? bias, Tensor running_mean, Tensor running_var, float momentum, float eps) -> (Tensor, Tensor, Tensor) |
| `aten._pdist_forward` | _pdist_forward(Tensor self, float p=2) -> Tensor |
| `aten._softmax` | _softmax(Tensor self, int dim, bool half_to_float) -> Tensor |
| `aten._to_copy` | _to_copy(Tensor self, *, ScalarType? dtype=None, Layout? layout=None, Device? device=None, bool? pin_memory=None, bool non_blocking=False, MemoryFormat? memory_format=None) -> Tensor |
| `aten.abs` | abs(Tensor self) -> Tensor |
| `aten.acos` | acos(Tensor self) -> Tensor |
| `aten.acosh` | acosh(Tensor self) -> Tensor |
| `aten.adaptive_avg_pool1d` | adaptive_avg_pool1d(Tensor self, int[1] output_size) -> Tensor |
| `aten.add.Scalar` | add.Scalar(Tensor self, Scalar other, Scalar alpha=1) -> Tensor |
| `aten.add.Tensor` | add.Tensor(Tensor self, Tensor other, *, Scalar alpha=1) -> Tensor |
| `aten.addmm` | addmm(Tensor self, Tensor mat1, Tensor mat2, *, Scalar beta=1, Scalar alpha=1) -> Tensor |
| `aten.alias` | alias(Tensor(a) self) -> Tensor(a) |
| `aten.amax` | amax(Tensor self, int[1] dim=[], bool keepdim=False) -> Tensor |
| `aten.amin` | amin(Tensor self, int[1] dim=[], bool keepdim=False) -> Tensor |
| `aten.any` | any(Tensor self) -> Tensor |
| `aten.any.dim` | any.dim(Tensor self, int dim, bool keepdim=False) -> Tensor |
| `aten.any.dims` | any.dims(Tensor self, int[]? dim=None, bool keepdim=False) -> Tensor |
| `aten.arange.start_step` | arange.start_step(Scalar start, Scalar end, Scalar step=1, *, ScalarType? dtype=None, Layout? layout=None, Device? device=None, bool? pin_memory=None) -> Tensor |
| `aten.argmax` | argmax(Tensor self, int? dim=None, bool keepdim=False) -> Tensor |
| `aten.argmin` | argmin(Tensor self, int? dim=None, bool keepdim=False) -> Tensor |
| `aten.as_strided` | as_strided(Tensor(a) self, SymInt[] size, SymInt[] stride, SymInt? storage_offset=None) -> Tensor(a) |
| `aten.asin` | asin(Tensor self) -> Tensor |
| `aten.asinh` | asinh(Tensor self) -> Tensor |
| `aten.atan` | atan(Tensor self) -> Tensor |
| `aten.atan2` | atan2(Tensor self, Tensor other) -> Tensor |
| `aten.atan2.out` | atan2.out(Tensor self, Tensor other, *, Tensor(a!) out) -> Tensor(a!) |
| `aten.atanh` | atanh(Tensor self) -> Tensor |
| `aten.avg_pool1d` | avg_pool1d(Tensor self, int[1] kernel_size, int[1] stride=[], int[1] padding=0, bool ceil_mode=False, bool count_include_pad=True) -> Tensor |
| `aten.avg_pool2d` | avg_pool2d(Tensor self, int[2] kernel_size, int[2] stride=[], int[2] padding=0, bool ceil_mode=False, bool count_include_pad=True, int? divisor_override=None) -> Tensor |
| `aten.avg_pool2d_backward` | avg_pool2d_backward(Tensor grad_output, Tensor self, int[2] kernel_size, int[2] stride, int[2] padding, bool ceil_mode, bool count_include_pad, int? divisor_override) -> Tensor |
| `aten.avg_pool3d` | avg_pool3d(Tensor self, int[3] kernel_size, int[3] stride=[], int[3] padding=0, bool ceil_mode=False, bool count_include_pad=True, int? divisor_override=None) -> Tensor |
| `aten.bitwise_and.Scalar` | bitwise_and.Scalar(Tensor self, Scalar other) -> Tensor |
| `aten.bitwise_and.Tensor` | bitwise_and.Tensor(Tensor self, Tensor other) -> Tensor |
| `aten.bitwise_not` | bitwise_not(Tensor self) -> Tensor |
| `aten.bitwise_or.Scalar` | bitwise_or.Scalar(Tensor self, Scalar other) -> Tensor |
| `aten.bitwise_or.Tensor` | bitwise_or.Tensor(Tensor self, Tensor other) -> Tensor |
| `aten.bitwise_xor.Scalar` | bitwise_xor.Scalar(Tensor self, Scalar other) -> Tensor |
| `aten.bitwise_xor.Tensor` | bitwise_xor.Tensor(Tensor self, Tensor other) -> Tensor |
| `aten.bmm` | bmm(Tensor self, Tensor mat2) -> Tensor |
| `aten.cat` | cat(Tensor[] tensors, int dim=0) -> Tensor |
| `aten.ceil` | ceil(Tensor self) -> Tensor |
| `aten.clamp` | clamp(Tensor self, Scalar? min=None, Scalar? max=None) -> Tensor |
| `aten.clamp.Tensor` | clamp.Tensor(Tensor self, Tensor? min=None, Tensor? max=None) -> Tensor |
| `aten.clone` | clone(Tensor self, *, MemoryFormat? memory_format=None) -> Tensor |
| `aten.col2im` | col2im(Tensor self, SymInt[2] output_size, int[2] kernel_size, int[2] dilation, int[2] padding, int[2] stride) -> Tensor |
| `aten.constant_pad_nd` | constant_pad_nd(Tensor self, SymInt[] pad, Scalar value=0) -> Tensor |
| `aten.convolution` | convolution(Tensor input, Tensor weight, Tensor? bias, SymInt[] stride, SymInt[] padding, SymInt[] dilation, bool transposed, SymInt[] output_padding, SymInt groups) -> Tensor |
| `aten.convolution_backward` | convolution_backward(Tensor grad_output, Tensor input, Tensor weight, SymInt[]? bias_sizes, SymInt[] stride, SymInt[] padding, SymInt[] dilation, bool transposed, SymInt[] output_padding, SymInt groups, bool[3] output_mask) -> (Tensor, Tensor, Tensor) |
| `aten.copy` | copy(Tensor self, Tensor src, bool non_blocking=False) -> Tensor |
| `aten.cos` | cos(Tensor self) -> Tensor |
| `aten.cosh` | cosh(Tensor self) -> Tensor |
| `aten.cumsum` | cumsum(Tensor self, int dim, *, ScalarType? dtype=None) -> Tensor |
| `aten.diagonal` | diagonal(Tensor(a) self, int offset=0, int dim1=0, int dim2=1) -> Tensor(a) |
| `aten.div.Scalar` | div.Scalar(Tensor self, Scalar other) -> Tensor |
| `aten.div.Scalar_mode` | div.Scalar_mode(Tensor self, Scalar other, *, str? rounding_mode) -> Tensor |
| `aten.div.Tensor` | div.Tensor(Tensor self, Tensor other) -> Tensor |
| `aten.div.Tensor_mode` | div.Tensor_mode(Tensor self, Tensor other, *, str? rounding_mode) -> Tensor |
| `aten.elu` | elu(Tensor self, Scalar alpha=1, Scalar scale=1, Scalar input_scale=1) -> Tensor |
| `aten.embedding` | embedding(Tensor weight, Tensor indices, SymInt padding_idx=-1, bool scale_grad_by_freq=False, bool sparse=False) -> Tensor |
| `aten.embedding_dense_backward` | embedding_dense_backward(Tensor grad_output, Tensor indices, SymInt num_weights, SymInt padding_idx, bool scale_grad_by_freq) -> Tensor |
| `aten.empty.memory_format` | empty.memory_format(SymInt[] size, *, ScalarType? dtype=None, Layout? layout=None, Device? device=None, bool? pin_memory=None, MemoryFormat? memory_format=None) -> Tensor |
| `aten.empty_strided` | empty_strided(SymInt[] size, SymInt[] stride, *, ScalarType? dtype=None, Layout? layout=None, Device? device=None, bool? pin_memory=None) -> Tensor |
| `aten.eq.Scalar` | eq.Scalar(Tensor self, Scalar other) -> Tensor |
| `aten.eq.Tensor` | eq.Tensor(Tensor self, Tensor other) -> Tensor |
| `aten.erf` | erf(Tensor self) -> Tensor |
| `aten.exp` | exp(Tensor self) -> Tensor |
| `aten.expand` | expand(Tensor(a) self, SymInt[] size, *, bool implicit=False) -> Tensor(a) |
| `aten.expm1` | expm1(Tensor self) -> Tensor |
| `aten.fill.Scalar` | fill.Scalar(Tensor self, Scalar value) -> Tensor |
| `aten.flip` | flip(Tensor self, int[] dims) -> Tensor |
| `aten.floor` | floor(Tensor self) -> Tensor |
| `aten.fmod.Scalar` | fmod.Scalar(Tensor self, Scalar other) -> Tensor |
| `aten.fmod.Tensor` | fmod.Tensor(Tensor self, Tensor other) -> Tensor |
| `aten.full` | full(SymInt[] size, Scalar fill_value, *, ScalarType? dtype=None, Layout? layout=None, Device? device=None, bool? pin_memory=None) -> Tensor |
| `aten.full_like` | full_like(Tensor self, Scalar fill_value, *, ScalarType? dtype=None, Layout? layout=None, Device? device=None, bool? pin_memory=None, MemoryFormat? memory_format=None) -> Tensor |
| `aten.gather` | gather(Tensor self, int dim, Tensor index, *, bool sparse_grad=False) -> Tensor |
| `aten.ge.Scalar` | ge.Scalar(Tensor self, Scalar other) -> Tensor |
| `aten.ge.Tensor` | ge.Tensor(Tensor self, Tensor other) -> Tensor |
| `aten.gelu` | gelu(Tensor self, *, str approximate='none') -> Tensor |
| `aten.grid_sampler_2d` | grid_sampler_2d(Tensor input, Tensor grid, int interpolation_mode, int padding_mode, bool align_corners) -> Tensor |
| `aten.gt.Scalar` | gt.Scalar(Tensor self, Scalar other) -> Tensor |
| `aten.gt.Tensor` | gt.Tensor(Tensor self, Tensor other) -> Tensor |
| `aten.hardtanh` | hardtanh(Tensor self, Scalar min_val=-1, Scalar max_val=1) -> Tensor |
| `aten.index.Tensor` | index.Tensor(Tensor self, Tensor?[] indices) -> Tensor |
| `aten.index_put` | index_put(Tensor self, Tensor?[] indices, Tensor values, bool accumulate=False) -> Tensor |
| `aten.index_select` | index_select(Tensor self, int dim, Tensor index) -> Tensor |
| `aten.isinf` | isinf(Tensor self) -> Tensor |
| `aten.isnan` | isnan(Tensor self) -> Tensor |
| `aten.le.Scalar` | le.Scalar(Tensor self, Scalar other) -> Tensor |
| `aten.le.Tensor` | le.Tensor(Tensor self, Tensor other) -> Tensor |
| `aten.leaky_relu` | leaky_relu(Tensor self, Scalar negative_slope=0.01) -> Tensor |
| `aten.log` | log(Tensor self) -> Tensor |
| `aten.log10` | log10(Tensor self) -> Tensor |
| `aten.log1p` | log1p(Tensor self) -> Tensor |
| `aten.log2` | log2(Tensor self) -> Tensor |
| `aten.logical_and` | logical_and(Tensor self, Tensor other) -> Tensor |
| `aten.logical_not` | logical_not(Tensor self) -> Tensor |
| `aten.logical_or` | logical_or(Tensor self, Tensor other) -> Tensor |
| `aten.logical_xor` | logical_xor(Tensor self, Tensor other) -> Tensor |
| `aten.lt.Scalar` | lt.Scalar(Tensor self, Scalar other) -> Tensor |
| `aten.lt.Tensor` | lt.Tensor(Tensor self, Tensor other) -> Tensor |
| `aten.masked_scatter` | masked_scatter(Tensor self, Tensor mask, Tensor source) -> Tensor |
| `aten.max.dim` | max.dim(Tensor self, int dim, bool keepdim=False) -> (Tensor values, Tensor indices) |
| `aten.max_pool2d_with_indices` | max_pool2d_with_indices(Tensor self, int[2] kernel_size, int[2] stride=[], int[2] padding=0, int[2] dilation=1, bool ceil_mode=False) -> (Tensor, Tensor) |
| `aten.max_pool2d_with_indices_backward` | max_pool2d_with_indices_backward(Tensor grad_output, Tensor self, int[2] kernel_size, int[2] stride, int[2] padding, int[2] dilation, bool ceil_mode, Tensor indices) -> Tensor |
| `aten.max_pool3d_with_indices` | max_pool3d_with_indices(Tensor self, int[3] kernel_size, int[3] stride=[], int[3] padding=0, int[3] dilation=1, bool ceil_mode=False) -> (Tensor, Tensor) |
| `aten.maximum` | maximum(Tensor self, Tensor other) -> Tensor |
| `aten.mean` | mean(Tensor self, *, ScalarType? dtype=None) -> Tensor |
| `aten.mean.dim` | mean.dim(Tensor self, int[1]? dim, bool keepdim=False, *, ScalarType? dtype=None) -> Tensor |
| `aten.min.dim` | min.dim(Tensor self, int dim, bool keepdim=False) -> (Tensor values, Tensor indices) |
| `aten.minimum` | minimum(Tensor self, Tensor other) -> Tensor |
| `aten.mm` | mm(Tensor self, Tensor mat2) -> Tensor |
| `aten.mul.Scalar` | mul.Scalar(Tensor self, Scalar other) -> Tensor |
| `aten.mul.Tensor` | mul.Tensor(Tensor self, Tensor other) -> Tensor |
| `aten.native_dropout` | native_dropout(Tensor input, float p, bool? train) -> (Tensor, Tensor) |
| `aten.native_group_norm` | native_group_norm(Tensor input, Tensor? weight, Tensor? bias, SymInt N, SymInt C, SymInt HxW, int group, float eps) -> (Tensor, Tensor, Tensor) |
| `aten.native_group_norm_backward` | native_group_norm_backward(Tensor grad_out, Tensor input, Tensor mean, Tensor rstd, Tensor? weight, SymInt N, SymInt C, SymInt HxW, int group, bool[3] output_mask) -> (Tensor, Tensor, Tensor) |
| `aten.native_layer_norm` | native_layer_norm(Tensor input, SymInt[] normalized_shape, Tensor? weight, Tensor? bias, float eps) -> (Tensor, Tensor, Tensor) |
| `aten.native_layer_norm_backward` | native_layer_norm_backward(Tensor grad_out, Tensor input, SymInt[] normalized_shape, Tensor mean, Tensor rstd, Tensor? weight, Tensor? bias, bool[3] output_mask) -> (Tensor, Tensor, Tensor) |
| `aten.ne.Scalar` | ne.Scalar(Tensor self, Scalar other) -> Tensor |
| `aten.ne.Tensor` | ne.Tensor(Tensor self, Tensor other) -> Tensor |
| `aten.neg` | neg(Tensor self) -> Tensor |
| `aten.nonzero` | nonzero(Tensor self) -> Tensor |
| `aten.permute` | permute(Tensor(a) self, int[] dims) -> Tensor(a) |
| `aten.pow.Scalar` | pow.Scalar(Scalar self, Tensor exponent) -> Tensor |
| `aten.pow.Tensor_Scalar` | pow.Tensor_Scalar(Tensor self, Scalar exponent) -> Tensor |
| `aten.pow.Tensor_Tensor` | pow.Tensor_Tensor(Tensor self, Tensor exponent) -> Tensor |
| `aten.prod` | prod(Tensor self, *, ScalarType? dtype=None) -> Tensor |
| `aten.prod.dim_int` | prod.dim_int(Tensor self, int dim, bool keepdim=False, *, ScalarType? dtype=None) -> Tensor |
| `aten.rand` | rand(SymInt[] size, *, ScalarType? dtype=None, Layout? layout=None, Device? device=None, bool? pin_memory=None) -> Tensor |
| `aten.randn` | randn(SymInt[] size, *, ScalarType? dtype=None, Layout? layout=None, Device? device=None, bool? pin_memory=None) -> Tensor |
| `aten.randperm` | randperm(SymInt n, *, ScalarType? dtype=long, Layout? layout=None, Device? device=None, bool? pin_memory=None) -> Tensor |
| `aten.reciprocal` | reciprocal(Tensor self) -> Tensor |
| `aten.reflection_pad1d` | reflection_pad1d(Tensor self, SymInt[2] padding) -> Tensor |
| `aten.reflection_pad2d` | reflection_pad2d(Tensor self, SymInt[4] padding) -> Tensor |
| `aten.reflection_pad3d` | reflection_pad3d(Tensor self, SymInt[6] padding) -> Tensor |
| `aten.relu` | relu(Tensor self) -> Tensor |
| `aten.remainder.Scalar` | remainder.Scalar(Tensor self, Scalar other) -> Tensor |
| `aten.remainder.Tensor` | remainder.Tensor(Tensor self, Tensor other) -> Tensor |
| `aten.repeat` | repeat(Tensor self, SymInt[] repeats) -> Tensor |
| `aten.replication_pad2d` | replication_pad2d(Tensor self, SymInt[4] padding) -> Tensor |
| `aten.replication_pad3d` | replication_pad3d(Tensor self, SymInt[6] padding) -> Tensor |
| `aten.resize_` | resize_(Tensor(a!) self, SymInt[] size, *, MemoryFormat? memory_format=None) -> Tensor(a!) |
| `aten.round` | round(Tensor self) -> Tensor |
| `aten.rsqrt` | rsqrt(Tensor self) -> Tensor |
| `aten.scalar_tensor` | scalar_tensor(Scalar s, *, ScalarType? dtype=None, Layout? layout=None, Device? device=None, bool? pin_memory=None) -> Tensor |
| `aten.scatter.src` | scatter.src(Tensor self, int dim, Tensor index, Tensor src) -> Tensor |
| `aten.scatter.value` | scatter.value(Tensor self, int dim, Tensor index, Scalar value) -> Tensor |
| `aten.scatter_add` | scatter_add(Tensor self, int dim, Tensor index, Tensor src) -> Tensor |
| `aten.scatter_reduce.two` | scatter_reduce.two(Tensor self, int dim, Tensor index, Tensor src, str reduce, *, bool include_self=True) -> Tensor |
| `aten.select.int` | select.int(Tensor(a) self, int dim, SymInt index) -> Tensor(a) |
| `aten.select_scatter` | select_scatter(Tensor self, Tensor src, int dim, SymInt index) -> Tensor |
| `aten.sigmoid` | sigmoid(Tensor self) -> Tensor |
| `aten.sign` | sign(Tensor self) -> Tensor |
| `aten.sin` | sin(Tensor self) -> Tensor |
| `aten.sinh` | sinh(Tensor self) -> Tensor |
| `aten.slice.Tensor` | slice.Tensor(Tensor(a) self, int dim=0, SymInt? start=None, SymInt? end=None, SymInt step=1) -> Tensor(a) |
| `aten.slice_scatter` | slice_scatter(Tensor self, Tensor src, int dim=0, SymInt? start=None, SymInt? end=None, SymInt step=1) -> Tensor |
| `aten.sort` | sort(Tensor self, int dim=-1, bool descending=False) -> (Tensor values, Tensor indices) |
| `aten.split_with_sizes` | split_with_sizes(Tensor(a -> *) self, SymInt[] split_sizes, int dim=0) -> Tensor(a)[] |
| `aten.sqrt` | sqrt(Tensor self) -> Tensor |
| `aten.squeeze.dim` | squeeze.dim(Tensor(a) self, int dim) -> Tensor(a) |
| `aten.squeeze.dims` | squeeze.dims(Tensor(a) self, int[] dim) -> Tensor(a) |
| `aten.sub.Scalar` | sub.Scalar(Tensor self, Scalar other, Scalar alpha=1) -> Tensor |
| `aten.sub.Tensor` | sub.Tensor(Tensor self, Tensor other, *, Scalar alpha=1) -> Tensor |
| `aten.sum.dim_IntList` | sum.dim_IntList(Tensor self, int[1]? dim, bool keepdim=False, *, ScalarType? dtype=None) -> Tensor |
| `aten.sym_is_contiguous` | sym_is_contiguous(Tensor self, MemoryFormat memory_format=contiguous_format) -> SymBool |
| `aten.sym_numel` | sym_numel(Tensor self) -> SymInt |
| `aten.sym_size.int` | sym_size.int(Tensor self, int dim) -> SymInt |
| `aten.sym_storage_offset` | sym_storage_offset(Tensor self) -> SymInt |
| `aten.sym_stride.int` | sym_stride.int(Tensor self, int dim) -> SymInt |
| `aten.tan` | tan(Tensor self) -> Tensor |
| `aten.tanh` | tanh(Tensor self) -> Tensor |
| `aten.topk` | topk(Tensor self, SymInt k, int dim=-1, bool largest=True, bool sorted=True) -> (Tensor values, Tensor indices) |
| `aten.trunc` | trunc(Tensor self) -> Tensor |
| `aten.unsqueeze` | unsqueeze(Tensor(a) self, int dim) -> Tensor(a) |
| `aten.upsample_bilinear2d.vec` | upsample_bilinear2d.vec(Tensor input, SymInt[]? output_size, bool align_corners, float[]? scale_factors) -> Tensor |
| `aten.upsample_nearest2d.vec` | upsample_nearest2d.vec(Tensor input, SymInt[]? output_size, float[]? scale_factors) -> Tensor |
| `aten.var.correction` | var.correction(Tensor self, int[1]? dim=None, *, Scalar? correction=None, bool keepdim=False) -> Tensor |
| `aten.var.dim` | var.dim(Tensor self, int[1]? dim, bool unbiased=True, bool keepdim=False) -> Tensor |
| `aten.view` | view(Tensor(a) self, SymInt[] size) -> Tensor(a) |
| `aten.where.self` | where.self(Tensor condition, Tensor self, Tensor other) -> Tensor |

## Prims IR

Prims IR is a set of primitive operators that can be used to compose other operators.
Prims IR is a lower level opset than core aten IR, and it further decomposes ops into explicit
type promotion and broadcasting ops: prims.convert_element_type and prims.broadcast_in_dim.
This opset is designed to interface with compiler backends.

Warning

This opset is still under active development, more ops will be added in the future.

| Operator | Schema |
| --- | --- |
| `prims.abs` | (Tensor self) -> Tensor |
| `prims.acos` | (Tensor self) -> Tensor |
| `prims.acosh` | (Tensor self) -> Tensor |
| `prims.asin` | (Tensor self) -> Tensor |
| `prims.asinh` | (Tensor self) -> Tensor |
| `prims.atan` | (Tensor self) -> Tensor |
| `prims.atanh` | (Tensor self) -> Tensor |
| `prims.cos` | (Tensor self) -> Tensor |
| `prims.cosh` | (Tensor self) -> Tensor |
| `prims.bessel_i0` | (Tensor self) -> Tensor |
| `prims.bessel_i0e` | (Tensor self) -> Tensor |
| `prims.bessel_i1` | (Tensor self) -> Tensor |
| `prims.bessel_i1e` | (Tensor self) -> Tensor |
| `prims.bessel_j0` | (Tensor self) -> Tensor |
| `prims.bessel_j1` | (Tensor self) -> Tensor |
| `prims.bitwise_not` | (Tensor self) -> Tensor |
| `prims.cbrt` | (Tensor self) -> Tensor |
| `prims.ceil` | (Tensor self) -> Tensor |
| `prims.conj_physical` | (Tensor self) -> Tensor |
| `prims.digamma` | (Tensor self) -> Tensor |
| `prims.erf` | (Tensor self) -> Tensor |
| `prims.erf_inv` | (Tensor self) -> Tensor |
| `prims.erfc` | (Tensor self) -> Tensor |
| `prims.erfcx` | (Tensor self) -> Tensor |
| `prims.exp` | (Tensor self) -> Tensor |
| `prims.expm1` | (Tensor self) -> Tensor |
| `prims.exp2` | (Tensor self) -> Tensor |
| `prims.fill` | (Tensor self, Scalar value) -> Tensor |
| `prims.floor` | (Tensor self) -> Tensor |
| `prims.imag` | (Tensor(a) self) -> Tensor(a) |
| `prims.isfinite` | (Tensor self) -> Tensor |
| `prims.lgamma` | (Tensor self) -> Tensor |
| `prims.log` | (Tensor self) -> Tensor |
| `prims.log1p` | (Tensor self) -> Tensor |
| `prims.log2` | (Tensor self) -> Tensor |
| `prims.log10` | (Tensor self) -> Tensor |
| `prims.ndtri` | (Tensor self) -> Tensor |
| `prims.neg` | (Tensor self) -> Tensor |
| `prims.real` | (Tensor(a) self) -> Tensor(a) |
| `prims.reciprocal` | (Tensor self) -> Tensor |
| `prims.round` | (Tensor self) -> Tensor |
| `prims.sign` | (Tensor self) -> Tensor |
| `prims.signbit` | (Tensor self) -> Tensor |
| `prims.sin` | (Tensor self) -> Tensor |
| `prims.sinh` | (Tensor self) -> Tensor |
| `prims.spherical_bessel_j0` | (Tensor self) -> Tensor |
| `prims.sqrt` | (Tensor self) -> Tensor |
| `prims.tan` | (Tensor self) -> Tensor |
| `prims.tanh` | (Tensor self) -> Tensor |
| `prims.trunc` | (Tensor self) -> Tensor |
| `prims.add` | (Tensor self, Tensor other) -> Tensor |
| `prims.atan2` | (Tensor self, Tensor other) -> Tensor |
| `prims.bitwise_and` | (Tensor self, Tensor other) -> Tensor |
| `prims.bitwise_or` | (Tensor self, Tensor other) -> Tensor |
| `prims.bitwise_xor` | (Tensor self, Tensor other) -> Tensor |
| `prims.div` | (Tensor self, Tensor other) -> Tensor |
| `prims.eq` | (Tensor self, Tensor other) -> Tensor |
| `prims.fmax` | (Tensor self, Tensor other) -> Tensor |
| `prims.fmin` | (Tensor self, Tensor other) -> Tensor |
| `prims.fmod` | (Tensor self, Tensor other) -> Tensor |
| `prims.frexp` | (Tensor self) -> (Tensor mantissa, Tensor exponent) |
| `prims.gcd` | (Tensor self, Tensor other) -> Tensor |
| `prims.ge` | (Tensor self, Tensor other) -> Tensor |
| `prims.gt` | (Tensor self, Tensor other) -> Tensor |
| `prims.hypot` | (Tensor self, Tensor other) -> Tensor |
| `prims.igamma` | (Tensor self, Tensor other) -> Tensor |
| `prims.igammac` | (Tensor self, Tensor other) -> Tensor |
| `prims.le` | (Tensor self, Tensor other) -> Tensor |
| `prims.lt` | (Tensor self, Tensor other) -> Tensor |
| `prims.maximum` | (Tensor self, Tensor other) -> Tensor |
| `prims.minimum` | (Tensor self, Tensor other) -> Tensor |
| `prims.mul` | (Tensor self, Tensor other) -> Tensor |
| `prims.ne` | (Tensor self, Tensor other) -> Tensor |
| `prims.nextafter` | (Tensor self, Tensor other) -> Tensor |
| `prims.pow` | (Tensor self, Tensor other) -> Tensor |
| `prims.remainder` | (Tensor self, Tensor other) -> Tensor |
| `prims.rsqrt` | (Tensor self) -> Tensor |
| `prims.shift_left` | (Tensor self, Tensor other) -> Tensor |
| `prims.shift_right_arithmetic` | (Tensor self, Tensor other) -> Tensor |
| `prims.sub` | (Tensor self, Tensor other) -> Tensor |
| `prims.zeta` | (Tensor self, Tensor other) -> Tensor |
| `prims.as_strided` | (Tensor(a!) a, SymInt[] size, SymInt[] stride, SymInt storage_offset) -> Tensor(a!) |
| `prims.broadcast_in_dim` | (Tensor(a) a, SymInt[] shape, int[] broadcast_dimensions) -> Tensor(a) |
| `prims.collapse_view` | (Tensor(a) a, int start, int end) -> Tensor(a) |
| `prims.conj` | (Tensor(a) a) -> Tensor(a) |
| `prims.split_dim` | (Tensor(a) a, int dim, SymInt outer_length) -> Tensor(a) |
| `prims.squeeze` | (Tensor(a) a, int[] dimensions) -> Tensor(a) |
| `prims.transpose` | (Tensor(a) a, int[] permutation) -> Tensor(a) |
| `prims.view_of` | (Tensor(a) a) -> Tensor(a) |
| `prims.view_of_dtype` | (Tensor(a) a, ScalarType dtype) -> Tensor(a) |
| `prims.as_strided_scatter` | (Tensor self, Tensor src, SymInt[] size, SymInt[] stride, SymInt storage_offset) -> Tensor |
| `prims.collapse` | (Tensor a, int start, int end) -> Tensor |
| `prims.cat` | (Tensor[] tensors, int dim) -> Tensor |
| `prims.reshape` | (Tensor a, SymInt[] shape) -> Tensor |
| `prims.rev` | (Tensor a, int[] dims) -> Tensor |
| `prims.where` | (Tensor pred, Tensor a, Tensor b) -> Tensor |
| `prims.clone` | (Tensor self, *, MemoryFormat? memory_format=None) -> Tensor |
| `prims.convert_element_type` | (Tensor a, ScalarType dtype) -> Tensor |
| `prims.device_put` | (Tensor a, Device device, bool non_blocking=False) -> Tensor |
| `prims.item` | (Tensor a) -> Scalar |
| `prims.maximum_value` | (ScalarType dtype) -> Scalar |
| `prims.minimum_value` | (ScalarType dtype) -> Scalar |
| `prims.copy_strided` | (Tensor a, SymInt[] stride) -> Tensor |
| `prims.copy_to` | (Tensor(a!) a, Tensor b) -> Tensor(a!) |
| `prims.resize` | (Tensor(a!) a, SymInt[] shape) -> Tensor(a!) |
| `prims.amax` | (Tensor inp, int[]? dims, *, ScalarType? output_dtype=None) -> Tensor |
| `prims.amin` | (Tensor inp, int[]? dims, *, ScalarType? output_dtype=None) -> Tensor |
| `prims.prod` | (Tensor inp, int[]? dims, *, ScalarType? output_dtype=None) -> Tensor |
| `prims.sum` | (Tensor inp, int[]? dims, *, ScalarType? output_dtype=None) -> Tensor |
| `prims.xor_sum` | (Tensor inp, int[]? dims, *, ScalarType? output_dtype=None) -> Tensor |
| `prims.var` | (Tensor inp, int[]? dims, float? correction=1, *, ScalarType? output_dtype=None) -> Tensor |
| `prims.empty_strided` | (SymInt[] shape, SymInt[] strides, *, ScalarType dtype, Device device, bool requires_grad) -> Tensor |
| `prims.empty_permuted` | (SymInt[] shape, int[] physical_layout, *, ScalarType dtype, Device device, bool requires_grad) -> Tensor |
| `prims.scalar_tensor` | (Scalar s, *, ScalarType? dtype=None, Device? device=None) -> Tensor |
| `prims.iota` | (SymInt length, *, SymInt start, SymInt step, ScalarType dtype, Device device, bool requires_grad) -> Tensor |
| `prims.svd` | (Tensor A, *, bool full_matrices) -> (Tensor U, Tensor S, Tensor Vh) |
| `prims.normal` | (SymInt[] shape, *, Scalar mean, Scalar std, ScalarType dtype, Device device, bool requires_grad, Generator? generator=None) -> Tensor |
| `prims.uniform` | (SymInt[] shape, *, Scalar low, Scalar high, ScalarType dtype, Device device, SymInt[] stride, Generator? generator=None) -> Tensor |
| `prims.fft_r2c` | (Tensor self, *, int[] dim, bool onesided) -> Tensor |
| `prims.fft_c2c` | (Tensor self, *, int[] dim, bool forward) -> Tensor |
| `prims.fft_c2r` | (Tensor self, *, int[] dim, SymInt last_dim_size) -> Tensor |
| `prims._make_token` | () -> Tensor |
| `prims._sink_tokens` | (Tensor[] tokens) -> () |