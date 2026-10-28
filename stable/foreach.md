# torch.foreach

Operations over lists of tensors.

Warning

`torch.foreach` is a beta API. Its signatures may change based on user
feedback. Existing private `torch._foreach_*` functions remain available
for compatibility during migration.

Each function applies the corresponding ordinary PyTorch operation to every
position in one or more tensor lists.

The functions will use an accelerated multi-tensor implementation when their
inputs meet its requirements. Otherwise they use a semantically equivalent
per-tensor fallback. Calling a function in this module does not guarantee a
single or fused kernel.

`torch.foreach` applies familiar PyTorch operations across lists of tensors. For
example, `torch.foreach.add(inputs, other)` is semantically equivalent to a
Python loop that applies [`torch.add()`](generated/torch.add.html#torch.add) at every list position. When
available on an accelerator and certain conditions are met, a foreach operation will use a horizontally fused multi-tensor kernel to improve
runtime. On CUDA, common eligibility requirements include strided,
non-overlapping dense tensors on the same device, compatible dtypes, and
matching sizes and strides for corresponding tensors.

```
inputs = [torch.ones(2), torch.ones(3)]
result = torch.foreach.add(inputs, 2)
# Equivalent to tuple(torch.add(tensor, 2) for tensor in inputs)

torch.foreach.mul_(inputs, 3)
# Mutates each tensor and returns `inputs`.
```

## API Coverage

A foreach API lifts an ordinary tensor operation over a list of inputs. This
creates a combinatorial space of possible signatures. Depending on the
operation, a tensor argument could be shared as a Tensor or supplied
elementwise as a TensorList, while a scalar argument could be a Scalar, a
ScalarList, a shared 0-D Tensor, or a packed 1-D CPU Tensor.

You can then imagine that one operation may take on various forms such as TensorList/TensorList, TensorList/Tensor, TensorList/ScalarList, TensorList/Scalar, etc. Operations with more parameters would have more combinations. The public foreach APIs support a subset of these combinations based on usage. If you would like to see an implementation of a missing combination, please file an [issue](https://github.com/pytorch/pytorch/issues/new/choose)!

Across the supported signatures, we maintain constraints that TensorList and ScalarList arguments must be non-empty, and corresponding tensor and scalar lists must have the same length.

Only signatures that explicitly list `Tensor` include it in the supported typed
surface. A 0-D Tensor that does not require gradients may sometimes be accepted
for a `Scalar` parameter through implicit scalar conversion. Converting an
accelerator Tensor this way reads its value on the host, which may be expensive. On CUDA, this synchronizes eager execution and is unsupported during CUDA graph capture, so it should not be relied upon as a Tensor overload.

The public foreach API also does not support `out=` variants and may have a higher memory footprint than looping through the non-foreach original API, as multiple intermediates can be alive simultaneously.

## Migrating from the private API

You may be familiar with the private spellings of foreach APIs, e.g., for [`torch.add()`](generated/torch.add.html#torch.add):

```
torch._foreach_add(inputs, other) # Private spelling
torch.foreach.add(inputs, other) # Public beta spelling
```

The private spellings remain available with unchanged signatures for backward compatibility.
Public functions call the same ATen operators but improve API consistency in two ways:

1. All required operands are positional-only, and all optional parameters are keyword-only.
2. Parameter names align with the corresponding ordinary operation.

The primary tensor-list argument that the foreach API applies over is named `inputs`, and other
arguments retain the ordinary operation's logical name, even when the currently supported form
requires a list. This keeps signatures descriptive as operand forms evolve.

## Unary operations

| [`abs`](generated/torch.foreach.abs.html#torch.foreach.abs) | Applies [`torch.abs()`](generated/torch.abs.html#torch.abs) to each tensor in `inputs`. |
| --- | --- |
| [`abs_`](generated/torch.foreach.abs_.html#torch.foreach.abs_) | Applies [`torch.abs()`](generated/torch.abs.html#torch.abs) to each tensor in `inputs` in-place. |
| [`acos`](generated/torch.foreach.acos.html#torch.foreach.acos) | Applies [`torch.acos()`](generated/torch.acos.html#torch.acos) to each tensor in `inputs`. |
| [`acos_`](generated/torch.foreach.acos_.html#torch.foreach.acos_) | Applies [`torch.acos()`](generated/torch.acos.html#torch.acos) to each tensor in `inputs` in-place. |
| [`asin`](generated/torch.foreach.asin.html#torch.foreach.asin) | Applies [`torch.asin()`](generated/torch.asin.html#torch.asin) to each tensor in `inputs`. |
| [`asin_`](generated/torch.foreach.asin_.html#torch.foreach.asin_) | Applies [`torch.asin()`](generated/torch.asin.html#torch.asin) to each tensor in `inputs` in-place. |
| [`atan`](generated/torch.foreach.atan.html#torch.foreach.atan) | Applies [`torch.atan()`](generated/torch.atan.html#torch.atan) to each tensor in `inputs`. |
| [`atan_`](generated/torch.foreach.atan_.html#torch.foreach.atan_) | Applies [`torch.atan()`](generated/torch.atan.html#torch.atan) to each tensor in `inputs` in-place. |
| [`ceil`](generated/torch.foreach.ceil.html#torch.foreach.ceil) | Applies [`torch.ceil()`](generated/torch.ceil.html#torch.ceil) to each tensor in `inputs`. |
| [`ceil_`](generated/torch.foreach.ceil_.html#torch.foreach.ceil_) | Applies [`torch.ceil()`](generated/torch.ceil.html#torch.ceil) to each tensor in `inputs` in-place. |
| [`clone`](generated/torch.foreach.clone.html#torch.foreach.clone) | Clones every tensor in `inputs`. |
| [`cos`](generated/torch.foreach.cos.html#torch.foreach.cos) | Applies [`torch.cos()`](generated/torch.cos.html#torch.cos) to each tensor in `inputs`. |
| [`cos_`](generated/torch.foreach.cos_.html#torch.foreach.cos_) | Applies [`torch.cos()`](generated/torch.cos.html#torch.cos) to each tensor in `inputs` in-place. |
| [`cosh`](generated/torch.foreach.cosh.html#torch.foreach.cosh) | Applies [`torch.cosh()`](generated/torch.cosh.html#torch.cosh) to each tensor in `inputs`. |
| [`cosh_`](generated/torch.foreach.cosh_.html#torch.foreach.cosh_) | Applies [`torch.cosh()`](generated/torch.cosh.html#torch.cosh) to each tensor in `inputs` in-place. |
| [`erf`](generated/torch.foreach.erf.html#torch.foreach.erf) | Applies [`torch.erf()`](generated/torch.erf.html#torch.erf) to each tensor in `inputs`. |
| [`erf_`](generated/torch.foreach.erf_.html#torch.foreach.erf_) | Applies [`torch.erf()`](generated/torch.erf.html#torch.erf) to each tensor in `inputs` in-place. |
| [`erfc`](generated/torch.foreach.erfc.html#torch.foreach.erfc) | Applies [`torch.erfc()`](generated/torch.erfc.html#torch.erfc) to each tensor in `inputs`. |
| [`erfc_`](generated/torch.foreach.erfc_.html#torch.foreach.erfc_) | Applies [`torch.erfc()`](generated/torch.erfc.html#torch.erfc) to each tensor in `inputs` in-place. |
| [`exp`](generated/torch.foreach.exp.html#torch.foreach.exp) | Applies [`torch.exp()`](generated/torch.exp.html#torch.exp) to each tensor in `inputs`. |
| [`exp_`](generated/torch.foreach.exp_.html#torch.foreach.exp_) | Applies [`torch.exp()`](generated/torch.exp.html#torch.exp) to each tensor in `inputs` in-place. |
| [`expm1`](generated/torch.foreach.expm1.html#torch.foreach.expm1) | Applies [`torch.expm1()`](generated/torch.expm1.html#torch.expm1) to each tensor in `inputs`. |
| [`expm1_`](generated/torch.foreach.expm1_.html#torch.foreach.expm1_) | Applies [`torch.expm1()`](generated/torch.expm1.html#torch.expm1) to each tensor in `inputs` in-place. |
| [`floor`](generated/torch.foreach.floor.html#torch.foreach.floor) | Applies [`torch.floor()`](generated/torch.floor.html#torch.floor) to each tensor in `inputs`. |
| [`floor_`](generated/torch.foreach.floor_.html#torch.foreach.floor_) | Applies [`torch.floor()`](generated/torch.floor.html#torch.floor) to each tensor in `inputs` in-place. |
| [`frac`](generated/torch.foreach.frac.html#torch.foreach.frac) | Applies [`torch.frac()`](generated/torch.frac.html#torch.frac) to each tensor in `inputs`. |
| [`frac_`](generated/torch.foreach.frac_.html#torch.foreach.frac_) | Applies [`torch.frac()`](generated/torch.frac.html#torch.frac) to each tensor in `inputs` in-place. |
| [`lgamma`](generated/torch.foreach.lgamma.html#torch.foreach.lgamma) | Applies [`torch.lgamma()`](generated/torch.lgamma.html#torch.lgamma) to each tensor in `inputs`. |
| [`lgamma_`](generated/torch.foreach.lgamma_.html#torch.foreach.lgamma_) | Applies [`torch.lgamma()`](generated/torch.lgamma.html#torch.lgamma) to each tensor in `inputs` in-place. |
| [`log`](generated/torch.foreach.log.html#torch.foreach.log) | Applies [`torch.log()`](generated/torch.log.html#torch.log) to each tensor in `inputs`. |
| [`log_`](generated/torch.foreach.log_.html#torch.foreach.log_) | Applies [`torch.log()`](generated/torch.log.html#torch.log) to each tensor in `inputs` in-place. |
| [`log10`](generated/torch.foreach.log10.html#torch.foreach.log10) | Applies [`torch.log10()`](generated/torch.log10.html#torch.log10) to each tensor in `inputs`. |
| [`log10_`](generated/torch.foreach.log10_.html#torch.foreach.log10_) | Applies [`torch.log10()`](generated/torch.log10.html#torch.log10) to each tensor in `inputs` in-place. |
| [`log1p`](generated/torch.foreach.log1p.html#torch.foreach.log1p) | Applies [`torch.log1p()`](generated/torch.log1p.html#torch.log1p) to each tensor in `inputs`. |
| [`log1p_`](generated/torch.foreach.log1p_.html#torch.foreach.log1p_) | Applies [`torch.log1p()`](generated/torch.log1p.html#torch.log1p) to each tensor in `inputs` in-place. |
| [`log2`](generated/torch.foreach.log2.html#torch.foreach.log2) | Applies [`torch.log2()`](generated/torch.log2.html#torch.log2) to each tensor in `inputs`. |
| [`log2_`](generated/torch.foreach.log2_.html#torch.foreach.log2_) | Applies [`torch.log2()`](generated/torch.log2.html#torch.log2) to each tensor in `inputs` in-place. |
| [`neg`](generated/torch.foreach.neg.html#torch.foreach.neg) | Applies [`torch.neg()`](generated/torch.neg.html#torch.neg) to each tensor in `inputs`. |
| [`neg_`](generated/torch.foreach.neg_.html#torch.foreach.neg_) | Applies [`torch.neg()`](generated/torch.neg.html#torch.neg) to each tensor in `inputs` in-place. |
| [`reciprocal`](generated/torch.foreach.reciprocal.html#torch.foreach.reciprocal) | Applies [`torch.reciprocal()`](generated/torch.reciprocal.html#torch.reciprocal) to each tensor in `inputs`. |
| [`reciprocal_`](generated/torch.foreach.reciprocal_.html#torch.foreach.reciprocal_) | Applies [`torch.reciprocal()`](generated/torch.reciprocal.html#torch.reciprocal) to each tensor in `inputs` in-place. |
| [`round`](generated/torch.foreach.round.html#torch.foreach.round) | Applies [`torch.round()`](generated/torch.round.html#torch.round) to each tensor in `inputs`. |
| [`round_`](generated/torch.foreach.round_.html#torch.foreach.round_) | Applies [`torch.round()`](generated/torch.round.html#torch.round) to each tensor in `inputs` in-place. |
| [`rsqrt`](generated/torch.foreach.rsqrt.html#torch.foreach.rsqrt) | Applies [`torch.rsqrt()`](generated/torch.rsqrt.html#torch.rsqrt) to each tensor in `inputs`. |
| [`rsqrt_`](generated/torch.foreach.rsqrt_.html#torch.foreach.rsqrt_) | Applies [`torch.rsqrt()`](generated/torch.rsqrt.html#torch.rsqrt) to each tensor in `inputs` in-place. |
| [`sigmoid`](generated/torch.foreach.sigmoid.html#torch.foreach.sigmoid) | Applies [`torch.sigmoid()`](generated/torch.sigmoid.html#torch.sigmoid) to each tensor in `inputs`. |
| [`sigmoid_`](generated/torch.foreach.sigmoid_.html#torch.foreach.sigmoid_) | Applies [`torch.sigmoid()`](generated/torch.sigmoid.html#torch.sigmoid) to each tensor in `inputs` in-place. |
| [`sign`](generated/torch.foreach.sign.html#torch.foreach.sign) | Applies [`torch.sign()`](generated/torch.sign.html#torch.sign) to each tensor in `inputs`. |
| [`sign_`](generated/torch.foreach.sign_.html#torch.foreach.sign_) | Applies [`torch.sign()`](generated/torch.sign.html#torch.sign) to each tensor in `inputs` in-place. |
| [`sin`](generated/torch.foreach.sin.html#torch.foreach.sin) | Applies [`torch.sin()`](generated/torch.sin.html#torch.sin) to each tensor in `inputs`. |
| [`sin_`](generated/torch.foreach.sin_.html#torch.foreach.sin_) | Applies [`torch.sin()`](generated/torch.sin.html#torch.sin) to each tensor in `inputs` in-place. |
| [`sinh`](generated/torch.foreach.sinh.html#torch.foreach.sinh) | Applies [`torch.sinh()`](generated/torch.sinh.html#torch.sinh) to each tensor in `inputs`. |
| [`sinh_`](generated/torch.foreach.sinh_.html#torch.foreach.sinh_) | Applies [`torch.sinh()`](generated/torch.sinh.html#torch.sinh) to each tensor in `inputs` in-place. |
| [`sqrt`](generated/torch.foreach.sqrt.html#torch.foreach.sqrt) | Applies [`torch.sqrt()`](generated/torch.sqrt.html#torch.sqrt) to each tensor in `inputs`. |
| [`sqrt_`](generated/torch.foreach.sqrt_.html#torch.foreach.sqrt_) | Applies [`torch.sqrt()`](generated/torch.sqrt.html#torch.sqrt) to each tensor in `inputs` in-place. |
| [`tan`](generated/torch.foreach.tan.html#torch.foreach.tan) | Applies [`torch.tan()`](generated/torch.tan.html#torch.tan) to each tensor in `inputs`. |
| [`tan_`](generated/torch.foreach.tan_.html#torch.foreach.tan_) | Applies [`torch.tan()`](generated/torch.tan.html#torch.tan) to each tensor in `inputs` in-place. |
| [`tanh`](generated/torch.foreach.tanh.html#torch.foreach.tanh) | Applies [`torch.tanh()`](generated/torch.tanh.html#torch.tanh) to each tensor in `inputs`. |
| [`tanh_`](generated/torch.foreach.tanh_.html#torch.foreach.tanh_) | Applies [`torch.tanh()`](generated/torch.tanh.html#torch.tanh) to each tensor in `inputs` in-place. |
| [`trunc`](generated/torch.foreach.trunc.html#torch.foreach.trunc) | Applies [`torch.trunc()`](generated/torch.trunc.html#torch.trunc) to each tensor in `inputs`. |
| [`trunc_`](generated/torch.foreach.trunc_.html#torch.foreach.trunc_) | Applies [`torch.trunc()`](generated/torch.trunc.html#torch.trunc) to each tensor in `inputs` in-place. |
| [`zero_`](generated/torch.foreach.zero_.html#torch.foreach.zero_) | Fills every tensor in `inputs` with zero. |

## Binary operations

| [`add`](generated/torch.foreach.add.html#torch.foreach.add) | Applies [`torch.add()`](generated/torch.add.html#torch.add) to every tensor in `inputs`. |
| --- | --- |
| [`add_`](generated/torch.foreach.add_.html#torch.foreach.add_) | Applies [`torch.add()`](generated/torch.add.html#torch.add) to every tensor in `inputs`. |
| [`sub`](generated/torch.foreach.sub.html#torch.foreach.sub) | Applies [`torch.sub()`](generated/torch.sub.html#torch.sub) to every tensor in `inputs`. |
| [`sub_`](generated/torch.foreach.sub_.html#torch.foreach.sub_) | Applies [`torch.sub()`](generated/torch.sub.html#torch.sub) to every tensor in `inputs`. |
| [`mul`](generated/torch.foreach.mul.html#torch.foreach.mul) | Applies [`torch.mul()`](generated/torch.mul.html#torch.mul) to every tensor in `inputs`. |
| [`mul_`](generated/torch.foreach.mul_.html#torch.foreach.mul_) | Applies [`torch.mul()`](generated/torch.mul.html#torch.mul) to every tensor in `inputs`. |
| [`div`](generated/torch.foreach.div.html#torch.foreach.div) | Applies [`torch.div()`](generated/torch.div.html#torch.div) to every tensor in `inputs`. |
| [`div_`](generated/torch.foreach.div_.html#torch.foreach.div_) | Applies [`torch.div()`](generated/torch.div.html#torch.div) to every tensor in `inputs`. |
| [`clamp_min`](generated/torch.foreach.clamp_min.html#torch.foreach.clamp_min) | Applies [`torch.clamp()`](generated/torch.clamp.html#torch.clamp) to every tensor in `inputs`. |
| [`clamp_min_`](generated/torch.foreach.clamp_min_.html#torch.foreach.clamp_min_) | Applies [`torch.clamp()`](generated/torch.clamp.html#torch.clamp) to every tensor in `inputs`. |
| [`clamp_max`](generated/torch.foreach.clamp_max.html#torch.foreach.clamp_max) | Applies [`torch.clamp()`](generated/torch.clamp.html#torch.clamp) to every tensor in `inputs`. |
| [`clamp_max_`](generated/torch.foreach.clamp_max_.html#torch.foreach.clamp_max_) | Applies [`torch.clamp()`](generated/torch.clamp.html#torch.clamp) to every tensor in `inputs`. |
| [`minimum`](generated/torch.foreach.minimum.html#torch.foreach.minimum) | Applies [`torch.minimum()`](generated/torch.minimum.html#torch.minimum) to every tensor in `inputs`. |
| [`minimum_`](generated/torch.foreach.minimum_.html#torch.foreach.minimum_) | Applies [`torch.minimum()`](generated/torch.minimum.html#torch.minimum) to every tensor in `inputs`. |
| [`maximum`](generated/torch.foreach.maximum.html#torch.foreach.maximum) | Applies [`torch.maximum()`](generated/torch.maximum.html#torch.maximum) to every tensor in `inputs`. |
| [`maximum_`](generated/torch.foreach.maximum_.html#torch.foreach.maximum_) | Applies [`torch.maximum()`](generated/torch.maximum.html#torch.maximum) to every tensor in `inputs`. |
| [`pow`](generated/torch.foreach.pow.html#torch.foreach.pow) | Applies [`torch.pow()`](generated/torch.pow.html#torch.pow) at each list position. |
| [`pow_`](generated/torch.foreach.pow_.html#torch.foreach.pow_) | In-place version of [`torch.foreach.pow()`](generated/torch.foreach.pow.html#torch.foreach.pow). |
| [`copy_`](generated/torch.foreach.copy_.html#torch.foreach.copy_) | Copies each tensor in `src` into the corresponding tensor in `inputs`, following [`torch.Tensor.copy_()`](generated/torch.Tensor.copy_.html#torch.Tensor.copy_). |

## Pointwise operations

| [`addcmul`](generated/torch.foreach.addcmul.html#torch.foreach.addcmul) | Applies [`torch.addcmul()`](generated/torch.addcmul.html#torch.addcmul) to corresponding tensors from the three input lists. |
| --- | --- |
| [`addcmul_`](generated/torch.foreach.addcmul_.html#torch.foreach.addcmul_) | Applies [`torch.addcmul()`](generated/torch.addcmul.html#torch.addcmul) to corresponding tensors from the three input lists. |
| [`addcdiv`](generated/torch.foreach.addcdiv.html#torch.foreach.addcdiv) | Applies [`torch.addcdiv()`](generated/torch.addcdiv.html#torch.addcdiv) to corresponding tensors from the three input lists. |
| [`addcdiv_`](generated/torch.foreach.addcdiv_.html#torch.foreach.addcdiv_) | Applies [`torch.addcdiv()`](generated/torch.addcdiv.html#torch.addcdiv) to corresponding tensors from the three input lists. |
| [`lerp`](generated/torch.foreach.lerp.html#torch.foreach.lerp) | Applies [`torch.lerp()`](generated/torch.lerp.html#torch.lerp) to corresponding tensors in `inputs` and `end`. |
| [`lerp_`](generated/torch.foreach.lerp_.html#torch.foreach.lerp_) | In-place version of [`torch.foreach.lerp()`](generated/torch.foreach.lerp.html#torch.foreach.lerp). |

## Reductions and matrix operations

| [`max`](generated/torch.foreach.max.html#torch.foreach.max) | Returns the maximum value of each tensor in `inputs`. |
| --- | --- |
| [`norm`](generated/torch.foreach.norm.html#torch.foreach.norm) | Returns the vector norm of each tensor in `inputs`. |
| [`mm`](generated/torch.foreach.mm.html#torch.foreach.mm) | Multiplies corresponding matrices from `inputs` and `mat2` using [`torch.mm()`](generated/torch.mm.html#torch.mm). |