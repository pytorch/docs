# torch.addbmm

torch.addbmm(*input*, *batch1*, *batch2*, ***, *beta=1*, *alpha=1*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Performs a batch matrix-matrix product of matrices stored
in `batch1` and `batch2`,
with a reduced add step (all matrix multiplications get accumulated
along the first dimension).
`input` is added to the final result.

`batch1` and `batch2` must be 3-D tensors each containing the
same number of matrices.

If `batch1` is a (b×n×m)(b \times n \times m)(b×n×m) tensor, `batch2` is a
(b×m×p)(b \times m \times p)(b×m×p) tensor, `input` must be
[broadcastable](../notes/broadcasting.html#broadcasting-semantics) with a (n×p)(n \times p)(n×p) tensor
and `out` will be a (n×p)(n \times p)(n×p) tensor.

out=β input+α (∑i=0b−1batch1i@batch2i)out = \beta\ \text{input} + \alpha\ (\sum_{i=0}^{b-1} \text{batch1}_i \mathbin{@} \text{batch2}_i)

out=β input+α (i=0∑b−1​batch1i​@batch2i​)

If `beta` is 0, then the content of `input` will be ignored, and nan and inf in
it will not be propagated.

For inputs of type FloatTensor or DoubleTensor, arguments `beta` and `alpha`
must be real numbers, otherwise they should be integers.

This operator supports [TensorFloat32](../notes/cuda.html#tf32-on-ampere).

On certain ROCm devices, when using float16 inputs this module will use [different precision](../notes/numerical_accuracy.html#fp16-on-mi200) for backward.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - matrix to be added
- **batch1** ([*Tensor*](../tensors.html#torch.Tensor)) - the first batch of matrices to be multiplied
- **batch2** ([*Tensor*](../tensors.html#torch.Tensor)) - the second batch of matrices to be multiplied

Keyword Arguments:

- **beta** (*Number**,**optional*) - multiplier for `input` (β\betaβ)
- **alpha** (*Number**,**optional*) - multiplier for batch1 @ batch2 (α\alphaα)
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> M = torch.randn(3, 5)
>>> batch1 = torch.randn(10, 3, 4)
>>> batch2 = torch.randn(10, 4, 5)
>>> torch.addbmm(M, batch1, batch2)
tensor([[ 6.6311, 0.0503, 6.9768, -12.0362, -2.1653],
 [ -4.8185, -1.4255, -6.6760, 8.9453, 2.5743],
 [ -3.8202, 4.3691, 1.0943, -1.1109, 5.4730]])
```