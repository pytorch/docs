# torch.mm

torch.mm(*input*, *mat2*, *out_dtype=None*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Performs a matrix multiplication of the matrices `input` and `mat2`.

If `input` is a (n×m)(n \times m)(n×m) tensor, `mat2` is a
(m×p)(m \times p)(m×p) tensor, `out` will be a (n×p)(n \times p)(n×p) tensor.

Note

This function does not [broadcast](../notes/broadcasting.html#broadcasting-semantics).
For broadcasting matrix products, see [`torch.matmul()`](torch.matmul.html#torch.matmul).

Supports strided and sparse 2-D tensors as inputs, autograd with
respect to strided inputs.

This operation has support for arguments with [sparse layouts](../sparse.html#sparse-docs).
If `out` is provided its layout will be used. Otherwise, the result
layout will be deduced from that of `input`.

Warning

Sparse support is a beta feature and some layout(s)/dtype/device combinations may not be supported,
or may not have autograd support. If you notice missing functionality please
open a feature request.

This operator supports [TensorFloat32](../notes/cuda.html#tf32-on-ampere).

On certain ROCm devices, when using float16 inputs this module will use [different precision](../notes/numerical_accuracy.html#fp16-on-mi200) for backward.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the first matrix to be matrix multiplied
- **mat2** ([*Tensor*](../tensors.html#torch.Tensor)) - the second matrix to be matrix multiplied
- **out_dtype** ([*dtype*](../tensor_attributes.html#torch.dtype)*,**optional*) - the dtype of the output tensor,
Supported only on CUDA and for torch.float32 given
torch.float16/torch.bfloat16 input dtypes

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> mat1 = torch.randn(2, 3)
>>> mat2 = torch.randn(3, 3)
>>> torch.mm(mat1, mat2)
tensor([[ 0.4851, 0.5037, -0.3633],
 [-0.0760, -3.6705, 2.4784]])
```