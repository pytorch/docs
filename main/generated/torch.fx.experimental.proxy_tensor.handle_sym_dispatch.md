# torch.fx.experimental.proxy_tensor.handle_sym_dispatch

torch.fx.experimental.proxy_tensor.handle_sym_dispatch(*func*, *args*, *kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/fx/experimental/proxy_tensor.py#L3413)

Call into the currently active proxy tracing mode to do a
SymInt/SymFloat/SymBool dispatch trace on a function that operates on
these arguments.

Return type:

*R*