# torch.baddbmm

torch.baddbmm(*input*, *batch1*, *batch2*, *out_dtype=None*, ***, *beta=1*, *alpha=1*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Performs a batch matrix-matrix product of matrices in `batch1`
and `batch2`.
`input` is added to the final result.

`batch1` and `batch2` must be 3-D tensors each containing the same
number of matrices.

If `batch1` is a (b×n×m)(b \times n \times m)(b×n×m) tensor, `batch2` is a
(b×m×p)(b \times m \times p)(b×m×p) tensor, then `input` must be
[broadcastable](../notes/broadcasting.html#broadcasting-semantics) with a
(b×n×p)(b \times n \times p)(b×n×p) tensor and `out` will be a
(b×n×p)(b \times n \times p)(b×n×p) tensor. Both `alpha` and `beta` mean the
same as the scaling factors used in [`torch.addbmm()`](torch.addbmm.html#torch.addbmm).

outi=β inputi+α (batch1i@batch2i)\text{out}_i = \beta\ \text{input}_i + \alpha\ (\text{batch1}_i \mathbin{@} \text{batch2}_i)

outi​=β inputi​+α (batch1i​@batch2i​)

If `beta` is 0, then the content of `input` will be ignored, and nan and inf in
it will not be propagated.

For inputs of type FloatTensor or DoubleTensor, arguments `beta` and
`alpha` must be real numbers, otherwise they should be integers.

This operator supports [TensorFloat32](../notes/cuda.html#tf32-on-ampere).

On certain ROCm devices, when using float16 inputs this module will use [different precision](../notes/numerical_accuracy.html#fp16-on-mi200) for backward.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor to be added
- **batch1** ([*Tensor*](../tensors.html#torch.Tensor)) - the first batch of matrices to be multiplied
- **batch2** ([*Tensor*](../tensors.html#torch.Tensor)) - the second batch of matrices to be multiplied
- **out_dtype** ([*dtype*](../tensor_attributes.html#torch.dtype)*,**optional*) - the dtype of the output tensor,
Supported only on CUDA and for torch.float32 given
torch.float16/torch.bfloat16 input dtypes

Keyword Arguments:

- **beta** (*Number**,**optional*) - multiplier for `input` (β\betaβ)
- **alpha** (*Number**,**optional*) - multiplier for batch1@batch2\text{batch1} \mathbin{@} \text{batch2}batch1@batch2 (α\alphaα)
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> M = torch.randn(10, 3, 5)
>>> batch1 = torch.randn(10, 3, 4)
>>> batch2 = torch.randn(10, 4, 5)
>>> torch.baddbmm(M, batch1, batch2).size()
torch.Size([10, 3, 5])
```