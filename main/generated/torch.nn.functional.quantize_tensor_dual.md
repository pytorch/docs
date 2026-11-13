# torch.nn.functional.quantize_tensor_dual

torch.nn.functional.quantize_tensor_dual(*input*, ***, *dim*, *scaling_type*, *qdata_dtype*, *scaling_algorithm*, *swizzle_type*, *scaling_type_use_square_block_size=False*) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), [Tensor](../tensors.html#torch.Tensor), [Tensor](../tensors.html#torch.Tensor), [Tensor](../tensors.html#torch.Tensor)][[source]](https://github.com/pytorch/pytorch/blob/b896199bee9ca0e125f6ec366a265418a8f3290e/torch/nn/functional.py#L7425)

Subdivide `input` into 2D regions of `scaling_type` along the axes
specified in `dim` as well as `dim[::-1]`, then quantize according to
`scaling_algorithm` and `qdata_dtype` and return
`(qdata0, scale0, qdata1, scale1)` for use with [`scaled_mm()`](torch.nn.functional.scaled_mm.html#torch.nn.functional.scaled_mm).

See [`quantize_tensor()`](torch.nn.functional.quantize_tensor.html#torch.nn.functional.quantize_tensor) to quantize along only one direction.

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
Currently supported values: `SwizzleType.SWIZZLE_32_4_4`.
- **scaling_type_use_square_block_size** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*,**optional*) - When `True`,
modify the size of the local region corresponding to a single scale
value to be a square (for example, modify `1x32` to be `32x32`).
Note that the output scale size is still controlled by `scaling_type`
and `swizzle_type`. Note: currently only `False` is supported.
Default: `False`.

Returns:

`(qdata, scale, qdata_reverse, scale_reverse)`.

For example, for input of shape `(M, K)` and the
`mxfp8` format, both quantized tensors have shape `(M, K)`.
When `dim=(0, 1)`, the dim-K result is contiguous; the dim-M result has strides
`(1, M)`. Their E8M0 scales have shapes `(1, L)` and
`(L, 1)`, respectively, where
`L = 512 * ceil(M / 128) * ceil(K / 128)`.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](../tensors.html#torch.Tensor), [Tensor](../tensors.html#torch.Tensor), [Tensor](../tensors.html#torch.Tensor), [Tensor](../tensors.html#torch.Tensor)]

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
>>> # mxfp8 dim-km with swizzled scales
>>> qdata_k, scale_k, qdata_m, scale_m = F.quantize_tensor_dual(x, dim=(-2, -1), **mxfp8_kwargs)
```