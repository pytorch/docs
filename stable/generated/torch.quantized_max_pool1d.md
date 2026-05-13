# torch.quantized_max_pool1d

torch.quantized_max_pool1d(*input*, *kernel_size*, *stride=[]*, *padding=0*, *dilation=1*, *ceil_mode=False*) → [Tensor](../tensors.html#torch.Tensor)

Applies a 1D max pooling over an input quantized tensor composed of several input planes.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - quantized tensor
- **kernel_size** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*of*[*int*](https://docs.python.org/3/library/functions.html#int)) - the size of the sliding window
- **stride** (`list of int`, optional) - the stride of the sliding window
- **padding** (`list of int`, optional) - padding to be added on both sides, must be >= 0 and <= kernel_size / 2
- **dilation** (`list of int`, optional) - The stride between elements within a sliding window, must be > 0. Default 1
- **ceil_mode** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If True, will use ceil instead of floor to compute the output shape.
Defaults to False.

Returns:

A quantized tensor with max_pool1d applied.

Return type:

[Tensor](../tensors.html#torch.Tensor)

Example:

```
>>> qx = torch.quantize_per_tensor(torch.rand(2, 2), 1.5, 3, torch.quint8)
>>> torch.quantized_max_pool1d(qx, [2])
tensor([[0.0000],
 [1.5000]], size=(2, 1), dtype=torch.quint8,
 quantization_scheme=torch.per_tensor_affine, scale=1.5, zero_point=3)
```