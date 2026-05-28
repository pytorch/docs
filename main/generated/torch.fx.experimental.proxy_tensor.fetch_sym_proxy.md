# torch.fx.experimental.proxy_tensor.fetch_sym_proxy

torch.fx.experimental.proxy_tensor.fetch_sym_proxy(*tracer*)[[source]](https://github.com/pytorch/pytorch/blob/fd6d216e3e8bf07c470716dfbf022d82fadd521d/torch/fx/experimental/proxy_tensor.py#L1002)

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*SymInt*](../torch.html#torch.SymInt) | [*SymFloat*](../torch.html#torch.SymFloat) | [*SymBool*](../torch.html#torch.SymBool)], [bool](https://docs.python.org/3/library/functions.html#bool) | [int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float) | [*Proxy*](../fx.html#torch.fx.Proxy)]