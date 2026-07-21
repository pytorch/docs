# torch.nn.functional.cosine_similarity

torch.nn.functional.cosine_similarity(*x1*, *x2*, *dim=1*, *eps=1e-8*, *keepdim=False*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/08fea85059e6f8092daa38319f7ea5bd7603d5e9/torch/nn/functional.py#L5895)

Returns cosine similarity between `x1` and `x2`, computed along dim. `x1` and `x2` must be broadcastable
to a common shape. `dim` refers to the dimension in this common shape. By default, dimension `dim` of the
output is squeezed (see [`torch.squeeze()`](torch.squeeze.html#torch.squeeze)), resulting in the output tensor having 1 fewer dimension.
When `keepdim` is `True`, the output has the same number of dimensions as the inputs with size 1 at `dim`.

similarity=x1⋅x2max⁡(∥x1∥2,ϵ)⋅max⁡(∥x2∥2,ϵ)\text{similarity} = \dfrac{x_1 \cdot x_2}{\max(\Vert x_1 \Vert _2, \epsilon) \cdot \max(\Vert x_2 \Vert _2, \epsilon)}

similarity=max(∥x1​∥2​,ϵ)⋅max(∥x2​∥2​,ϵ)x1​⋅x2​​

Supports [type promotion](../tensor_attributes.html#type-promotion-doc).

Parameters:

- **x1** ([*Tensor*](../tensors.html#torch.Tensor)) - First input.
- **x2** ([*Tensor*](../tensors.html#torch.Tensor)) - Second input.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Dimension along which cosine similarity is computed. Default: 1
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - Small value to avoid division by zero.
Default: 1e-8
- **keepdim** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether the output tensor retains `dim`. Default: False

Example:

```
>>> input1 = torch.randn(100, 128)
>>> input2 = torch.randn(100, 128)
>>> output = F.cosine_similarity(input1, input2)
>>> print(output)
```