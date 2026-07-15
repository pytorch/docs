# torch.fx.experimental.proxy_tensor.set_proxy_slot

torch.fx.experimental.proxy_tensor.set_proxy_slot(*obj: [Tensor](../tensors.html#torch.Tensor)*, *tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *proxy: _ProxyTensor*) → [None](https://docs.python.org/3/library/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/0f5932e5e82c3a4da21331c6cf7cddf6bce55cff/torch/fx/experimental/proxy_tensor.py#L285)

torch.fx.experimental.proxy_tensor.set_proxy_slot(*obj: ScriptObject | FakeScriptObject | CustomClassBase*, *tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *proxy: [Proxy](../fx.html#torch.fx.Proxy)*) → [None](https://docs.python.org/3/library/constants.html#None)

torch.fx.experimental.proxy_tensor.set_proxy_slot(*obj: [SymInt](../torch.html#torch.SymInt) | [SymFloat](../torch.html#torch.SymFloat) | [SymBool](../torch.html#torch.SymBool)*, *tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *proxy: Thunk[[Proxy](../fx.html#torch.fx.Proxy)]*) → [None](https://docs.python.org/3/library/constants.html#None)