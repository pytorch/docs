# torch.addmm

torch.addmm(*input*, *mat1*, *mat2*, ***, *beta=1*, *alpha=1*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Performs a matrix multiplication of the matrices `mat1` and `mat2`.
The matrix `input` is added to the final result.

If `mat1` is a (n×m)(n \times m)(n×m) tensor, `mat2` is a
(m×p)(m \times p)(m×p) tensor, then `input` must be
[broadcastable](../notes/broadcasting.html#broadcasting-semantics) with a (n×p)(n \times p)(n×p) tensor
and `out` will be a (n×p)(n \times p)(n×p) tensor.

`alpha` and `beta` are scaling factors on matrix-vector product between
`mat1` and `mat2` and the added matrix `input` respectively.

out=β input+α (mat1i@mat2i)\text{out} = \beta\ \text{input} + \alpha\ (\text{mat1}_i \mathbin{@} \text{mat2}_i)

out=β input+α (mat1i​@mat2i​)

If `beta` is 0, then the content of `input` will be ignored, and nan and inf in
it will not be propagated.

For inputs of type FloatTensor or DoubleTensor, arguments `beta` and
`alpha` must be real numbers, otherwise they should be integers.

This operation has support for arguments with [sparse layouts](../sparse.html#sparse-docs). If
`input` is sparse the result will have the same layout and if `out`
is provided it must have the same layout as `input`.

Warning

Sparse support is a beta feature and some layout(s)/dtype/device combinations may not be supported,
or may not have autograd support. If you notice missing functionality please
open a feature request.

This operator supports [TensorFloat32](../notes/cuda.html#tf32-on-ampere).

On certain ROCm devices, when using float16 inputs this module will use [different precision](../notes/numerical_accuracy.html#fp16-on-mi200) for backward.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - matrix to be added
- **mat1** ([*Tensor*](../tensors.html#torch.Tensor)) - the first matrix to be matrix multiplied
- **mat2** ([*Tensor*](../tensors.html#torch.Tensor)) - the second matrix to be matrix multiplied

Keyword Arguments:

- **beta** (*Number**,**optional*) - multiplier for `input` (β\betaβ)
- **alpha** (*Number**,**optional*) - multiplier for mat1@mat2mat1 @ mat2mat1@mat2 (α\alphaα)
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> M = torch.randn(2, 3)
>>> mat1 = torch.randn(2, 3)
>>> mat2 = torch.randn(3, 3)
>>> torch.addmm(M, mat1, mat2)
tensor([[-4.8716, 1.4671, -1.3746],
 [ 0.7573, -3.9555, -2.8681]])
```

torch.addmm(*input*, *mat1*, *mat2*, *out_dtype*, ***, *beta=1*, *alpha=1*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - matrix to be added
- **mat1** ([*Tensor*](../tensors.html#torch.Tensor)) - the first matrix to be matrix multiplied
- **mat2** ([*Tensor*](../tensors.html#torch.Tensor)) - the second matrix to be matrix multiplied
- **out_dtype** ([*dtype*](../tensor_attributes.html#torch.dtype)) - the dtype of the output tensor.
On CUDA and XPU, only `torch.float32` is supported given
`torch.float16`/`torch.bfloat16` input dtypes. Other backends
(including out-of-tree accelerators) may support additional
input/output dtype combinations.

Keyword Arguments:

- **beta** (*Number**,**optional*) - multiplier for `input` (β\betaβ)
- **alpha** (*Number**,**optional*) - multiplier for mat1@mat2mat1 @ mat2mat1@mat2 (α\alphaα)
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.