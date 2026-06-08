# Linear

*class*torch.ao.nn.quantized.dynamic.Linear(*in_features*, *out_features*, *bias_=True*, *dtype=torch.qint8*)[[source]](https://github.com/pytorch/pytorch/blob/411c8477fa2478b2318f3823d57cf684a3a1f389/torch/ao/nn/quantized/dynamic/modules/linear.py#L13)

A dynamic quantized linear module with floating point tensor as inputs and outputs.
We adopt the same interface as torch.nn.Linear, please see
[https://pytorch.org/docs/stable/nn.html#torch.nn.Linear](https://pytorch.org/docs/stable/nn.html#torch.nn.Linear) for documentation.

Similar to [`torch.nn.Linear`](torch.nn.Linear.html#torch.nn.Linear), attributes will be randomly
initialized at module creation time and will be overwritten later

Variables:

- **weight** ([*Tensor*](../tensors.html#torch.Tensor)) - the non-learnable quantized weights of the module which are of
shape (out_features,in_features)(\text{out\_features}, \text{in\_features})(out_features,in_features).
- **bias** ([*Tensor*](../tensors.html#torch.Tensor)) - the non-learnable floating point bias of the module of shape
(out_features)(\text{out\_features})(out_features). If `bias` is `True`,
the values are initialized to zero.

Examples:

```
>>> m = nn.quantized.dynamic.Linear(20, 30)
>>> input = torch.randn(128, 20)
>>> output = m(input)
>>> print(output.size())
torch.Size([128, 30])
```

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/411c8477fa2478b2318f3823d57cf684a3a1f389/torch/ao/nn/quantized/dynamic/modules/linear.py#L100)

Create a dynamic quantized module from a float module or qparams_dict

Parameters:

**mod** ([*Module*](torch.nn.Module.html#torch.nn.Module)) - a float module, either produced by torch.ao.quantization
utilities or provided by the user

*classmethod*from_reference(*ref_qlinear*)[[source]](https://github.com/pytorch/pytorch/blob/411c8477fa2478b2318f3823d57cf684a3a1f389/torch/ao/nn/quantized/dynamic/modules/linear.py#L154)

Create a (fbgemm/qnnpack) dynamic quantized module from a reference quantized
module
:param ref_qlinear: a reference quantized module, either produced by
:type ref_qlinear: Module
:param torch.ao.quantization functions or provided by the user: