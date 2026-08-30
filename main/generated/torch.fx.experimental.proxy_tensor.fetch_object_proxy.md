# torch.fx.experimental.proxy_tensor.fetch_object_proxy

torch.fx.experimental.proxy_tensor.fetch_object_proxy(*tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *t: [Tensor](../tensors.html#torch.Tensor)*) → _ProxyTensor | [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/9f46548f5371f0271c651e4ec060c44956128533/torch/fx/experimental/proxy_tensor.py#L1098)

torch.fx.experimental.proxy_tensor.fetch_object_proxy(*tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *t: ScriptObject | FakeScriptObject*) → [Proxy](../fx.html#torch.fx.Proxy) | ScriptObject | FakeScriptObject

torch.fx.experimental.proxy_tensor.fetch_object_proxy(*tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *t: [SymInt](../torch.html#torch.SymInt) | [SymFloat](../torch.html#torch.SymFloat) | [SymBool](../torch.html#torch.SymBool)*) → Thunk[[Proxy](../fx.html#torch.fx.Proxy)] | [SymInt](../torch.html#torch.SymInt) | [SymFloat](../torch.html#torch.SymFloat) | [SymBool](../torch.html#torch.SymBool)

torch.fx.experimental.proxy_tensor.fetch_object_proxy(*tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *t: CustomClassBase*) → [Proxy](../fx.html#torch.fx.Proxy) | [SymInt](../torch.html#torch.SymInt) | [SymFloat](../torch.html#torch.SymFloat) | [SymBool](../torch.html#torch.SymBool)