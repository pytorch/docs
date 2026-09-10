# torch.nn.functional.scaled_addmm_

torch.nn.functional.scaled_addmm_(*input*, *mat1*, *mat2*, *scale_a*, *scale_recipe_a*, *scale_b*, *scale_recipe_b*, *swizzle_a=None*, *swizzle_b=None*, *contraction_dim=()*, *use_fast_accum=False*, ***, *beta=1.0*, *alpha=1.0*)[[source]](https://github.com/pytorch/pytorch/blob/a62499b17156f49891b06593215215c6df2f94b4/torch/nn/functional.py#L7342)

In-place version of [`scaled_addmm()`](torch.nn.functional.scaled_addmm.html#torch.nn.functional.scaled_addmm).

This function accumulates in `input.dtype` (`float16`, `bfloat16`, or
`float32`), preserves the storage of `input`, and returns `input`. A
serialized WGRAD loop can create the first contribution with
[`scaled_mm()`](torch.nn.functional.scaled_mm.html#torch.nn.functional.scaled_mm), then use `scaled_addmm_` for later contributions.

Warning

In-place accumulation is not safe for concurrent writers. Callers must
serialize writes or provide external coordination.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)