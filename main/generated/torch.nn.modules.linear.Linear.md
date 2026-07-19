# Linear

*class*torch.nn.modules.linear.Linear(*in_features*, *out_features*, *bias=True*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/nn/modules/linear.py#L53)

Applies an affine linear transformation to the incoming data: y=xAT+by = xA^T + by=xAT+b.

This module supports [TensorFloat32](../notes/cuda.html#tf32-on-ampere).

On certain ROCm devices, when using float16 inputs this module will use [different precision](../notes/numerical_accuracy.html#fp16-on-mi200) for backward.

Parameters:

- **in_features** ([*int*](https://docs.python.org/3/library/functions.html#int)) - size of each input sample
- **out_features** ([*int*](https://docs.python.org/3/library/functions.html#int)) - size of each output sample
- **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If set to `False`, the layer will not learn an additive bias.
Default: `True`

Shape:

- Input: (∗,Hin)(*, H_\text{in})(∗,Hin​) where ∗*∗ means any number of
dimensions including none and Hin=in_featuresH_\text{in} = \text{in\_features}Hin​=in_features.
- Output: (∗,Hout)(*, H_\text{out})(∗,Hout​) where all but the last dimension
are the same shape as the input and Hout=out_featuresH_\text{out} = \text{out\_features}Hout​=out_features.

Variables:

- **weight** ([*torch.Tensor*](../tensors.html#torch.Tensor)) - the learnable weights of the module of shape
(out_features,in_features)(\text{out\_features}, \text{in\_features})(out_features,in_features). The values are
initialized from U(−k,k)\mathcal{U}(-\sqrt{k}, \sqrt{k})U(−k​,k​), where
k=1in_featuresk = \frac{1}{\text{in\_features}}k=in_features1​
- **bias** - the learnable bias of the module of shape (out_features)(\text{out\_features})(out_features).
If `bias` is `True`, the values are initialized from
U(−k,k)\mathcal{U}(-\sqrt{k}, \sqrt{k})U(−k​,k​) where
k=1in_featuresk = \frac{1}{\text{in\_features}}k=in_features1​

Examples:

```
>>> m = nn.Linear(20, 30)
>>> input = torch.randn(128, 20)
>>> output = m(input)
>>> print(output.size())
torch.Size([128, 30])
```

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/nn/modules/linear.py#L136)

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/nn/modules/linear.py#L130)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

reset_parameters()[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/nn/modules/linear.py#L117)

Resets parameters based on their initialization used in `__init__`.