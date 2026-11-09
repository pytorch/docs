# torch.fx.experimental.proxy_tensor.fetch_sym_proxy

torch.fx.experimental.proxy_tensor.fetch_sym_proxy(*tracer*)[[source]](https://github.com/pytorch/pytorch/blob/50d50e722913b05a0762c886507c9be7ae43d2f3/torch/fx/experimental/proxy_tensor.py#L1085)

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*SymInt*](../torch.html#torch.SymInt) | [*SymFloat*](../torch.html#torch.SymFloat) | [*SymBool*](../torch.html#torch.SymBool)], [bool](https://docs.python.org/3/builtins/functions.html#bool) | [int](https://docs.python.org/3/builtins/functions.html#int) | [float](https://docs.python.org/3/builtins/functions.html#float) | [*Proxy*](../fx.html#torch.fx.Proxy)]