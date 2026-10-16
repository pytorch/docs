# torch.nn.functional.grouped_mm

torch.nn.functional.grouped_mm(*mat_a*, *mat_b*, ***, *offs=None*, *bias=None*, *out_dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/be79392a0cedbbc0b5d2d3288173316425f90af4/torch/nn/functional.py#L7200)

Computes a grouped matrix multiply that shares weight shapes across experts but
allows jagged token counts per expert, which is common in Mixture-of-Experts
(MoE) layers. Both `mat_a` and `mat_b` must be 2D or 3D tensors that satisfy
the physical layout restrictions of grouped GEMM kernels. Inputs may be
`torch.float16`, `torch.bfloat16`, or `torch.float32` values. CUDA
execution is supported on devices with SM≥80SM \ge 80SM≥80.

Parameters:

- **mat_a** ([*Tensor*](../tensors.html#torch.Tensor)) - Left operand. When 2D, its leading dimension is sliced into groups
according to `offs`. When 3D, its first dimension enumerates the groups
directly and `offs` must be `None`.
- **mat_b** ([*Tensor*](../tensors.html#torch.Tensor)) - Right operand. When both operands are 2D (e.g., MoE weight-gradient
updates), the trailing dimension of `mat_a` and the leading dimension of
`mat_b` are partitioned according to the same `offs` tensor. For the
common forward pass (`out = input @ weight.T`) `mat_b` is 3D with
shape `(num_groups, K, N)`. If expert weights are stored in the standard
`nn.Linear` layout `(num_groups, N, K)`, pass
`weight.transpose(-2, -1)` as `mat_b`.
- **offs** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - Optional 1D tensor of monotonically increasing `int32` offsets that
delimit the jagged dimension of any 2D operand. `offs[i]` marks the end
of group `i` and `offs[-1]` must be strictly less than the total
length of that operand's sliced dimension; elements beyond `offs[-1]`
are ignored.
- **bias** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - Reserved for future use. It must currently be `None`.
- **out_dtype** ([*dtype*](../tensor_attributes.html#torch.dtype)*|**None*) - Optional output dtype. When provided, it must match the dtype of
`mat_a`.

Returns:

A tensor containing the concatenated results of each per-group GEMM with
shape inferred from the operands and `offs`.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)