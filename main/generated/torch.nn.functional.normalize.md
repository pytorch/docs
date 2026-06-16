# torch.nn.functional.normalize

torch.nn.functional.normalize(*input*, *p=2.0*, *dim=1*, *eps=1e-12*, *out=None*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/nn/functional.py#L6070)

Perform LpL_pLp​ normalization of inputs over specified dimension.

For a tensor `input` of sizes (n0,...,ndim,...,nk)(n_0, ..., n_{dim}, ..., n_k)(n0​,...,ndim​,...,nk​), each
ndimn_{dim}ndim​ -element vector vvv along dimension `dim` is transformed as

v=vmax⁡(∥v∥p,ϵ).v = \frac{v}{\max(\lVert v \rVert_p, \epsilon)}.

v=max(∥v∥p​,ϵ)v​.

With the default arguments it uses the Euclidean norm over vectors along dimension 111 for normalization.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - input tensor of any shape
- **p** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the exponent value in the norm formulation. Default: 2
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**ints*) - the dimension to reduce. Default: 1
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)) - small value to avoid division by zero. Default: 1e-12
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor. If `out` is used, this
operation won't be differentiable.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)