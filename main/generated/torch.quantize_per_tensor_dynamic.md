# torch.quantize_per_tensor_dynamic

torch.quantize_per_tensor_dynamic(*input*, *dtype*, *reduce_range*) → [Tensor](../tensors.html#torch.Tensor)

Converts a float tensor to a quantized tensor with scale and zero_point calculated
dynamically based on the input.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - float tensor or list of tensors to quantize
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype)) - the desired data type of returned tensor.
Has to be one of the quantized dtypes: `torch.quint8`, `torch.qint8`
- **reduce_range** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - a flag to indicate whether to reduce the range of quantized
- **bit** (*data by 1*) -
- **hardwares** (*it's required to avoid instruction overflow for some*) -

Returns:

A newly (dynamically) quantized tensor

Return type:

[Tensor](../tensors.html#torch.Tensor)

Example:

```
>>> t = torch.quantize_per_tensor_dynamic(torch.tensor([-1.0, 0.0, 1.0, 2.0]), torch.quint8, False)
>>> print(t)
tensor([-1., 0., 1., 2.], size=(4,), dtype=torch.quint8,
 quantization_scheme=torch.per_tensor_affine, scale=0.011764705882352941,
 zero_point=85)
>>> t.int_repr()
tensor([ 0, 85, 170, 255], dtype=torch.uint8)
```