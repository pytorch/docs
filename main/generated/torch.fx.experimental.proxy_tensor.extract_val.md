# torch.fx.experimental.proxy_tensor.extract_val

torch.fx.experimental.proxy_tensor.extract_val(*val*, *include_real=False*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/fx/experimental/proxy_tensor.py#L732)

Return type:

None | [*SymInt*](../torch.html#torch.SymInt) | [*SymFloat*](../torch.html#torch.SymFloat) | [*SymBool*](../torch.html#torch.SymBool) | *CustomClassBase* | *ScriptObject* | *FakeScriptObject* | *BackwardState* | [list](https://docs.python.org/3/builtins/stdtypes.html#list)[_ExtractValType] | [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[_ExtractValType, ...] | [dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), _ExtractValType] | [*Tensor*](../tensors.html#torch.Tensor) | [int](https://docs.python.org/3/builtins/functions.html#int) | [float](https://docs.python.org/3/builtins/functions.html#float) | [bool](https://docs.python.org/3/builtins/functions.html#bool)