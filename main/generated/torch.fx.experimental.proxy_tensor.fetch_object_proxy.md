# torch.fx.experimental.proxy_tensor.fetch_object_proxy

torch.fx.experimental.proxy_tensor.fetch_object_proxy(*tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *t: [Tensor](../tensors.html#torch.Tensor)*) → _ProxyTensor | [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/4ff2d1161191378e895e560774c1622dba40076d/torch/fx/experimental/proxy_tensor.py#L1051)

torch.fx.experimental.proxy_tensor.fetch_object_proxy(*tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *t: ScriptObject | FakeScriptObject*) → [Proxy](../fx.html#torch.fx.Proxy) | ScriptObject | FakeScriptObject

torch.fx.experimental.proxy_tensor.fetch_object_proxy(*tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *t: [SymInt](../torch.html#torch.SymInt) | [SymFloat](../torch.html#torch.SymFloat) | [SymBool](../torch.html#torch.SymBool)*) → Thunk[[Proxy](../fx.html#torch.fx.Proxy)] | [SymInt](../torch.html#torch.SymInt) | [SymFloat](../torch.html#torch.SymFloat) | [SymBool](../torch.html#torch.SymBool)

torch.fx.experimental.proxy_tensor.fetch_object_proxy(*tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *t: OpaqueBase*) → [Proxy](../fx.html#torch.fx.Proxy) | [SymInt](../torch.html#torch.SymInt) | [SymFloat](../torch.html#torch.SymFloat) | [SymBool](../torch.html#torch.SymBool)