# torch.nn.functional.scaled_addmm

torch.nn.functional.scaled_addmm(*input*, *mat1*, *mat2*, *scale_a*, *scale_recipe_a*, *scale_b*, *scale_recipe_b*, *swizzle_a=None*, *swizzle_b=None*, *contraction_dim=()*, *use_fast_accum=False*, ***, *beta=1.0*, *alpha=1.0*)[[source]](https://github.com/pytorch/pytorch/blob/84e524623ea4754a748936bf1ba6ecaaa92c3ae6/torch/nn/functional.py#L7266)

Compute a scaled matrix product and add it to `input`.

The result is

out=β input+α scaled_mm(mat1,mat2).\mathrm{out} = \beta\,\mathrm{input} +
\alpha\,\mathrm{scaled\_mm}(\mathrm{mat1}, \mathrm{mat2}).

out=βinput+αscaled_mm(mat1,mat2).

The scaling recipes and swizzles have the same meaning as in
[`scaled_mm()`](torch.nn.functional.scaled_mm.html#torch.nn.functional.scaled_mm). `input` must be a canonically contiguous, 16-byte-aligned
matrix with shape `(mat1.size(0), mat2.size(1))` and dtype `float16`, `bfloat16`, or
`float32`. The result has the dtype of `input`; there is no separate
output dtype. CUDA recipes are supported when their selected implementation
uses cuBLASLt; non-cuBLAS fallbacks and ROCm are not supported.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Matrix accumulated into the scaled matrix product.
- **mat1** ([*Tensor*](../tensors.html#torch.Tensor)) - Left matrix operand.
- **mat2** ([*Tensor*](../tensors.html#torch.Tensor)) - Right matrix operand.
- **scale_a** ([*Tensor*](../tensors.html#torch.Tensor)*|*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - Tensor containing decoding scaling factors for `mat1`.
- **scale_recipe_a** (*_ScalingType**|*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**_ScalingType**]*) - Scaling recipe for `mat1`.
- **scale_b** ([*Tensor*](../tensors.html#torch.Tensor)*|*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - Tensor containing decoding scaling factors for `mat2`.
- **scale_recipe_b** (*_ScalingType**|*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**_ScalingType**]*) - Scaling recipe for `mat2`.
- **swizzle_a** (*_SwizzleType**|*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**_SwizzleType**]**|**None*) - Swizzling pattern, if any, for `scale_a`.
- **swizzle_b** (*_SwizzleType**|*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**_SwizzleType**]**|**None*) - Swizzling pattern, if any, for `scale_b`.
- **contraction_dim** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,**...**]*) - Must be empty or `(1, 0)` (equivalent negative
dimensions are also accepted).
- **use_fast_accum** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Whether to enable tensor-core fast accumulation.
- **beta** ([*float*](https://docs.python.org/3/library/functions.html#float)) - Multiplier for `input`.
- **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) - Multiplier for the scaled matrix product.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Note

Fusing the addition removes an intermediate output rounding step, so
the result need not be bitwise equal to a separate scaled matrix
multiply followed by an addition.