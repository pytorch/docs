# torch.nn.functional.cosine_similarity

torch.nn.functional.cosine_similarity(*x1*, *x2*, *dim=1*, *eps=1e-8*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/2e3c34c8bd8296fe6b14c14ec67f82e8af85507e/torch/nn/functional.py#L5895)

Returns cosine similarity between `x1` and `x2`, computed along dim. `x1` and `x2` must be broadcastable
to a common shape. `dim` refers to the dimension in this common shape. Dimension `dim` of the output is
squeezed (see [`torch.squeeze()`](torch.squeeze.html#torch.squeeze)), resulting in the
output tensor having 1 fewer dimension.

similarity=x1⋅x2max⁡(∥x1∥2,ϵ)⋅max⁡(∥x2∥2,ϵ)\text{similarity} = \dfrac{x_1 \cdot x_2}{\max(\Vert x_1 \Vert _2, \epsilon) \cdot \max(\Vert x_2 \Vert _2, \epsilon)}

similarity=max(∥x1​∥2​,ϵ)⋅max(∥x2​∥2​,ϵ)x1​⋅x2​​

Supports [type promotion](../tensor_attributes.html#type-promotion-doc).

Parameters:

- **x1** ([*Tensor*](../tensors.html#torch.Tensor)) - First input.
- **x2** ([*Tensor*](../tensors.html#torch.Tensor)) - Second input.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Dimension along which cosine similarity is computed. Default: 1
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - Small value to avoid division by zero.
Default: 1e-8

Example:

```
>>> input1 = torch.randn(100, 128)
>>> input2 = torch.randn(100, 128)
>>> output = F.cosine_similarity(input1, input2)
>>> print(output)
```