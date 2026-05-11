# torch.bmm

torch.bmm(*input*, *mat2*, *out_dtype=None*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Performs a batch matrix-matrix product of matrices stored in `input`
and `mat2`.

`input` and `mat2` must be 3-D tensors each containing
the same number of matrices.

If `input` is a (b×n×m)(b \times n \times m)(b×n×m) tensor, `mat2` is a
(b×m×p)(b \times m \times p)(b×m×p) tensor, `out` will be a
(b×n×p)(b \times n \times p)(b×n×p) tensor.

outi=inputi@mat2i\text{out}_i = \text{input}_i \mathbin{@} \text{mat2}_i

outi​=inputi​@mat2i​

This operator supports [TensorFloat32](../notes/cuda.html#tf32-on-ampere).

On certain ROCm devices, when using float16 inputs this module will use [different precision](../notes/numerical_accuracy.html#fp16-on-mi200) for backward.

Note

This function does not [broadcast](../notes/broadcasting.html#broadcasting-semantics).
For broadcasting matrix products, see [`torch.matmul()`](torch.matmul.html#torch.matmul).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the first batch of matrices to be multiplied
- **mat2** ([*Tensor*](../tensors.html#torch.Tensor)) - the second batch of matrices to be multiplied
- **out_dtype** ([*dtype*](../tensor_attributes.html#torch.dtype)*,**optional*) - the dtype of the output tensor,
Supported only on CUDA and for torch.float32 given
torch.float16/torch.bfloat16 input dtypes

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> input = torch.randn(10, 3, 4)
>>> mat2 = torch.randn(10, 4, 5)
>>> res = torch.bmm(input, mat2)
>>> res.size()
torch.Size([10, 3, 5])
```