# Linear

*class*torch.ao.nn.quantized.Linear(*in_features*, *out_features*, *bias_=True*, *dtype=torch.qint8*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/ao/nn/quantized/modules/linear.py#L117)

A quantized linear module with quantized tensor as inputs and outputs.
We adopt the same interface as torch.nn.Linear, please see
[https://pytorch.org/docs/stable/nn.html#torch.nn.Linear](https://pytorch.org/docs/stable/nn.html#torch.nn.Linear) for documentation.

Similar to [`Linear`](torch.nn.Linear.html#torch.nn.Linear), attributes will be randomly
initialized at module creation time and will be overwritten later

Variables:

- **weight** ([*Tensor*](../tensors.html#torch.Tensor)) - the non-learnable quantized weights of the module of
shape (out_features,in_features)(\text{out\_features}, \text{in\_features})(out_features,in_features).
- **bias** ([*Tensor*](../tensors.html#torch.Tensor)) - the non-learnable bias of the module of shape (out_features)(\text{out\_features})(out_features).
If `bias` is `True`, the values are initialized to zero.
- **scale** - scale parameter of output Quantized Tensor, type: double
- **zero_point** - zero_point parameter for output Quantized Tensor, type: long

Examples:

```
>>> m = nn.quantized.Linear(20, 30)
>>> input = torch.randn(128, 20)
>>> input = torch.quantize_per_tensor(input, 1.0, 0, torch.quint8)
>>> output = m(input)
>>> print(output.size())
torch.Size([128, 30])
```

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/ao/nn/quantized/modules/linear.py#L282)

Create a quantized module from an observed float module

Parameters:

- **mod** ([*Module*](torch.nn.Module.html#torch.nn.Module)) - a float module, either produced by torch.ao.quantization
utilities or provided by the user
- **use_precomputed_fake_quant** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - if True, the module will reuse min/max
values from the precomputed fake quant module.

*classmethod*from_reference(*ref_qlinear*, *output_scale*, *output_zero_point*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/ao/nn/quantized/modules/linear.py#L346)

Create a (fbgemm/qnnpack) quantized module from a reference quantized module

Parameters:

- **ref_qlinear** ([*Module*](torch.nn.Module.html#torch.nn.Module)) - a reference quantized linear module, either produced by torch.ao.quantization
utilities or provided by the user
- **output_scale** ([*float*](https://docs.python.org/3/library/functions.html#float)) - scale for output Tensor
- **output_zero_point** ([*int*](https://docs.python.org/3/library/functions.html#int)) - zero point for output Tensor