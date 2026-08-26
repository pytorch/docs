# CosineSimilarity

*class*torch.nn.CosineSimilarity(*dim=1*, *eps=1e-08*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/nn/modules/distance.py#L64)

Returns cosine similarity between x1x_1x1​ and x2x_2x2​, computed along dim.

similarity=x1⋅x2max⁡(∥x1∥2⋅∥x2∥2,ϵ).\text{similarity} = \dfrac{x_1 \cdot x_2}{\max(\Vert x_1 \Vert _2 \cdot \Vert x_2 \Vert _2, \epsilon)}.

similarity=max(∥x1​∥2​⋅∥x2​∥2​,ϵ)x1​⋅x2​​.
Parameters:

- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Dimension where cosine similarity is computed. Default: 1
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - Small value to avoid division by zero.
Default: 1e-8

Shape:

- Input1: (∗1,D,∗2)(\ast_1, D, \ast_2)(∗1​,D,∗2​) where D is at position dim
- Input2: (∗1,D,∗2)(\ast_1, D, \ast_2)(∗1​,D,∗2​), same number of dimensions as x1, matching x1 size at dimension dim,
and broadcastable with x1 at other dimensions.
- Output: (∗1,∗2)(\ast_1, \ast_2)(∗1​,∗2​)

Examples

```
>>> input1 = torch.randn(100, 128)
>>> input2 = torch.randn(100, 128)
>>> cos = nn.CosineSimilarity(dim=1, eps=1e-6)
>>> output = cos(input1, input2)
```

forward(*x1*, *x2*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/nn/modules/distance.py#L96)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)