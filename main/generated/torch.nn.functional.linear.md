# torch.nn.functional.linear

torch.nn.functional.linear(*input*, *weight*, *bias=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/nn/functional.py#L2382)

Applies a linear transformation to the incoming data: y=xAT+by = xA^T + by=xAT+b.

This operation supports 2-D `weight` with [sparse layout](../sparse.html#sparse-docs)

Warning

Sparse support is a beta feature and some layout(s)/dtype/device combinations may not be supported,
or may not have autograd support. If you notice missing functionality please
open a feature request.

This operator supports [TensorFloat32](../notes/cuda.html#tf32-on-ampere).

Shape:

> - Input: (∗,in_features)(*, in\_features)(∗,in_features) where * means any number of
> additional dimensions, including none
> - Weight: (out_features,in_features)(out\_features, in\_features)(out_features,in_features) or (in_features)(in\_features)(in_features)
> - Bias: (out_features)(out\_features)(out_features) or ()()()
> - Output: (∗,out_features)(*, out\_features)(∗,out_features) or (∗)(*)(∗), based on the shape of the weight