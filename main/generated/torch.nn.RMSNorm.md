# RMSNorm

*class*torch.nn.RMSNorm(*normalized_shape*, *eps=None*, *elementwise_affine=True*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/8df61039f8235b92b0ca250355cc296020f46e2d/torch/nn/modules/normalization.py#L343)

Applies Root Mean Square Layer Normalization over a mini-batch of inputs.

This layer implements the operation as described in
the paper [Root Mean Square Layer Normalization](https://arxiv.org/pdf/1910.07467.pdf)

yi=xiRMS(x)∗γi,whereRMS(x)=ϵ+1n∑i=1nxi2y_i = \frac{x_i}{\mathrm{RMS}(x)} * \gamma_i, \quad
\text{where} \quad \text{RMS}(x) = \sqrt{\epsilon + \frac{1}{n} \sum_{i=1}^{n} x_i^2}

yi​=RMS(x)xi​​∗γi​,whereRMS(x)=ϵ+n1​i=1∑n​xi2​​

The RMS is taken over the last `D` dimensions, where `D`
is the dimension of `normalized_shape`. For example, if `normalized_shape`
is `(3, 5)` (a 2-dimensional shape), the RMS is computed over
the last 2 dimensions of the input.

Parameters:

- **normalized_shape** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*torch.Size*](../size.html#torch.Size)) -

input shape from an expected input
of size

[∗×normalized_shape[0]×normalized_shape[1]×...×normalized_shape[−1]][* \times \text{normalized\_shape}[0] \times \text{normalized\_shape}[1]
 \times \ldots \times \text{normalized\_shape}[-1]]

[∗×normalized_shape[0]×normalized_shape[1]×...×normalized_shape[−1]]

If a single integer is used, it is treated as a singleton list, and this module will
normalize over the last dimension which is expected to be of that specific size.
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - a value added to the denominator for numerical stability.
If not specified, uses the machine epsilon of the computation (opmath) type:
fp16/bf16 and fp32 inputs use `torch.finfo(torch.float32).eps`, while fp64
inputs use `torch.finfo(torch.float64).eps`. Default: `None`
- **elementwise_affine** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - a boolean value that when set to `True`, this module
has learnable per-element affine parameters initialized to ones (for weights). Default: `True`.

Shape:

- Input: (N,∗)(N, *)(N,∗)
- Output: (N,∗)(N, *)(N,∗) (same shape as input)

Examples:

```
>>> rms_norm = nn.RMSNorm([2, 3])
>>> input = torch.randn(2, 2, 3)
>>> rms_norm(input)
```

extra_repr()[[source]](https://github.com/pytorch/pytorch/blob/8df61039f8235b92b0ca250355cc296020f46e2d/torch/nn/modules/normalization.py#L429)

Return the extra representation of the module.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

forward(*x*)[[source]](https://github.com/pytorch/pytorch/blob/8df61039f8235b92b0ca250355cc296020f46e2d/torch/nn/modules/normalization.py#L423)

Runs the forward pass.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

reset_parameters()[[source]](https://github.com/pytorch/pytorch/blob/8df61039f8235b92b0ca250355cc296020f46e2d/torch/nn/modules/normalization.py#L416)

Resets parameters based on their initialization used in __init__.