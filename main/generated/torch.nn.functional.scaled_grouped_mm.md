# torch.nn.functional.scaled_grouped_mm

torch.nn.functional.scaled_grouped_mm(*mat_a*, *mat_b*, *scale_a*, *scale_recipe_a*, *scale_b*, *scale_recipe_b*, *swizzle_a=None*, *swizzle_b=None*, *bias=None*, *offs=None*, *output_dtype=torch.bfloat16*, *contraction_dim=()*, *use_fast_accum=False*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/nn/functional.py#L7139)

scaled_grouped_mm(mat_a, mat_b, scale_a, scale_recipe_a, scale_b, scale_recipe_b, swizzle_a, swizzle_b, bias, offs,

output_dtype, use_fast_accum)

Applies a grouped scaled matrix-multiply, grouped_mm(mat_a, mat_b) where the scaling of mat_a and mat_b are described by
scale_recipe_a and scale_recipe_b respectively.

Parameters:

- **scale_a** ([*Tensor*](../tensors.html#torch.Tensor)*|*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - Tensor containing decoding scaling factors for mat_a
- **scale_recipe_a** (*_ScalingType**|*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**_ScalingType**]*) - Enum describing how mat_a has been scaled
- **scale_b** ([*Tensor*](../tensors.html#torch.Tensor)*|*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*Tensor*](../tensors.html#torch.Tensor)*]*) - Tensor containing decoding scaling factors for mat_b
- **scale_recipe_b** (*_ScalingType**|*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**_ScalingType**]*) - Enum describing how mat_b has been scaled
- **swizzle_a** (*_SwizzleType**|*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**_SwizzleType**]**|**None*) - Enum describing the swizzling pattern (if any) of scale_a
- **swizzle_b** (*_SwizzleType**|*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**_SwizzleType**]**|**None*) - Enum describing the swizzling pattern (if any) of scale_b
- **bias** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - optional bias term to be added to the output
- **offs** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - optional offsets into the source tensors denoting group start indices
- **output_dtype** ([*dtype*](../tensor_attributes.html#torch.dtype)*|**None*) - dtype used for the output tensor
- **contraction_dim** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,**...**]*) - describe which dimensions are KKK in the matmul.
- **use_fast_accum** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - enable/disable tensor-core fast accumulation (Hopper-GPUs only)

Return type:

[*Tensor*](../tensors.html#torch.Tensor)