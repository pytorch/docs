# torch.fx.experimental.proxy_tensor.extract_val

torch.fx.experimental.proxy_tensor.extract_val(*val*, *include_real=False*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/fx/experimental/proxy_tensor.py#L713)

Return type:

None | [*SymInt*](../torch.html#torch.SymInt) | [*SymFloat*](../torch.html#torch.SymFloat) | [*SymBool*](../torch.html#torch.SymBool) | *OpaqueBase* | *ScriptObject* | *FakeScriptObject* | *BackwardState* | [list](https://docs.python.org/3/library/stdtypes.html#list)[_ExtractValType] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[_ExtractValType, ...] | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), _ExtractValType] | [*Tensor*](../tensors.html#torch.Tensor) | [int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float) | [bool](https://docs.python.org/3/library/functions.html#bool)