# torch.fx.experimental.proxy_tensor.fetch_sym_proxy

torch.fx.experimental.proxy_tensor.fetch_sym_proxy(*tracer*)[[source]](https://github.com/pytorch/pytorch/blob/bdfbe0c16b37fa7a4c09348321cabd906cb4019a/torch/fx/experimental/proxy_tensor.py#L1085)

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*SymInt*](../torch.html#torch.SymInt) | [*SymFloat*](../torch.html#torch.SymFloat) | [*SymBool*](../torch.html#torch.SymBool)], [bool](https://docs.python.org/3/builtins/functions.html#bool) | [int](https://docs.python.org/3/builtins/functions.html#int) | [float](https://docs.python.org/3/builtins/functions.html#float) | [*Proxy*](../fx.html#torch.fx.Proxy)]