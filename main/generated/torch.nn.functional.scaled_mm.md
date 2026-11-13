# torch.nn.functional.scaled_mm

torch.nn.functional.scaled_mm(*mat_a*, *mat_b*, *scale_a*, *scale_recipe_a*, *scale_b*, *scale_recipe_b*, *swizzle_a=None*, *swizzle_b=None*, *bias=None*, *output_dtype=torch.bfloat16*, *contraction_dim=()*, *use_fast_accum=False*)[[source]](https://github.com/pytorch/pytorch/blob/b896199bee9ca0e125f6ec366a265418a8f3290e/torch/nn/functional.py#L7512)

scaled_mm(mat_a, mat_b, scale_a, scale_recipe_a, scale_b, scale_recipe_b, swizzle_a, swizzle_b, bias, output_dtype,

contraction_dim, use_fast_accum)

Applies a scaled matrix-multiply, mm(mat_a, mat_b) where the scaling of mat_a and mat_b are described by
scale_recipe_a and scale_recipe_b respectively.

Packed MNxK4 scaling uses matching `BlockWise1x32` or `BlockWise1x128` recipes
with `SWIZZLE_MN_K4` on both inputs. Inputs must be `float8_e4m3fn` or
`float8_e5m2`, with at least one `float8_e4m3fn` input.
It requires cuBLASLt 13.8.1 or later
(bundled with CUDA 13.4) on SM10.x/SM11.x, and supports bfloat16, float16, and
float32 outputs. Bias requires bfloat16 or float16 output with matching dtype.
`use_fast_accum` is forwarded to cuBLASLt for MNxK4.
MNxK4 requires row-major `mat_a` and column-major `mat_b`.
Scales are contiguous `float8_e8m0fnu` tensors with 16-byte-aligned data pointers.
For block size `B` (32 or 128) and outer extent `O` (M for A, N for B),
the physical row-major byte order is `[ceil(K / (4 * B)), round_up(O, 4), 4]`:
four consecutive K-block scales are packed together for each outer position.
Each scale buffer has `16 * ceil(O / 4) * ceil(K / (4 * B))` elements.
M need not be a multiple of four; K and N must be divisible by 16. Padding entries are ignored.

Parameters:

- **scale_a** ([*Tensor*](../tensors.html#torch.Tensor)*|*[*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - Tensor containing decoding scaling factors for mat_a
- **scale_recipe_a** (*_ScalingType**|*[*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[**_ScalingType**]*) - Enum describing how mat_a has been scaled
- **scale_b** ([*Tensor*](../tensors.html#torch.Tensor)*|*[*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - Tensor containing decoding scaling factors for mat_b
- **scale_recipe_b** (*_ScalingType**|*[*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[**_ScalingType**]*) - Enum describing how mat_b has been scaled
- **swizzle_a** (*_SwizzleType**|*[*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[**_SwizzleType**]**|**None*) - Enum describing the swizzling pattern (if any) of scale_a
- **swizzle_b** (*_SwizzleType**|*[*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[**_SwizzleType**]**|**None*) - Enum describing the swizzling pattern (if any) of scale_b
- **bias** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - optional bias term to be added to the output
- **output_dtype** ([*dtype*](../tensor_attributes.html#torch.dtype)*|**None*) - dtype used for the output tensor
- **contraction_dim** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*]**|*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**...**]*) - Must be empty or `(1, 0)` (equivalent negative
dimensions are also accepted).
- **use_fast_accum** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - Request tensor-core fast accumulation for supported recipes.
Hopper `BlockWise1x128`/`BlockWise128x128` require `False`;
MNxK4 forwards the flag to cuBLASLt.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)