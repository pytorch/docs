# torch.nn.functional.grouped_mm

torch.nn.functional.grouped_mm(*mat_a*, *mat_b*, ***, *offs=None*, *bias=None*, *out_dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/nn/functional.py#L6894)

Computes a grouped matrix multiply that shares weight shapes across experts but
allows jagged token counts per expert, which is common in Mixture-of-Experts
(MoE) layers. Both `mat_a` and `mat_b` must be 2D or 3D tensors that already
satisfy the physical layout restrictions of grouped GEMM kernels (e.g., row-major
`mat_a` and column-major `mat_b` for FP8 inputs). Inputs are currently
expected to be `torch.bfloat16` values on CUDA devices with SM≥80SM \ge 80SM≥80.

Parameters:

- **mat_a** ([*Tensor*](../tensors.html#torch.Tensor)) - Left operand. When 2D, its leading dimension is sliced into groups
according to `offs`. When 3D, its first dimension enumerates the groups
directly and `offs` must be `None`.
- **mat_b** ([*Tensor*](../tensors.html#torch.Tensor)) - Right operand. When both operands are 2D (e.g., MoE weight-gradient
updates), the trailing dimension of `mat_a` and the leading dimension of
`mat_b` are partitioned according to the same `offs` tensor. For the
common forward pass (`out = input @ weight.T`) `mat_b` is 3D with
shape `(num_groups, N, K)`.
- **offs** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - Optional 1D tensor of monotonically increasing `int32` offsets that
delimit the jagged dimension of any 2D operand. `offs[i]` marks the end
of group `i` and `offs[-1]` must be strictly less than the total
length of that operand's sliced dimension; elements beyond `offs[-1]`
are ignored.
- **bias** ([*Tensor*](../tensors.html#torch.Tensor)*|**None*) - Optional tensor that is added to the grouped outputs. Bias is not
jagged and must be broadcastable to the result shape of each group.
- **out_dtype** ([*dtype*](../tensor_attributes.html#torch.dtype)*|**None*) - Optional dtype that controls the accumulation/output dtype.
Passing `torch.float32` accumulates BF16 inputs in FP32 while keeping
the grouped GEMM API non-differentiable.

Returns:

A tensor containing the concatenated results of each per-group GEMM with
shape inferred from the operands and `offs`.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)