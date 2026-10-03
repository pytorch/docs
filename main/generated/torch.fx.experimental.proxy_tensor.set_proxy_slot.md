# torch.fx.experimental.proxy_tensor.set_proxy_slot

torch.fx.experimental.proxy_tensor.set_proxy_slot(*obj: [Tensor](../tensors.html#torch.Tensor)*, *tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *proxy: _ProxyTensor*) → [None](https://docs.python.org/3/builtins/constants.html#None)[[source]](https://github.com/pytorch/pytorch/blob/8ab13d788b9dab3e338e618576e65bb8b0c75e1a/torch/fx/experimental/proxy_tensor.py#L286)

torch.fx.experimental.proxy_tensor.set_proxy_slot(*obj: ScriptObject | FakeScriptObject | CustomClassBase*, *tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *proxy: [Proxy](../fx.html#torch.fx.Proxy)*) → [None](https://docs.python.org/3/builtins/constants.html#None)

torch.fx.experimental.proxy_tensor.set_proxy_slot(*obj: [SymInt](../torch.html#torch.SymInt) | [SymFloat](../torch.html#torch.SymFloat) | [SymBool](../torch.html#torch.SymBool)*, *tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *proxy: Thunk[[Proxy](../fx.html#torch.fx.Proxy)]*) → [None](https://docs.python.org/3/builtins/constants.html#None)