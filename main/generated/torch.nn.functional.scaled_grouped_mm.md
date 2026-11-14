# torch.nn.functional.scaled_grouped_mm

torch.nn.functional.scaled_grouped_mm(*mat_a*, *mat_b*, *scale_a*, *scale_recipe_a*, *scale_b*, *scale_recipe_b*, *swizzle_a=None*, *swizzle_b=None*, *bias=None*, *offs=None*, *output_dtype=torch.bfloat16*, *contraction_dim=()*, *use_fast_accum=False*)[[source]](https://github.com/pytorch/pytorch/blob/b5cf35aa75e0d5087ede9131ab2f970aa2de6509/torch/nn/functional.py#L7716)

scaled_grouped_mm(mat_a, mat_b, scale_a, scale_recipe_a, scale_b, scale_recipe_b, swizzle_a, swizzle_b, bias, offs,

output_dtype, use_fast_accum)

Applies a grouped scaled matrix-multiply, grouped_mm(mat_a, mat_b) where the scaling of mat_a and mat_b are described by
scale_recipe_a and scale_recipe_b respectively.

When `scale_recipe_a` and `scale_recipe_b` are each the single recipe `TensorWise`,
each float32 scale contains either a single value shared by all groups
or one value per group in a contiguous 1D tensor. Each input may use either scale layout.
Both inputs must be `float8_e4m3fn` or `float8_e5m2`, with at least one `float8_e4m3fn` input.
At most 1024 groups are supported.
TensorWise scaling requires CUDA 13.4 or later on SM9.x-SM11.x; swizzle metadata is ignored.
It supports bfloat16, float16, and float32 outputs.

Hopper block scaling requires CUDA 13.4 or later on SM9.x and supports recipe pairs
1x128/1x128, 1x128/128x128, and 128x128/1x128 with float32 scales and two
`float8_e4m3fn` inputs. Each group packs
its scales separately. For outer extent `O` (M for A, N for B), let `L = ceil(K / 128)`.
A 1x128 group stores `O * L` values with the outer dimension contiguous; a 128x128
group stores `round_up(L, 4) * ceil(O / 128)` values with the padded K-block dimension
contiguous. Scales are contiguous, with 16-byte-aligned group starts. A 3D operand uses
shape `(groups, values_per_group)`; a 2D operand uses a 1D tensor concatenating
the flattened group scales in offset order, covering only the groups selected by `offs`. M and N must be multiples
of 4. These recipes support bfloat16, float16, and float32 outputs and require
`use_fast_accum=False`. Swizzle metadata must be omitted or `NO_SWIZZLE`.

Packed MNxK4 scaling uses the recipes, byte order, element count, and alignment
described in [`scaled_mm()`](torch.nn.functional.scaled_mm.html#torch.nn.functional.scaled_mm), independently for each group. A 3D operand uses
scale shape `(groups, elements_per_group)`; a 2D operand concatenates each
group's flattened scale buffer in offset order. Each group starts at a 16-byte
boundary. Per-group M need not be a multiple of four. K and the total N
dimension must be divisible by 16, including when `offs` splits N. Group output
starts must be 16-byte aligned: starting N offsets must be multiples of 8
for bfloat16/float16 output or 4 for float32 output. Invalid group output
alignment triggers a device assertion. It requires
cuBLASLt 13.8.1 or later (bundled with CUDA 13.4) on SM10.x/SM11.x and accepts
bfloat16, float16, and float32 outputs. `use_fast_accum` is forwarded to cuBLASLt
for MNxK4.

Other recipes require bfloat16 output.

Parameters:

- **scale_a** ([*Tensor*](../tensors.html#torch.Tensor)*|*[*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - Tensor containing decoding scaling factors for mat_a
- **scale_recipe_a** (*_ScalingType**|*[*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[**_ScalingType**]*) - Enum describing how mat_a has been scaled
- **scale_b** ([*Tensor*](../tensors.html#torch.Tensor)*|*[*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - Tensor containing decoding scaling factors for mat_b
- **scale_recipe_b** (*_ScalingType**|*[*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[**_ScalingType**]*) - Enum describing how mat_b has been scaled
- **swizzle_a** (*_SwizzleType**|*[*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[**_SwizzleType**]**|**None*) - Enum describing the swizzling pattern (if any) of scale_a
- **swizzle_b** (*_SwizzleType**|*[*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[**_SwizzleType**]**|**None*) - Enum describing the swizzling pattern (if any) of scale_b
- **bias** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - optional bias term to be added to the output
- **offs** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - optional offsets into the source tensors denoting group start indices
- **output_dtype** ([*dtype*](../tensor_attributes.html#torch.dtype)*|**None*) - output dtype; the cuBLASLt recipes described above (including `TensorWise`
alone on both inputs) accept bfloat16, float16, or float32; other recipes require bfloat16
- **contraction_dim** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list)*[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*]**|*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**...**]*) - describe which dimensions are KKK in the matmul.
- **use_fast_accum** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - Request tensor-core fast accumulation for cuBLASLt recipes
(including MNxK4) and CUDA RowWise scaling. Hopper
`BlockWise1x128`/`BlockWise128x128` require `False`.
MSLK recipes and ROCm ignore this flag.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)