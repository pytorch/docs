# torch.quantized_batch_norm

torch.quantized_batch_norm(*input*, *weight=None*, *bias=None*, *mean*, *var*, *eps*, *output_scale*, *output_zero_point*) → [Tensor](../tensors.html#torch.Tensor)

Applies batch normalization on a 4D (NCHW) quantized tensor.

y=x−E[x]Var[x]+ϵ∗γ+βy = \frac{x - \mathrm{E}[x]}{\sqrt{\mathrm{Var}[x] + \epsilon}} * \gamma + \betay=Var[x]+ϵ​x−E[x]​∗γ+β
Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - quantized tensor
- **weight** ([*Tensor*](../tensors.html#torch.Tensor)) - float tensor that corresponds to the gamma, size C
- **bias** ([*Tensor*](../tensors.html#torch.Tensor)) - float tensor that corresponds to the beta, size C
- **mean** ([*Tensor*](../tensors.html#torch.Tensor)) - float mean value in batch normalization, size C
- **var** ([*Tensor*](../tensors.html#torch.Tensor)) - float tensor for variance, size C
- **eps** ([*float*](https://docs.python.org/3/library/functions.html#float)) - a value added to the denominator for numerical stability.
- **output_scale** ([*float*](https://docs.python.org/3/library/functions.html#float)) - output quantized tensor scale
- **output_zero_point** ([*int*](https://docs.python.org/3/library/functions.html#int)) - output quantized tensor zero_point

Returns:

A quantized tensor with batch normalization applied.

Return type:

[Tensor](../tensors.html#torch.Tensor)

Example:

```
>>> qx = torch.quantize_per_tensor(torch.rand(2, 2, 2, 2), 1.5, 3, torch.quint8)
>>> torch.quantized_batch_norm(qx, torch.ones(2), torch.zeros(2), torch.rand(2), torch.rand(2), 0.00001, 0.2, 2)
tensor([[[[-0.2000, -0.2000],
 [ 1.6000, -0.2000]],

 [[-0.4000, -0.4000],
 [-0.4000, 0.6000]]],

 [[[-0.2000, -0.2000],
 [-0.2000, -0.2000]],

 [[ 0.6000, -0.4000],
 [ 0.6000, -0.4000]]]], size=(2, 2, 2, 2), dtype=torch.quint8,
 quantization_scheme=torch.per_tensor_affine, scale=0.2, zero_point=2)
```