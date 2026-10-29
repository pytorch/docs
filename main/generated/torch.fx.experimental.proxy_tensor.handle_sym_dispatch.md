# torch.fx.experimental.proxy_tensor.handle_sym_dispatch

torch.fx.experimental.proxy_tensor.handle_sym_dispatch(*func*, *args*, *kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/fx/experimental/proxy_tensor.py#L3586)

Call into the currently active proxy tracing mode to do a
SymInt/SymFloat/SymBool dispatch trace on a function that operates on
these arguments.

Return type:

*R*