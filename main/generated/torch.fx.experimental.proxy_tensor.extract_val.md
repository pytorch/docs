# torch.fx.experimental.proxy_tensor.extract_val

torch.fx.experimental.proxy_tensor.extract_val(*val*, *include_real=False*)[[source]](https://github.com/pytorch/pytorch/blob/52b7da3f54bb5af4e72fc6040fc43f091267ad09/torch/fx/experimental/proxy_tensor.py#L702)

Return type:

None | [*SymInt*](../torch.html#torch.SymInt) | [*SymFloat*](../torch.html#torch.SymFloat) | [*SymBool*](../torch.html#torch.SymBool) | *OpaqueBase* | *ScriptObject* | *FakeScriptObject* | *BackwardState* | [list](https://docs.python.org/3/library/stdtypes.html#list)[_ExtractValType] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[_ExtractValType, ...] | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), _ExtractValType] | [*Tensor*](../tensors.html#torch.Tensor) | [int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float) | [bool](https://docs.python.org/3/library/functions.html#bool)