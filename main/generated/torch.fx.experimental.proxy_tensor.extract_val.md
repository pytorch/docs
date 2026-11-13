# torch.fx.experimental.proxy_tensor.extract_val

torch.fx.experimental.proxy_tensor.extract_val(*val*, *include_real=False*)[[source]](https://github.com/pytorch/pytorch/blob/b896199bee9ca0e125f6ec366a265418a8f3290e/torch/fx/experimental/proxy_tensor.py#L762)

Return type:

None | [*SymInt*](../torch.html#torch.SymInt) | [*SymFloat*](../torch.html#torch.SymFloat) | [*SymBool*](../torch.html#torch.SymBool) | *CustomClassBase* | *ScriptObject* | *FakeScriptObject* | *BackwardState* | [list](https://docs.python.org/3/builtins/stdtypes.html#list)[_ExtractValType] | [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[_ExtractValType, ...] | [dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), _ExtractValType] | [*Tensor*](../tensors.html#torch.Tensor) | [int](https://docs.python.org/3/builtins/functions.html#int) | [float](https://docs.python.org/3/builtins/functions.html#float) | [bool](https://docs.python.org/3/builtins/functions.html#bool)