# torch.fx.experimental.proxy_tensor.fetch_object_proxy

torch.fx.experimental.proxy_tensor.fetch_object_proxy(*tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *t: [Tensor](../tensors.html#torch.Tensor)*) → _ProxyTensor | [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/f8a8dd25ad84298ffbd713e8dbdb5bba38ef907d/torch/fx/experimental/proxy_tensor.py#L1142)

torch.fx.experimental.proxy_tensor.fetch_object_proxy(*tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *t: ScriptObject | FakeScriptObject*) → [Proxy](../fx.html#torch.fx.Proxy) | ScriptObject | FakeScriptObject

torch.fx.experimental.proxy_tensor.fetch_object_proxy(*tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *t: [SymInt](../torch.html#torch.SymInt) | [SymFloat](../torch.html#torch.SymFloat) | [SymBool](../torch.html#torch.SymBool)*) → Thunk[[Proxy](../fx.html#torch.fx.Proxy)] | [SymInt](../torch.html#torch.SymInt) | [SymFloat](../torch.html#torch.SymFloat) | [SymBool](../torch.html#torch.SymBool)

torch.fx.experimental.proxy_tensor.fetch_object_proxy(*tracer: PythonKeyTracer | _GraphAppendingTracerEx*, *t: CustomClassBase*) → [Proxy](../fx.html#torch.fx.Proxy) | [SymInt](../torch.html#torch.SymInt) | [SymFloat](../torch.html#torch.SymFloat) | [SymBool](../torch.html#torch.SymBool)