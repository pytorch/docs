# torch.fake_quantize_per_tensor_affine

torch.fake_quantize_per_tensor_affine(*input*, *scale*, *zero_point*, *quant_min*, *quant_max*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the data in `input` fake quantized using `scale`,
`zero_point`, `quant_min` and `quant_max`.

output=(min(quant_max,max(quant_min,std::nearby_int(input/scale)+zero_point))−zero_point)×scale\text{output} = (
 min(
 \text{quant\_max},
 max(
 \text{quant\_min},
 \text{std::nearby\_int}(\text{input} / \text{scale}) + \text{zero\_point}
 )
 ) - \text{zero\_point}
) \times \text{scale}

output=(min(quant_max,max(quant_min,std::nearby_int(input/scale)+zero_point))−zero_point)×scale
Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input value(s), `torch.float32` tensor
- **scale** (double scalar or `float32` Tensor) - quantization scale
- **zero_point** (int64 scalar or `int32` Tensor) - quantization zero_point
- **quant_min** (*int64*) - lower bound of the quantized domain
- **quant_max** (*int64*) - upper bound of the quantized domain

Returns:

A newly fake_quantized `torch.float32` tensor

Return type:

[Tensor](../tensors.html#torch.Tensor)

Example:

```
>>> x = torch.randn(4)
>>> x
tensor([ 0.0552, 0.9730, 0.3973, -1.0780])
>>> torch.fake_quantize_per_tensor_affine(x, 0.1, 0, 0, 255)
tensor([0.1000, 1.0000, 0.4000, 0.0000])
>>> torch.fake_quantize_per_tensor_affine(x, torch.tensor(0.1), torch.tensor(0), 0, 255)
tensor([0.1000, 1.0000, 0.4000, 0.0000])
```