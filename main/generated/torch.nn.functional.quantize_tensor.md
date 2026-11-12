# torch.nn.functional.quantize_tensor

torch.nn.functional.quantize_tensor(*input*, ***, *dim*, *scaling_type*, *qdata_dtype*, *scaling_algorithm*, *swizzle_type*, *scaling_type_use_square_block_size=False*) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), [Tensor](../tensors.html#torch.Tensor)][[source]](https://github.com/pytorch/pytorch/blob/c5a2c86d66eda12ed122b796baae9cb0aaf5aefb/torch/nn/functional.py#L7296)

Subdivide `input` into 2D regions of `scaling_type` along the axes
specified in `dim`, then quantize according to `scaling_algorithm`
and `qdata_dtype` and return `(qdata, scale)` for use with
[`scaled_mm()`](torch.nn.functional.scaled_mm.html#torch.nn.functional.scaled_mm).
Currently supported formats: `mxfp8`. See the code samples at the bottom
of this docblock for how to configure supported formats.

A swizzled scale layout is modeled as packed `[1, L]` over the requested
quantization dims, with `L` being swizzle-specific. For example, for an input
of shape `(B, M, K)` and `dim=(1, 2)` and
`swizzle_type=SwizzleType.SWIZZLE_32_4_4`, the output scale shape will be
`(B, 1, ceil_div(M, 128) * ceil_div(K, 128) * 32 * 16)`.

Both outputs preserve the axis positions of the input. For both outputs,
the quantization axes from `dim` form contiguous slices when viewed
in `dim=(outer, inner)` order, with the inner dim varying the fastest
and outer next-fastest. For example:

- `mxfp8` unswizzled quantization of input shaped `(M, K)` with
strides `(K, 1)` and `dim=(0, 1)` will result in `qdata` with
shape `(M, K)` and strides `(K, 1)`, and `scale` with
shape `(M, K // 32)` and strides `(K // 32, 1)`.
- `mxfp8` swizzled quantization of input shaped `(M, K)` with
strides `(K, 1)` and `dim=(1, 0)` will result in `qdata` with
shape `(M, K)` and strides `(1, M)`, and `scale` with
shape `(L, 1)` and strides `(1, L)`, with `L` being
swizzle-specific.
- `mxfp8` swizzled quantization of input shaped `(K, M)` with
strides `(1, K)` and `dim=(0, 1)` will result in `qdata` with
shape `(K, M)` and strides `(M, 1)`, and `scale` with
shape `(1, L)` and strides `(L, 1)`, with `L` being
swizzle-specific.
- `mxfp8` swizzled quantization of input shaped `(B, K, N)` with
strides `(N * K, 1, K)` and `dim=(2, 1)` will result in `qdata`
with shape `(B, K, N)` and strides `(N * K, 1, K)` and `scale`
with shape `(B, L, 1)` and strides `(L, 1, L)`, with `L` being
swizzle-specific.

Automatic autograd is not supported for this op, users are encouraged to define
their own derivative.

This implementation currently requires an NVIDIA SM100 or newer GPU and the optional
`nvidia-cutlass-dsl` and `apache-tvm-ffi` packages. The hardware support may
expand in the future.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Tensor with at least two dimensions and dtype
`float16`, `bfloat16`, or `float32`.
- **dim** ([*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,*[*int*](https://docs.python.org/3/builtins/functions.html#int)*]*) - Ordered outer and inner quantization axes.
- **scaling_type** (*ScalingType*) - The size of the local region corresponding to
a single inner scale, as well as the layout of the output inner scale.
Currently supported values: `ScalingType.BlockWise1x32`.
- **qdata_dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype)) - The dtype of the resulting quantized
data. Currently supported values: `torch.float8_e4m3fn`. Special value
handling is format dependent. For example, for `mxfp8` an input
`NaN` or `Inf` makes every quantized value sharing its scale `NaN`;
all-zero blocks quantize to zero.
- **scaling_algorithm** ([*ScalingAlgorithm*](torch.nn.functional.ScalingAlgorithm.html#torch.nn.functional.ScalingAlgorithm)) - The algorithm to convert from a
local region of the `input` (with its size specified by `scaling_type`)
to the inner scale and inverse inner scale corresponding to that region.
Currently supported values: `ScalingAlgorithm.MXFP_E8M0_RU`.
- **swizzle_type** (*SwizzleType*) - The swizzle to apply to output inner scale.
Currently supported values: `SwizzleType.NO_SWIZZLE` and
`SwizzleType.SWIZZLE_32_4_4`.
- **scaling_type_use_square_block_size** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*,**optional*) - When `True`,
modify the size of the local region corresponding to a single scale
value to be a square (for example, modify `1x32` to be `32x32`).
Note that the output scale size is still controlled by `scaling_type`
and `swizzle_type`. If this flag is `True`, currently only
`SwizzleType.SWIZZLE_32_4_4` is supported. Default: `False`.

Returns:

Quantized data in the logical input shape and

scales with the dtype and layout honoring the `scaling_algorithm`,
`scaling_type`, and `swizzle_type` settings. For example, for
`mxfp8` on a 2D tensor with `dim=(0, 1)`, unswizzled scales have
shape `(rows, cols // 32)`; swizzled scales have shape `(1, L)`, where
`L = 512 * ceil(rows / 128) * ceil(cols / 128)`. Batch axes retain
their positions in both results.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), [Tensor](../tensors.html#torch.Tensor)]

Examples:

```
>>> import torch
>>> import torch.nn.functional as F
>>> x = torch.randn(128, 128, device="cuda", dtype=torch.bfloat16)
>>> mxfp8_kwargs = dict(
... scaling_type=F.ScalingType.BlockWise1x32,
... qdata_dtype=torch.float8_e4m3fn,
... scaling_algorithm=F.ScalingAlgorithm.MXFP_E8M0_RU,
... swizzle_type=F.SwizzleType.SWIZZLE_32_4_4,
... )
>>> # mxfp8 dim-k with swizzled scales
>>> qdata_k, scale_k = F.quantize_tensor(x, dim=(-2, -1), **mxfp8_kwargs)
>>> # mxfp8 dim-m on the same tensor
>>> qdata_m, scale_m = F.quantize_tensor(x, dim=(-1, -2), **mxfp8_kwargs)
>>> # mxfp8 dim-k with scales shared over 32x32 blocks
>>> qdata_square, scale_square = F.quantize_tensor(
... x, dim=(-2, -1), **mxfp8_kwargs, scaling_type_use_square_block_size=True
... )
>>> # mxfp8 dim-k with unswizzled scales
>>> plain_kwargs = {**mxfp8_kwargs, "swizzle_type": F.SwizzleType.NO_SWIZZLE}
>>> qdata_plain, scale_plain = F.quantize_tensor(x, dim=(-2, -1), **plain_kwargs)
```