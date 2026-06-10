# quantize_per_channel

*class*torch.quantize_per_channel(*input*, *scales*, *zero_points*, *axis*, *dtype*)

Converts a float tensor to a per-channel quantized tensor with given scales and zero points.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - float tensor to quantize
- **scales** ([*Tensor*](../tensors.html#torch.Tensor)) - float 1D tensor of scales to use, size should match `input.size(axis)`
- **zero_points** ([*int*](https://docs.python.org/3/library/functions.html#int)) - integer 1D tensor of offset to use, size should match `input.size(axis)`
- **axis** ([*int*](https://docs.python.org/3/library/functions.html#int)) - dimension on which apply per-channel quantization
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype)) - the desired data type of returned tensor.
Has to be one of the quantized dtypes: `torch.quint8`, `torch.qint8`, `torch.qint32`

Returns:

A newly quantized tensor

Return type:

[Tensor](../tensors.html#torch.Tensor)

Example:

```
>>> x = torch.tensor([[-1.0, 0.0], [1.0, 2.0]])
>>> torch.quantize_per_channel(x, torch.tensor([0.1, 0.01]), torch.tensor([10, 0]), 0, torch.quint8)
tensor([[-1., 0.],
 [ 1., 2.]], size=(2, 2), dtype=torch.quint8,
 quantization_scheme=torch.per_channel_affine,
 scale=tensor([0.1000, 0.0100], dtype=torch.float64),
 zero_point=tensor([10, 0]), axis=0)
>>> torch.quantize_per_channel(x, torch.tensor([0.1, 0.01]), torch.tensor([10, 0]), 0, torch.quint8).int_repr()
tensor([[ 0, 10],
 [100, 200]], dtype=torch.uint8)
```